# Form implementation generated from reading ui file 'folder_widget.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(446, 74)
        Frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.name = QtWidgets.QLabel(Frame)
        self.name.setWordWrap(True)
        self.name.setObjectName("name")
        self.verticalLayout_6.addWidget(self.name)
        self.path = QtWidgets.QLabel(Frame)
        self.path.setWordWrap(True)
        self.path.setObjectName("path")
        self.verticalLayout_6.addWidget(self.path)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.rand = QtWidgets.QLabel(Frame)
        self.rand.setWordWrap(True)
        self.rand.setObjectName("rand")
        self.verticalLayout_7.addWidget(self.rand)
        self.marked = QtWidgets.QLabel(Frame)
        self.marked.setScaledContents(False)
        self.marked.setWordWrap(True)
        self.marked.setObjectName("marked")
        self.verticalLayout_7.addWidget(self.marked)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.horizontalLayout_6.setStretch(0, 9)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.horizontalLayout_6)
        self.itemButttons_2 = QtWidgets.QVBoxLayout()
        self.itemButttons_2.setObjectName("itemButttons_2")
        self.openEditor = QtWidgets.QPushButton(Frame)
        self.openEditor.setMaximumSize(QtCore.QSize(80, 16777215))
        self.openEditor.setObjectName("openEditor")
        self.itemButttons_2.addWidget(self.openEditor)
        self.delete_ = QtWidgets.QPushButton(Frame)
        self.delete_.setMaximumSize(QtCore.QSize(80, 16777215))
        self.delete_.setObjectName("delete_")
        self.itemButttons_2.addWidget(self.delete_)
        self.horizontalLayout.addLayout(self.itemButttons_2)
        self.horizontalLayout.setStretch(0, 9)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.name.setText(_translate("Frame", "Name"))
        self.path.setText(_translate("Frame", "Path"))
        self.rand.setText(_translate("Frame", "Idk Some random"))
        self.marked.setText(_translate("Frame", "MarkedCount/AllFiles"))
        self.openEditor.setText(_translate("Frame", "Open Editor"))
        self.delete_.setText(_translate("Frame", "Delete"))
