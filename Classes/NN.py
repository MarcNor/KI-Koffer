# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import Classes.images_rc

class Ui_NN_Form(object):
    def setupUi(self, NN_Form):
        if not NN_Form.objectName():
            NN_Form.setObjectName(u"NN_Form")
        NN_Form.resize(980, 790)
        self.gridLayout = QGridLayout(NN_Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(NN_Form)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setPointSize(15)
        self.tabWidget.setFont(font)
        self.NN_A = QWidget()
        self.NN_A.setObjectName(u"NN_A")
        self.verticalLayoutWidget = QWidget(self.NN_A)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(60, 120, 341, 381))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.NN_A_input_Camera_textBrowser = QLabel(self.verticalLayoutWidget)
        self.NN_A_input_Camera_textBrowser.setObjectName(u"NN_A_input_Camera_textBrowser")
        self.verticalLayout.addWidget(self.NN_A_input_Camera_textBrowser)

        self.verticalLayoutWidget_2 = QWidget(self.NN_A)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(520, 120, 321, 291))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.NN_A_Ergebnis_textBrowser = QTextBrowser(self.verticalLayoutWidget_2)
        self.NN_A_Ergebnis_textBrowser.setObjectName(u"NN_A_Ergebnis_textBrowser")
        font1 = QFont()
        font1.setPointSize(18)
        self.NN_A_Ergebnis_textBrowser.setFont(font1)

        self.verticalLayout_2.addWidget(self.NN_A_Ergebnis_textBrowser)

        self.NN_A_Submit_pushButton = QPushButton(self.NN_A)
        self.NN_A_Submit_pushButton.setObjectName(u"NN_A_Submit_pushButton")
        self.NN_A_Submit_pushButton.setGeometry(QRect(150, 570, 171, 32))
        self.NN_A_Submit_pushButton.setFont(font)
        self.label = QLabel(self.NN_A)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 70, 339, 22))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(1, 25, 147);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.NN_A)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(510, 70, 319, 22))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(1, 25, 147);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.NN_A, "")
        self.NN_NN = QWidget()
        self.NN_NN.setObjectName(u"NN_NN")
        self.verticalLayoutWidget_3 = QWidget(self.NN_NN)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(100, 30, 251, 251))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(1, 25, 147);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.verticalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.NN_NN_Input_Camera_textBrowser = QTextBrowser(self.verticalLayoutWidget_3)
        self.NN_NN_Input_Camera_textBrowser.setObjectName(u"NN_NN_Input_Camera_textBrowser")
        self.NN_NN_Input_Camera_textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NN_NN_Input_Camera_textBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NN_NN_Input_Camera_textBrowser.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.verticalLayout_3.addWidget(self.NN_NN_Input_Camera_textBrowser)

        self.verticalLayoutWidget_4 = QWidget(self.NN_NN)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(620, 30, 231, 191))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.verticalLayoutWidget_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(1, 25, 147);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.verticalSpacer = QSpacerItem(40, 80, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.NN_NN_Ergebnis_textBrowser = QTextBrowser(self.verticalLayoutWidget_4)
        self.NN_NN_Ergebnis_textBrowser.setObjectName(u"NN_NN_Ergebnis_textBrowser")
        self.NN_NN_Ergebnis_textBrowser.setFont(font1)
        self.NN_NN_Ergebnis_textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NN_NN_Ergebnis_textBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_4.addWidget(self.NN_NN_Ergebnis_textBrowser)

        self.NN_NN_Ergebnis_textBrowser_2 = QTextBrowser(self.NN_NN)
        self.NN_NN_Ergebnis_textBrowser_2.setObjectName(u"NN_NN_Ergebnis_textBrowser_2")
        self.NN_NN_Ergebnis_textBrowser_2.setGeometry(QRect(100, 380, 780, 350))
        self.NN_NN_Ergebnis_textBrowser_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NN_NN_Ergebnis_textBrowser_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NN_NN_Ergebnis_textBrowser_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tabWidget.addTab(self.NN_NN, "")
        self.NN_M = QWidget()
        self.NN_M.setObjectName(u"NN_M")
        self.verticalLayoutWidget_5 = QWidget(self.NN_M)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(160, 80, 31, 121))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.verticalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout_5.addWidget(self.label_5)

        self.label_6 = QLabel(self.verticalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_5.addWidget(self.label_6)

        self.label_7 = QLabel(self.verticalLayoutWidget_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout_5.addWidget(self.label_7)

        self.verticalLayoutWidget_6 = QWidget(self.NN_M)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(330, 80, 31, 121))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.verticalLayoutWidget_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_6.addWidget(self.label_8)

        self.label_9 = QLabel(self.verticalLayoutWidget_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout_6.addWidget(self.label_9)

        self.label_10 = QLabel(self.verticalLayoutWidget_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.verticalLayout_6.addWidget(self.label_10)

        self.verticalLayoutWidget_7 = QWidget(self.NN_M)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(190, 80, 76, 121))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.NN_M_x1_plainTextEdit = QPlainTextEdit(self.verticalLayoutWidget_7)
        self.NN_M_x1_plainTextEdit.setObjectName(u"NN_M_x1_plainTextEdit")
        self.NN_M_x1_plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NN_M_x1_plainTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_7.addWidget(self.NN_M_x1_plainTextEdit)

        self.NN_M_x2_plainTextEdit = QPlainTextEdit(self.verticalLayoutWidget_7)
        self.NN_M_x2_plainTextEdit.setObjectName(u"NN_M_x2_plainTextEdit")
        self.NN_M_x2_plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NN_M_x2_plainTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_7.addWidget(self.NN_M_x2_plainTextEdit)

        self.NN_M_x3_plainTextEdit = QPlainTextEdit(self.verticalLayoutWidget_7)
        self.NN_M_x3_plainTextEdit.setObjectName(u"NN_M_x3_plainTextEdit")
        self.NN_M_x3_plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NN_M_x3_plainTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_7.addWidget(self.NN_M_x3_plainTextEdit)

        self.verticalLayoutWidget_9 = QWidget(self.NN_M)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(560, 80, 76, 41))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.NN_M_HwBx_plainTextEdit = QPlainTextEdit(self.verticalLayoutWidget_9)
        self.NN_M_HwBx_plainTextEdit.setObjectName(u"NN_M_HwBx_plainTextEdit")
        self.NN_M_HwBx_plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NN_M_HwBx_plainTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_9.addWidget(self.NN_M_HwBx_plainTextEdit)

        self.verticalLayoutWidget_10 = QWidget(self.NN_M)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(500, 80, 61, 41))
        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.verticalLayoutWidget_10)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.verticalLayout_10.addWidget(self.label_11)

        self.NN_M_Ergebnis_textBrowser = QTextBrowser(self.NN_M)
        self.NN_M_Ergebnis_textBrowser.setObjectName(u"NN_M_Ergebnis_textBrowser")
        self.NN_M_Ergebnis_textBrowser.setGeometry(QRect(110, 350, 780, 350))
        self.NN_M_Ergebnis_textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NN_M_Ergebnis_textBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NN_M_Ergebnis_textBrowser.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.NN_M_Submit_pushButton = QPushButton(self.NN_M)
        self.NN_M_Submit_pushButton.setObjectName(u"NN_M_Submit_pushButton")
        self.NN_M_Submit_pushButton.setGeometry(QRect(510, 230, 112, 32))
        self.NN_M_Submit_pushButton.setFont(font)
        self.verticalLayoutWidget_8 = QWidget(self.NN_M)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(360, 80, 76, 121))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.NN_M_a1_plainTextEdit = QPlainTextEdit(self.verticalLayoutWidget_8)
        self.NN_M_a1_plainTextEdit.setObjectName(u"NN_M_a1_plainTextEdit")
        self.NN_M_a1_plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NN_M_a1_plainTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_8.addWidget(self.NN_M_a1_plainTextEdit)

        self.NN_M_a2_plainTextEdit = QPlainTextEdit(self.verticalLayoutWidget_8)
        self.NN_M_a2_plainTextEdit.setObjectName(u"NN_M_a2_plainTextEdit")
        self.NN_M_a2_plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NN_M_a2_plainTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_8.addWidget(self.NN_M_a2_plainTextEdit)

        self.NN_M_a3_plainTextEdit = QPlainTextEdit(self.verticalLayoutWidget_8)
        self.NN_M_a3_plainTextEdit.setObjectName(u"NN_M_a3_plainTextEdit")
        self.NN_M_a3_plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NN_M_a3_plainTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_8.addWidget(self.NN_M_a3_plainTextEdit)

        self.label_12 = QLabel(self.NN_M)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(160, 30, 471, 16))
        self.label_12.setStyleSheet(u"color: rgb(1, 25, 147);\n"
"font: 18pt \".AppleSystemUIFont\";")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.NN_M, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(NN_Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(NN_Form)
    # setupUi

    def retranslateUi(self, NN_Form):
        NN_Form.setWindowTitle(QCoreApplication.translate("NN_Form", u"Neural Network", None))

        pixmap = QPixmap("./Resources/incognito.png")
        self.NN_A_input_Camera_textBrowser.setPixmap(pixmap)
        self.NN_A_input_Camera_textBrowser.show()
        self.NN_A_Submit_pushButton.setText(QCoreApplication.translate("NN_Form", u"Los!", None))

        self.NN_A_Ergebnis_textBrowser.setHtml(QCoreApplication.translate("NN_Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:13pt;\"><br /></p></body></html>", None))
        self.NN_A_Submit_pushButton.setText(QCoreApplication.translate("NN_Form", u"Los!", None))
        self.label.setText(QCoreApplication.translate("NN_Form", u"Schau in die Kamera...", None))
        self.label_2.setText(QCoreApplication.translate("NN_Form", u"Ergebnis der Analyse", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.NN_A), QCoreApplication.translate("NN_Form", u"Analyse", None))
        self.label_3.setText(QCoreApplication.translate("NN_Form", u"Schau in die Kamera...", None))
        self.NN_NN_Input_Camera_textBrowser.setHtml(QCoreApplication.translate("NN_Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/incognito1.png\" /></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("NN_Form", u"Ergebnis der Analyse:", None))
        self.NN_NN_Ergebnis_textBrowser.setHtml(QCoreApplication.translate("NN_Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:13pt;\"><br /></p></body></html>", None))
        self.NN_NN_Ergebnis_textBrowser_2.setHtml(QCoreApplication.translate("NN_Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/NN3.png\" /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.NN_NN), QCoreApplication.translate("NN_Form", u"Neural Network", None))
        self.label_5.setText(QCoreApplication.translate("NN_Form", u" x1", None))
        self.label_6.setText(QCoreApplication.translate("NN_Form", u" x2", None))
        self.label_7.setText(QCoreApplication.translate("NN_Form", u" x3", None))
        self.label_8.setText(QCoreApplication.translate("NN_Form", u" a1", None))
        self.label_9.setText(QCoreApplication.translate("NN_Form", u" a2", None))
        self.label_10.setText(QCoreApplication.translate("NN_Form", u" a3", None))
        self.label_11.setText(QCoreApplication.translate("NN_Form", u" hw,b(x) ", None))
        self.NN_M_Ergebnis_textBrowser.setHtml(QCoreApplication.translate("NN_Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/NN3.png\" /></p></body></html>", None))
        self.NN_M_Submit_pushButton.setText(QCoreApplication.translate("NN_Form", u"Los!", None))
        self.label_12.setText(QCoreApplication.translate("NN_Form", u"Gib die Parameter f\u00fcr Neuronale Netz ein:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.NN_M), QCoreApplication.translate("NN_Form", u"Math", None))
    # retranslateUi

