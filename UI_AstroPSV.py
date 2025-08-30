# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledGMadEl.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_10.addWidget(self.label_10, 0, 2, 1, 1)

        self.lineEdit_7 = QLineEdit(self.groupBox)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_10.addWidget(self.lineEdit_7, 0, 3, 1, 1)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_10.addWidget(self.checkBox, 0, 4, 1, 1)

        self.lineEdit_6 = QLineEdit(self.groupBox)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 0))

        self.gridLayout_10.addWidget(self.lineEdit_6, 0, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_10.addWidget(self.label_8, 0, 6, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_10.addWidget(self.label_7, 0, 0, 1, 1)

        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(999)

        self.gridLayout_10.addWidget(self.spinBox, 0, 7, 1, 1)

        self.line_5 = QFrame(self.groupBox)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setLineWidth(0)
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_10.addWidget(self.line_5, 0, 5, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_10, 0, 0, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_7.addWidget(self.lineEdit, 1, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.label_2, 0, 2, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_7.addWidget(self.lineEdit_2, 1, 3, 1, 1)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_7.addWidget(self.comboBox, 1, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.label_3, 0, 3, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.label_9, 0, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_7.addWidget(self.comboBox_2, 1, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_7, 2, 0, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_9.addWidget(self.label_5, 0, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_9.addWidget(self.lineEdit_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_9.addWidget(self.label_4, 0, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_9.addWidget(self.lineEdit_4, 1, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_9.addWidget(self.label_6, 0, 2, 1, 1)

        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_9.addWidget(self.lineEdit_5, 1, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_9, 4, 0, 1, 1)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line, 3, 0, 1, 1)

        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_2, 1, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.groupBox)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_3.addWidget(self.pushButton_5)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_2 = QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableWidget = QTableWidget(self.tab_3)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setRowCount(1)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_3 = QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.textBrowser = QTextBrowser(self.tab_4)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout_3.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_5 = QGridLayout(self.tab_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.textBrowser_2 = QTextBrowser(self.tab_5)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.gridLayout_5.addWidget(self.textBrowser_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")

        self.verticalLayout_4.addWidget(self.tabWidget)


        self.verticalLayout.addLayout(self.verticalLayout_4)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 43))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\uae30\ubcf8 \uad00\uce21 \uc815\ubcf4 \uc785\ub825", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\uad00\uce21\uc9c0 \ucf54\ub4dc", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(\uc608) P62", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\ucf54\ub4dc \ubbf8\ubc1c\uae09", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(\uc608) P. Byeongmin", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\ub370\uc774\ud130 \uac1c\uc218", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\uad00\uce21\uc790 \uc774\ub984", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(\uc608) 0.43", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ub9dd\uc6d0\uacbd \uad6c\uacbd(m)", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"CCD", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"CMOS", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\uce74\uba54\ub77c \uc885\ub958", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\ub9dd\uc6d0\uacbd \uc885\ub958(\uc608. CDK, RC, reflector, Schmidt-Cassegrain)", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\ud544\ud130", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"U", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"B", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"G", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"V", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"R", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"I", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\uacbd\ub3c4", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(\uc608) 36 00 50.4 N", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\uc704\ub3c4", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(\uc608) 127 02 09.5 E", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\uace0\ub3c4(m)", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(\uc608) 67", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\uc124\uba85\uc11c", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PSV \ucd9c\ub825", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PSV \uc800\uc7a5", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PSV \ubd88\ub7ec\uc624\uae30", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\uc18c\ud589\uc131 \ubc88\ud638", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\ucd2c\uc601 \uc911\uc559 \uc2dc\uac01(UTC)", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\uc801\uacbd", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\uc801\uc704", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\uac89\ubcf4\uae30 \ub4f1\uae09", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\ub370\uc774\ud130 \uc785\ub825", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"PSV \ucd9c\ub825", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\ub85c\uadf8", None))
    # retranslateUi

