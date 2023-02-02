import sys
import json
import os
from PyQt6 import QtCore, QtGui, QtWidgets
from editor import Ui_MainWindow as Editor
from start_window import Ui_MainWindow as StartWindow
from folder_widget import Ui_Frame as FolderWidget


class MainWindow(QtWidgets.QMainWindow, Editor):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.setFixedSize(1024, 683)
        self.setWindowIcon(QtGui.QIcon('ico.ico'))
        self.setWindowTitle('Photos Tagger')
        self.checkBoxes = []
        self.scrollButtonsDict = {}
        self.photos = []
        self.tags = []
        self.photoCur = 0
        self.photosData = {'marked': []}
        self.boxesState = []
        self.disabledListButton = ''
        self.finded = []
        self.findedCur = 0
        self.folderName = ''
        self.folderPath = ''

        self.loadButton.clicked.connect(self.on_load_clicked)
        self.saveButton.clicked.connect(self.on_save_clicked)
        self.nextButton.clicked.connect(self.on_next_clicked)
        self.previousButton.clicked.connect(self.on_previous_clicked)
        self.searchButton.clicked.connect(self.search_photo)
        self.tagAdd.clicked.connect(self.add_tag)
        self.tagRemove.clicked.connect(self.remove_tag)
        self.saveSettings.clicked.connect(self.save_settings)
        self.updateFilesList.clicked.connect(self.photos_list_update)

    def start(self):
        self.load()
        self.folderName = self.folderPath.split('/')[-1].split('\\')[-1]

        for photo in self.photos:
            button = QtWidgets.QPushButton(photo)
            button.clicked.connect(self.change_photo)
            button.setMaximumWidth(140)
            self.scrollButtonsDict[photo] = button
            self.scrollAreaArea.addWidget(button)

        self.add_checkBoxes()

        self.set_check_boxes_state(False)

        self.index.setText(f'{self.photoCur+1}/{len(self.photos)}')
        self.path.setText(f'{self.photos[self.photoCur]}')
        self.scrollButtonsDict[self.photos[self.photoCur]].setEnabled(False)
        self.disabledListButton = self.photos[self.photoCur]
        self.tagsComboBox.addItems(self.tags)

        self.scene = QtWidgets.QGraphicsScene()
        self.change_photo(dir='init')
        self.graphicsView.setScene(self.scene)

    def add_checkBoxes(self):
        self.checkBoxes = []

        for box in self.findChildren(QtWidgets.QCheckBox):
            box.deleteLater()

        for name in self.tags:
            box = QtWidgets.QCheckBox(name)
            box.setMinimumWidth(75)
            box.setMaximumWidth(75)
            self.checkBoxes.append(box)

        for id, box in enumerate(self.checkBoxes):
            if id+1 <= len(self.checkBoxes)//2:
                self.checkBoxes1.addWidget(box)
            else:
                self.checkBoxes2.addWidget(box)

    def add_tag(self):
        curText = self.tagsComboBox.currentText()
        if curText not in self.tags:
            self.tags.append(curText)
            self.tagsComboBox.addItem(curText)
            self.tagsComboBox.setCurrentText('')

    def remove_tag(self):
        comboBox = self.tagsComboBox
        curText = comboBox.currentText()
        count = comboBox.count()

        if curText in self.tags:
            self.tags.remove(curText)
            for index in range(count):
                if comboBox.itemText(index) == curText:
                    comboBox.removeItem(index)

    def save_settings(self):
        with open(
                f'{self.folderPath}/Resources/config.json', 'w',
                encoding='utf8'
                ) as f:
            f.write(json.dumps({'tags': self.tags}))

        self.add_checkBoxes()

    def load(self):
        try:
            os.makedirs(f'{self.folderPath}/Resources')
        except OSError:
            pass
        try:
            with open(
                    f'{self.folderPath}/Resources/config.json', 'r',
                    encoding='utf8'
                    ) as f:
                config = json.loads(f.read())
                self.tags = config['tags']
        except FileNotFoundError:
            self.tags = ['Example', 'Example2']
            with open(
                    f'{self.folderPath}/Resources/config.json', 'w',
                    encoding='utf8'
                    ) as f:
                f.write(json.dumps({'tags': self.tags}))
        try:
            self.find_photos()
        except FileNotFoundError:
            try:
                files = os.listdir(self.folderPath)
                for id, file in enumerate(files):
                    if not os.path.isfile(f'{self.folderPath}/{file}'):
                        files.pop(id)
                self.photos = files
                with open(
                        f'{self.folderPath}/Resources/files.json', 'w',
                        encoding='utf8'
                        ) as f:
                    f.write(json.dumps(self.photos))
            except OSError:
                self.photos = ['exemple.png']
        try:
            with open(
                    f'{self.folderPath}/Resources/data.json', 'r',
                    encoding='utf8'
                    ) as f:
                self.photosData = json.loads(f.read())
        except FileNotFoundError:
            with open(
                    f'{self.folderPath}/Resources/data.json', 'w',
                    encoding='utf8'
                    ) as f:
                self.photosData['marked'] = [0, len(self.photos)]
                f.write(json.dumps(self.photosData))

    def photos_list_update(self):
        buttons = self.scrollArea.findChildren(QtWidgets.QPushButton)
        for button in buttons:
            button.deleteLater()
        self.find_photos()
        for photo in self.photos:
            button = QtWidgets.QPushButton(photo)
            button.clicked.connect(self.change_photo)
            button.setMaximumWidth(140)
            self.scrollButtonsDict[photo] = button
            self.scrollAreaArea.addWidget(button)
        self.path.setText(f'????')
        self.index.setText(f'{self.photoCur+1}/{len(self.photos)}')

    def find_photos(self):
        with open(
                f'{self.folderPath}/Resources/files.json', 'r',
                encoding='utf8'
                ) as f:
            self.photos = json.loads(f.read())
            files = os.listdir(self.folderPath)
            if len(self.photos) != len(files) - 1:
                for id, file in enumerate(files):
                    if not os.path.isfile(f'{self.folderPath}/{file}'):
                        files.pop(id)
                self.photos = files
                with open(
                        f'{self.folderPath}/Resources/files.json', 'w',
                        encoding='utf8'
                        ) as f:
                    f.write(json.dumps(self.photos))

    def on_load_clicked(self):
        with open(
                f'{self.folderPath}/Resources/data.json', 'r',
                encoding='utf8'
                ) as f:
            self.photosData = json.loads(f.read())
        self.set_check_boxes_state(False)

    def change_photo(self, dir: str = 'next' or 'previous'):
        sender = self.sender()

        if dir == 'init':
            name = self.photos[self.photoCur]
        elif sender.parent().objectName() == 'scrollAreaWidgetContents':
            self.boxesState = self.get_check_boxes_state()
            self.update_photos_data()
            index = self.photos.index(sender.text())
            name = sender.text()
            self.photoCur = index
            self.scrollButtonsDict[self.disabledListButton].setEnabled(True)
            self.disabledListButton = sender.text()
            self.sender().setEnabled(False)
            self.set_check_boxes_state(False)
        elif self.finded:
            try:
                self.findedCur += 1 if dir == 'next' else -1
                self.photoCur = self.photos.index(self.finded[self.findedCur])
                name = self.finded[self.findedCur]
            except IndexError:
                self.findedCur = 0
                self.photoCur = self.photos.index(self.finded[self.findedCur])
                name = self.finded[self.findedCur]
            if self.findedCur == -1:
                self.findedCur = len(self.finded) - 1
                self.photoCur = self.photos.index(self.finded[self.findedCur])
                name = self.finded[self.findedCur]
        else:
            try:
                self.photoCur += 1 if dir == 'next' else -1
                name = self.photos[self.photoCur]
            except IndexError:
                self.photoCur = 0
                name = self.photos[self.photoCur]
            if self.photoCur == -1:
                self.photoCur = len(self.photos) - 1
                name = self.photos[self.photoCur]

        self.scrollButtonsDict[self.disabledListButton].setEnabled(True)
        self.disabledListButton = name
        self.scrollButtonsDict[name].setEnabled(False)

        self.scene.clear()
        self.index.setText(f'{self.photoCur+1}/{len(self.photos)}')
        self.path.setText(f'{name}')
        self.pixmap = QtGui.QPixmap(f'{self.folderPath}/{name}')
        self.pixmap = self.pixmap.scaledToHeight(self.graphicsView.height()-25)
        self.pixmap_item = QtWidgets.QGraphicsPixmapItem(self.pixmap)
        self.scene.addItem(self.pixmap_item)

    def search_photo(self):
        finded = []
        querry = self.searchQuerry.text()
        for i in self.photos:
            if querry in i and (len(querry) > 0):
                self.scrollButtonsDict[i].show()
                finded.append(i)
            elif (len(querry) == 0):
                self.scrollButtonsDict[i].show()
            else:
                self.scrollButtonsDict[i].hide()
        self.finded = finded

    def update_photos_data(self):
        data = {}
        name = self.photos[self.photoCur].split('/')[-1]
        data['categories'] = self.boxesState
        data['path'] = f'{self.folderPath}/{self.photos[self.photoCur]}'
        self.photosData[name] = data
        self.photosData['marked'][0] = len(self.photosData) - 1

    def on_save_clicked(self):
        self.boxesState = self.get_check_boxes_state()
        self.update_photos_data()
        with open(
                f'{self.folderPath}/Resources/data.json', 'w',
                encoding='utf8'
                ) as f:
            f.write(json.dumps(self.photosData))

    def on_next_clicked(self):
        self.boxesState = self.get_check_boxes_state()
        self.update_photos_data()
        self.change_photo('next')
        self.set_check_boxes_state(False)

    def on_previous_clicked(self):
        self.boxesState = self.get_check_boxes_state()
        self.update_photos_data()
        self.change_photo('previous')
        self.set_check_boxes_state(False)

    def get_check_boxes_state(self):
        boxesState = []
        for widget in self.checkBoxes:
            boxesState.append((widget.text(), widget.isChecked()))
        return boxesState

    def set_check_boxes_state(self, state):
        curPhotoName = self.photos[self.photoCur]

        if curPhotoName in self.photosData:
            for ctg in self.photosData[curPhotoName]['categories']:
                for box in self.checkBoxes:
                    if box.text() == ctg[0]:
                        box.setChecked(ctg[1])
        else:
            for box in self.findChildren(QtWidgets.QCheckBox):
                box.setChecked(state)


class FolderFrame(QtWidgets.QFrame, FolderWidget):
    def __init__(self, *args, **kwargs):
        super(FolderFrame, self).__init__()
        # QFrame.__init__(self, *args, **kwargs)
        self.setupUi(self)


class StartWindow(QtWidgets.QMainWindow, StartWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(550, 683)
        self.setWindowIcon(QtGui.QIcon('ico.ico'))
        self.setWindowTitle('Photos Tagger')
        self.settings = {'Folders': []}

        self.mainWindow = MainWindow()

        self.load()
        if len(self.settings['Folders']) == 0:
            path = os.path.abspath('data/exemple')
            self.add_frame(path=path)
        else:
            for path in self.settings['Folders']:
                self.add_frame(path=path)

        self.addNew.clicked.connect(self.add_new)

    def add_frame(self, path):
        f = FolderFrame()
        name = path.split('/')[-1].split('\\')[-1]
        f.name.setText(name)
        f.path.setText(path)
        try:
            with open(f'{path}/Resources/data.json', 'r') as f_:
                f_ = json.loads(f_.read())
                f.marked.setText(f"{f_['marked'][0]}/{f_['marked'][1]}")
        except FileNotFoundError:
            f.marked.setText('????/????')
        f.rand.setText('')
        f.delete_.clicked.connect(self.delete)
        f.openEditor.clicked.connect(self.show_main)
        self.scrollAreaArea.addWidget(f)

    def load(self):
        try:
            with open('data/settings.json', 'r') as f:
                self.settings = json.loads(f.read())
        except FileNotFoundError:
            with open('data/settings.json', 'w') as f:
                f.write(json.dumps(self.settings))

    def delete(self):
        path = self.sender().parent().findChild(QtWidgets.QLabel, 'path')
        path = path.text()
        self.sender().parent().deleteLater()
        try:
            self.settings['Folders'].remove(path)
            with open('data/settings.json', 'w') as f:
                f.write(json.dumps(self.settings))
        except ValueError:
            pass

    def add_new(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Select Folder')
        if path in self.settings['Folders']:
            return
        try:
            self.settings['Folders'].append(path)
            with open('data/settings.json', 'w') as f:
                f.write(json.dumps(self.settings))
            self.add_frame(path=path)
        except FileNotFoundError:
            raise Exception('settings file was deleted')

    def show_main(self):
        path = self.sender().parent().findChild(QtWidgets.QLabel, 'path')
        path = path.text()

        self.mainWindow.folderPath = path
        self.mainWindow.start()
        self.mainWindow.show()

        self.destroy()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = StartWindow()
    window.show()
    sys.exit(app.exec())
