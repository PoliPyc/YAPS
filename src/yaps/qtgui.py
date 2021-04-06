# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yaps.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self, yaps):
        self.yaps = yaps

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, 9, 801, 441))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.picturesGrid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.picturesGrid.setContentsMargins(0, 0, 0, 0)
        self.picturesGrid.setObjectName("picturesGrid")
        self.pictureEmptyLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pictureEmptyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pictureEmptyLabel.setObjectName("pictureEmptyLabel")
        self.picturesGrid.addWidget(self.pictureEmptyLabel, 0, 0, 1, 1)
        self.findDuplicatesButton = QtWidgets.QPushButton(self.centralwidget)
        self.findDuplicatesButton.setGeometry(QtCore.QRect(30, 470, 131, 28))
        self.findDuplicatesButton.setObjectName("findDuplicatesButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuYaps = QtWidgets.QMenu(self.menubar)
        self.menuYaps.setObjectName("menuYaps")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpenCatalog = QtWidgets.QAction(MainWindow)
        self.actionOpenCatalog.setObjectName("actionOpenCatalog")
        self.menuYaps.addAction(self.actionOpenCatalog)
        self.menubar.addAction(self.menuYaps.menuAction())

        self.actionOpenCatalog.triggered.connect(self.openCatalog)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pictureEmptyLabel.setText(_translate("MainWindow", "No pictures to show"))
        self.findDuplicatesButton.setText(_translate("MainWindow", "Find duplicates"))
        self.menuYaps.setTitle(_translate("MainWindow", "Yaps"))
        self.actionOpenCatalog.setText(_translate("MainWindow", "Open catalog"))

    def openCatalog(self):
        self.yaps.setDirectory(self.openDirectoryDialog())
        self.yaps.preparePictureList()
        self.showPictures()

    def openDirectoryDialog(self):
        return str(QtWidgets.QFileDialog.getExistingDirectory(None, "Select Directory"))

    def showPictures(self):
        _translate = QtCore.QCoreApplication.translate
        self.pictureEmptyLabel.setText(_translate("MainWindow", "Powinno się załadować :p"))
        self.pictureLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pictureLabel.setObjectName("pictureLabel")
        print("ładujemy")
        pic_print = ''
        i = 1
        for pic in self.yaps.pictures:
            pic_print += pic.filename + '\n'
            self.picture = QtWidgets.QLabel(self.gridLayoutWidget)
            self.picture.setObjectName("picture_" + pic.filename)
            self.picture.setPixmap(QtGui.QPixmap(self.yaps.directory + "/" + pic.filename))
            self.picturesGrid.addWidget(self.picture, i, 1, 1, 1)
            i += 1

        self.pictureLabel.setText(pic_print)
        self.picturesGrid.addWidget(self.pictureLabel, 1, 0, 1, 1)



def run(yaps):
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(yaps)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    run(None)
