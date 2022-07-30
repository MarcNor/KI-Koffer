# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DT.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import Classes.images_rc

class Ui_DT_Form(object):
    def setupUi(self, DT_Form):
        if not DT_Form.objectName():
            DT_Form.setObjectName(u"DT_Form")
        DT_Form.resize(980, 790)
        self.gridLayout = QGridLayout(DT_Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(DT_Form)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setPointSize(15)
        self.tabWidget.setFont(font)
        self.DT_A = QWidget()
        self.DT_A.setObjectName(u"DT_A")
        self.label_5 = QLabel(self.DT_A)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 50, 251, 31))
        font1 = QFont()
        font1.setPointSize(18)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(1, 25, 147);")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.DT_A)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(590, 50, 251, 31))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: rgb(1, 25, 147);")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.DT_A_Ergebnis_textBrowser = QTextBrowser(self.DT_A)
        self.DT_A_Ergebnis_textBrowser.setObjectName(u"DT_A_Ergebnis_textBrowser")
        self.DT_A_Ergebnis_textBrowser.setGeometry(QRect(590, 120, 261, 261))
        self.DT_A_Ergebnis_textBrowser.setFont(font1)
        self.DT_A_Ergebnis_textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.DT_A_Ergebnis_textBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.DT_A_Ergebnis_textBrowser.setReadOnly(True)
        self.DT_A_pushButton = QPushButton(self.DT_A)
        self.DT_A_pushButton.setObjectName(u"DT_A_pushButton")
        self.DT_A_pushButton.setGeometry(QRect(150, 280, 67, 32))
        self.DT_A_pushButton.setFont(font)
        self.formLayoutWidget_3 = QWidget(self.DT_A)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(60, 120, 251, 101))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setVerticalSpacing(0)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.formLayoutWidget_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_18)

        self.DT_A_Geschlecht_comboBox = QComboBox(self.formLayoutWidget_3)
        self.DT_A_Geschlecht_comboBox.addItem("")
        self.DT_A_Geschlecht_comboBox.addItem("")
        self.DT_A_Geschlecht_comboBox.addItem("")
        self.DT_A_Geschlecht_comboBox.setObjectName(u"DT_A_Geschlecht_comboBox")
        self.DT_A_Geschlecht_comboBox.setFont(font)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.DT_A_Geschlecht_comboBox)

        self.label_17 = QLabel(self.formLayoutWidget_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_17)

        self.label_19 = QLabel(self.formLayoutWidget_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.label_19)

        self.DT_A_Monat_comboBox = QComboBox(self.formLayoutWidget_3)
        self.DT_A_Monat_comboBox.addItem("")
        self.DT_A_Monat_comboBox.addItem("")
        self.DT_A_Monat_comboBox.addItem("")
        self.DT_A_Monat_comboBox.addItem("")
        self.DT_A_Monat_comboBox.addItem("")
        self.DT_A_Monat_comboBox.addItem("")
        self.DT_A_Monat_comboBox.addItem("")
        self.DT_A_Monat_comboBox.addItem("")
        self.DT_A_Monat_comboBox.addItem("")
        self.DT_A_Monat_comboBox.addItem("")
        self.DT_A_Monat_comboBox.addItem("")
        self.DT_A_Monat_comboBox.addItem("")
        self.DT_A_Monat_comboBox.setObjectName(u"DT_A_Monat_comboBox")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.DT_A_Monat_comboBox)

        self.DT_A_Uhrzeit_timeEdit = QTimeEdit(self.formLayoutWidget_3)
        self.DT_A_Uhrzeit_timeEdit.setObjectName(u"DT_A_Uhrzeit_timeEdit")
        self.DT_A_Uhrzeit_timeEdit.setMinimumSize(QSize(0, 0))
        self.DT_A_Uhrzeit_timeEdit.setFont(font)
        self.DT_A_Uhrzeit_timeEdit.setLayoutDirection(Qt.LeftToRight)
        self.DT_A_Uhrzeit_timeEdit.setFrame(False)
        self.DT_A_Uhrzeit_timeEdit.setAlignment(Qt.AlignCenter)
        self.DT_A_Uhrzeit_timeEdit.setButtonSymbols(QAbstractSpinBox.PlusMinus)

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.DT_A_Uhrzeit_timeEdit)

        self.label_20 = QLabel(self.formLayoutWidget_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_20)

        self.DT_A_Alter_plainTextEdit = QPlainTextEdit(self.formLayoutWidget_3)
        self.DT_A_Alter_plainTextEdit.setObjectName(u"DT_A_Alter_plainTextEdit")
        self.DT_A_Alter_plainTextEdit.setFont(font)
        self.DT_A_Alter_plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.DT_A_Alter_plainTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.DT_A_Alter_plainTextEdit)

        self.tabWidget.addTab(self.DT_A, "")
        self.DT_DT = QWidget()
        self.DT_DT.setObjectName(u"DT_DT")
        self.label_11 = QLabel(self.DT_DT)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 40, 161, 31))
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"color: rgb(1, 25, 147);")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_12 = QLabel(self.DT_DT)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(250, 40, 311, 31))
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"color: rgb(1, 25, 147);")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.formLayoutWidget_2 = QWidget(self.DT_DT)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(0, 100, 161, 131))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(0)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.DT_DT_Geschlecht_plainTextEdit = QPlainTextEdit(self.formLayoutWidget_2)
        self.DT_DT_Geschlecht_plainTextEdit.setObjectName(u"DT_DT_Geschlecht_plainTextEdit")
        self.DT_DT_Geschlecht_plainTextEdit.setFont(font)
        self.DT_DT_Geschlecht_plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.DT_DT_Geschlecht_plainTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.DT_DT_Geschlecht_plainTextEdit.setReadOnly(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.DT_DT_Geschlecht_plainTextEdit)

        self.DT_DT_Alter_plainTextEdit = QPlainTextEdit(self.formLayoutWidget_2)
        self.DT_DT_Alter_plainTextEdit.setObjectName(u"DT_DT_Alter_plainTextEdit")
        self.DT_DT_Alter_plainTextEdit.setFont(font)
        self.DT_DT_Alter_plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.DT_DT_Alter_plainTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.DT_DT_Alter_plainTextEdit.setReadOnly(True)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.DT_DT_Alter_plainTextEdit)

        self.DT_DT_Monat_plainTextEdit = QPlainTextEdit(self.formLayoutWidget_2)
        self.DT_DT_Monat_plainTextEdit.setObjectName(u"DT_DT_Monat_plainTextEdit")
        self.DT_DT_Monat_plainTextEdit.setFont(font)
        self.DT_DT_Monat_plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.DT_DT_Monat_plainTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.DT_DT_Monat_plainTextEdit.setReadOnly(True)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.DT_DT_Monat_plainTextEdit)

        self.DT_DT_Uhrzeit_plainTextEdit = QPlainTextEdit(self.formLayoutWidget_2)
        self.DT_DT_Uhrzeit_plainTextEdit.setObjectName(u"DT_DT_Uhrzeit_plainTextEdit")
        self.DT_DT_Uhrzeit_plainTextEdit.setFont(font)
        self.DT_DT_Uhrzeit_plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.DT_DT_Uhrzeit_plainTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.DT_DT_Uhrzeit_plainTextEdit.setReadOnly(True)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.DT_DT_Uhrzeit_plainTextEdit)

        self.label_13 = QLabel(self.formLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_13)

        self.label_14 = QLabel(self.formLayoutWidget_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_14)

        self.label_15 = QLabel(self.formLayoutWidget_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_15)

        self.label_16 = QLabel(self.formLayoutWidget_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_16)

        self.DT_DT_Ergebnis_textBrowser = QTextBrowser(self.DT_DT)
        self.DT_DT_Ergebnis_textBrowser.setObjectName(u"DT_DT_Ergebnis_textBrowser")
        self.DT_DT_Ergebnis_textBrowser.setGeometry(QRect(170, 20, 791, 731))
        self.DT_DT_Ergebnis_textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.DT_DT_Ergebnis_textBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.DT_DT_Ergebnis_textBrowser.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.DT_DT_Ergebnis_textBrowser.setTabChangesFocus(False)
        self.tabWidget.addTab(self.DT_DT, "")
        self.label_11.raise_()
        self.formLayoutWidget_2.raise_()
        self.DT_DT_Ergebnis_textBrowser.raise_()
        self.label_12.raise_()

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(DT_Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DT_Form)
    # setupUi

    def retranslateUi(self, DT_Form):
        DT_Form.setWindowTitle(QCoreApplication.translate("DT_Form", u"Decision Tree", None))
        self.label_5.setText(QCoreApplication.translate("DT_Form", u"Input Data:", None))
        self.label_6.setText(QCoreApplication.translate("DT_Form", u"Ergebnis der Analyse", None))
        self.DT_A_Ergebnis_textBrowser.setHtml(QCoreApplication.translate("DT_Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:13pt;\"><br /></p></body></html>", None))
        self.DT_A_pushButton.setText(QCoreApplication.translate("DT_Form", u"Los!", None))
        self.label_18.setText(QCoreApplication.translate("DT_Form", u"Geschlecht", None))
        self.DT_A_Geschlecht_comboBox.setItemText(0, QCoreApplication.translate("DT_Form", u"-", None))
        self.DT_A_Geschlecht_comboBox.setItemText(1, QCoreApplication.translate("DT_Form", u"weiblich", None))
        self.DT_A_Geschlecht_comboBox.setItemText(2, QCoreApplication.translate("DT_Form", u"m\u00e4nnlich", None))

        self.label_17.setText(QCoreApplication.translate("DT_Form", u"Alter", None))
        self.label_19.setText(QCoreApplication.translate("DT_Form", u"Uhrzeit", None))
        self.DT_A_Monat_comboBox.setItemText(0, QCoreApplication.translate("DT_Form", u"-", None))
        self.DT_A_Monat_comboBox.setItemText(1, QCoreApplication.translate("DT_Form", u"Jan", None))
        self.DT_A_Monat_comboBox.setItemText(2, QCoreApplication.translate("DT_Form", u"Feb", None))
        self.DT_A_Monat_comboBox.setItemText(3, QCoreApplication.translate("DT_Form", u"M\u00e4r", None))
        self.DT_A_Monat_comboBox.setItemText(4, QCoreApplication.translate("DT_Form", u"Apr", None))
        self.DT_A_Monat_comboBox.setItemText(5, QCoreApplication.translate("DT_Form", u"Mai", None))
        self.DT_A_Monat_comboBox.setItemText(6, QCoreApplication.translate("DT_Form", u"Jun", None))
        self.DT_A_Monat_comboBox.setItemText(7, QCoreApplication.translate("DT_Form", u"Jul", None))
        self.DT_A_Monat_comboBox.setItemText(8, QCoreApplication.translate("DT_Form", u"Sep", None))
        self.DT_A_Monat_comboBox.setItemText(9, QCoreApplication.translate("DT_Form", u"Okt", None))
        self.DT_A_Monat_comboBox.setItemText(10, QCoreApplication.translate("DT_Form", u"Nov", None))
        self.DT_A_Monat_comboBox.setItemText(11, QCoreApplication.translate("DT_Form", u"Dez", None))

        self.label_20.setText(QCoreApplication.translate("DT_Form", u"Monat", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DT_A), QCoreApplication.translate("DT_Form", u"Analyse", None))
        self.label_11.setText(QCoreApplication.translate("DT_Form", u"Input Data:", None))
        self.label_12.setText(QCoreApplication.translate("DT_Form", u"Ergebnis der Analyse", None))
        self.label_13.setText(QCoreApplication.translate("DT_Form", u"Alter", None))
        self.label_14.setText(QCoreApplication.translate("DT_Form", u"Geschlecht", None))
        self.label_15.setText(QCoreApplication.translate("DT_Form", u"Uhrzeit", None))
        self.label_16.setText(QCoreApplication.translate("DT_Form", u"Monat", None))
        self.DT_DT_Ergebnis_textBrowser.setHtml(QCoreApplication.translate("DT_Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/decision_tree.png\" /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DT_DT), QCoreApplication.translate("DT_Form", u"Decision Tree", None))
    # retranslateUi

