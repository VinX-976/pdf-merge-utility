# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(439, 335)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 421, 281))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listWidget = QListWidget(self.widget)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout.addWidget(self.listWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.addButton = QPushButton(self.widget)
        self.addButton.setObjectName(u"addButton")

        self.verticalLayout.addWidget(self.addButton)

        self.moveUpButton = QPushButton(self.widget)
        self.moveUpButton.setObjectName(u"moveUpButton")

        self.verticalLayout.addWidget(self.moveUpButton)

        self.moveDownButton = QPushButton(self.widget)
        self.moveDownButton.setObjectName(u"moveDownButton")

        self.verticalLayout.addWidget(self.moveDownButton)

        self.removeButton = QPushButton(self.widget)
        self.removeButton.setObjectName(u"removeButton")

        self.verticalLayout.addWidget(self.removeButton)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.outputButton = QPushButton(self.widget)
        self.outputButton.setObjectName(u"outputButton")

        self.horizontalLayout_2.addWidget(self.outputButton)

        self.outputLabel = QLabel(self.widget)
        self.outputLabel.setObjectName(u"outputLabel")

        self.horizontalLayout_2.addWidget(self.outputLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.mergeButton = QPushButton(self.widget)
        self.mergeButton.setObjectName(u"mergeButton")

        self.verticalLayout_2.addWidget(self.mergeButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 439, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"Add PDF files", None))
        self.moveUpButton.setText(QCoreApplication.translate("MainWindow", u"Move UP", None))
        self.moveDownButton.setText(QCoreApplication.translate("MainWindow", u"Move DOWN", None))
        self.removeButton.setText(QCoreApplication.translate("MainWindow", u"Remove file", None))
        self.outputButton.setText(QCoreApplication.translate("MainWindow", u"Chose ouput file", None))
        self.outputLabel.setText(QCoreApplication.translate("MainWindow", u"File name...", None))
        self.mergeButton.setText(QCoreApplication.translate("MainWindow", u"Merge", None))
    # retranslateUi

