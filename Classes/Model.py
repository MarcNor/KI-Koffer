# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Model.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ModelForm(object):
    def setupUi(self, ModelForm):
        if not ModelForm.objectName():
            ModelForm.setObjectName(u"ModelForm")
        ModelForm.resize(980, 790)
        self.M_ZNT_pushButton = QPushButton(ModelForm)
        self.M_ZNT_pushButton.setObjectName(u"M_ZNT_pushButton")
        self.M_ZNT_pushButton.setGeometry(QRect(40, 170, 240, 40))
        font = QFont()
        font.setPointSize(15)
        self.M_ZNT_pushButton.setFont(font)
        self.M_MVT_pushButton = QPushButton(ModelForm)
        self.M_MVT_pushButton.setObjectName(u"M_MVT_pushButton")
        self.M_MVT_pushButton.setGeometry(QRect(290, 170, 240, 40))
        self.M_MVT_pushButton.setFont(font)
        self.M_V_pushButton = QPushButton(ModelForm)
        self.M_V_pushButton.setObjectName(u"M_V_pushButton")
        self.M_V_pushButton.setGeometry(QRect(40, 380, 120, 40))
        self.M_V_pushButton.setFont(font)
        self.horizontalLayoutWidget = QWidget(ModelForm)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(50, 310, 351, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.M_EF_plainTextEdit = QPlainTextEdit(self.horizontalLayoutWidget)
        self.M_EF_plainTextEdit.setObjectName(u"M_EF_plainTextEdit")
        self.M_EF_plainTextEdit.setFont(font)
        self.M_EF_plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout.addWidget(self.M_EF_plainTextEdit)

        self.M_ZF_plainTextEdit = QPlainTextEdit(self.horizontalLayoutWidget)
        self.M_ZF_plainTextEdit.setObjectName(u"M_ZF_plainTextEdit")
        self.M_ZF_plainTextEdit.setFont(font)
        self.M_ZF_plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout.addWidget(self.M_ZF_plainTextEdit)

        self.label_2 = QLabel(ModelForm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 280, 58, 16))
        self.label_2.setFont(font)
        self.M_FC_widget = QWidget(ModelForm)
        self.M_FC_widget.setObjectName(u"M_FC_widget")
        self.M_FC_widget.setGeometry(QRect(550, 120, 410, 600))
        self.M_FC_widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayoutWidget = QWidget(ModelForm)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(50, 520, 341, 71))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.M_V_plainTextEdit = QPlainTextEdit(self.verticalLayoutWidget)
        self.M_V_plainTextEdit.setObjectName(u"M_V_plainTextEdit")
        self.M_V_plainTextEdit.setFont(font)
        self.M_V_plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.M_V_plainTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.M_V_plainTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.M_V_plainTextEdit)

        self.label_3 = QLabel(ModelForm)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(547, 80, 411, 20))
        font1 = QFont()
        font1.setPointSize(18)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(1, 25, 147);")

        self.retranslateUi(ModelForm)

        QMetaObject.connectSlotsByName(ModelForm)
    # setupUi

    def retranslateUi(self, ModelForm):
        ModelForm.setWindowTitle(QCoreApplication.translate("ModelForm", u"Model", None))
        self.M_ZNT_pushButton.setText(QCoreApplication.translate("ModelForm", u"Zeige n\u00e4chste Trainingsschritte", None))
        self.M_MVT_pushButton.setText(QCoreApplication.translate("ModelForm", u"Modell vollst\u00e4ndig trainieren", None))
        self.M_V_pushButton.setText(QCoreApplication.translate("ModelForm", u"Vorhersage", None))
        self.M_EF_plainTextEdit.setPlainText(QCoreApplication.translate("ModelForm", u"(Erste Feature)", None))
        self.M_ZF_plainTextEdit.setPlainText(QCoreApplication.translate("ModelForm", u"(Zweite Feature)", None))
        self.label_2.setText(QCoreApplication.translate("ModelForm", u"Eingabe:", None))
        self.label.setText(QCoreApplication.translate("ModelForm", u"Vorhersage:", None))
        self.M_V_plainTextEdit.setPlainText(QCoreApplication.translate("ModelForm", u"(Klasse XY)", None))
        self.label_3.setText(QCoreApplication.translate("ModelForm", u"Figure / Canvas:", None))
    # retranslateUi

