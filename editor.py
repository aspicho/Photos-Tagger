# Form implementation generated from reading ui file 'editor.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(964, 683)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.main_tab = QtWidgets.QWidget()
        self.main_tab.setObjectName("main_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.graphicsView = QtWidgets.QGraphicsView(self.main_tab)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_4.addWidget(self.graphicsView)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.searchQuerry = QtWidgets.QLineEdit(self.main_tab)
        self.searchQuerry.setMinimumSize(QtCore.QSize(143, 0))
        self.searchQuerry.setMaximumSize(QtCore.QSize(143, 16777215))
        self.searchQuerry.setObjectName("searchQuerry")
        self.horizontalLayout_5.addWidget(self.searchQuerry)
        self.searchButton = QtWidgets.QPushButton(self.main_tab)
        self.searchButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_5.addWidget(self.searchButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.scrollArea = QtWidgets.QScrollArea(self.main_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(178, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(178, 16777215))
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 178, 509))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(178, 0))
        self.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(178, 16777215))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollAreaArea = QtWidgets.QVBoxLayout()
        self.scrollAreaArea.setObjectName("scrollAreaArea")
        self.verticalLayout_3.addLayout(self.scrollAreaArea)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.verticalLayout_4.setStretch(1, 20)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.horizontalLayout_4.setStretch(0, 9)
        self.horizontalLayout_4.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(self.main_tab)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.boxes = QtWidgets.QVBoxLayout()
        self.boxes.setObjectName("boxes")
        self.checkBoxes2 = QtWidgets.QHBoxLayout()
        self.checkBoxes2.setObjectName("checkBoxes2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.checkBoxes2.addItem(spacerItem)
        self.boxes.addLayout(self.checkBoxes2)
        self.checkBoxes1 = QtWidgets.QHBoxLayout()
        self.checkBoxes1.setObjectName("checkBoxes1")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.checkBoxes1.addItem(spacerItem1)
        self.boxes.addLayout(self.checkBoxes1)
        self.horizontalLayout_3.addLayout(self.boxes)
        self.line_2 = QtWidgets.QFrame(self.main_tab)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        self.stats = QtWidgets.QVBoxLayout()
        self.stats.setObjectName("stats")
        self.index = QtWidgets.QLabel(self.main_tab)
        self.index.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.index.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.index.setObjectName("index")
        self.stats.addWidget(self.index)
        self.path = QtWidgets.QLabel(self.main_tab)
        self.path.setMaximumSize(QtCore.QSize(150, 16777215))
        self.path.setObjectName("path")
        self.stats.addWidget(self.path)
        self.horizontalLayout_3.addLayout(self.stats)
        self.buttons = QtWidgets.QVBoxLayout()
        self.buttons.setObjectName("buttons")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.previousButton = QtWidgets.QPushButton(self.main_tab)
        self.previousButton.setObjectName("previousButton")
        self.horizontalLayout.addWidget(self.previousButton)
        self.nextButton = QtWidgets.QPushButton(self.main_tab)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout.addWidget(self.nextButton)
        self.buttons.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.loadButton = QtWidgets.QPushButton(self.main_tab)
        self.loadButton.setObjectName("loadButton")
        self.horizontalLayout_2.addWidget(self.loadButton)
        self.saveButton = QtWidgets.QPushButton(self.main_tab)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_2.addWidget(self.saveButton)
        self.buttons.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.buttons)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.main_tab, "")
        self.settings_tab = QtWidgets.QWidget()
        self.settings_tab.setObjectName("settings_tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.settings_tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.settings = QtWidgets.QVBoxLayout()
        self.settings.setObjectName("settings")
        self.label = QtWidgets.QLabel(self.settings_tab)
        self.label.setObjectName("label")
        self.settings.addWidget(self.label)
        self.tagsMenu = QtWidgets.QHBoxLayout()
        self.tagsMenu.setObjectName("tagsMenu")
        self.tagsComboBox = QtWidgets.QComboBox(self.settings_tab)
        self.tagsComboBox.setEditable(True)
        self.tagsComboBox.setCurrentText("")
        self.tagsComboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.tagsComboBox.setObjectName("tagsComboBox")
        self.tagsMenu.addWidget(self.tagsComboBox)
        self.tagAdd = QtWidgets.QPushButton(self.settings_tab)
        self.tagAdd.setObjectName("tagAdd")
        self.tagsMenu.addWidget(self.tagAdd)
        self.tagRemove = QtWidgets.QPushButton(self.settings_tab)
        self.tagRemove.setObjectName("tagRemove")
        self.tagsMenu.addWidget(self.tagRemove)
        self.tagsMenu.setStretch(0, 5)
        self.settings.addLayout(self.tagsMenu)
        self.line_3 = QtWidgets.QFrame(self.settings_tab)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.settings.addWidget(self.line_3)
        self.updateFilesList = QtWidgets.QPushButton(self.settings_tab)
        self.updateFilesList.setObjectName("updateFilesList")
        self.settings.addWidget(self.updateFilesList)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.settings.addItem(spacerItem2)
        self.saveSettings = QtWidgets.QPushButton(self.settings_tab)
        self.saveSettings.setObjectName("saveSettings")
        self.settings.addWidget(self.saveSettings)
        self.horizontalLayout_7.addLayout(self.settings)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 0, 1, 1, 1)
        self.tabWidget.addTab(self.settings_tab, "")
        self.horizontalLayout_6.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchButton.setText(_translate("MainWindow", "0"))
        self.index.setText(_translate("MainWindow", "1/12124"))
        self.path.setText(_translate("MainWindow", "TextLabel"))
        self.previousButton.setText(_translate("MainWindow", "Previous"))
        self.nextButton.setText(_translate("MainWindow", "Next"))
        self.loadButton.setText(_translate("MainWindow", "Load"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main_tab), _translate("MainWindow", "Main"))
        self.label.setText(_translate("MainWindow", "Edit Tags"))
        self.tagAdd.setText(_translate("MainWindow", "Add"))
        self.tagRemove.setText(_translate("MainWindow", "Remove"))
        self.updateFilesList.setText(_translate("MainWindow", "Update list of files"))
        self.saveSettings.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_tab), _translate("MainWindow", "Settings"))
