# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'About.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import Classes.images_rc

class Ui_About_Form(object):
    def setupUi(self, About_Form):
        if not About_Form.objectName():
            About_Form.setObjectName(u"About_Form")
        About_Form.resize(595, 496)
        self.About_pushButton = QPushButton(About_Form)
        self.About_pushButton.setObjectName(u"About_pushButton")
        self.About_pushButton.setGeometry(QRect(250, 430, 112, 32))
        self.textBrowser = QTextBrowser(About_Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(0, 0, 591, 421))
        self.textBrowser.setAutoFillBackground(True)
        self.textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.retranslateUi(About_Form)
        self.About_pushButton.clicked.connect(About_Form.close)

        QMetaObject.connectSlotsByName(About_Form)
    # setupUi

    def retranslateUi(self, About_Form):
        About_Form.setWindowTitle(QCoreApplication.translate("About_Form", u"About", None))
        self.About_pushButton.setText(QCoreApplication.translate("About_Form", u"OK", None))
        self.textBrowser.setHtml(QCoreApplication.translate("About_Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%;\"><img src=\":/newPrefix/NAK1.png\" /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margi"
                        "n-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%;\"><span style=\" font-family:'Arial'; font-size:14pt; font-weight:600; color:#000000; background-color:transparent;\">Masterprojekt</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%;\"><a name=\"docs-internal-guid-7505d79a-7fff-a996-b731-04aa7445589e\"></a><span style=\" font-family:'Trebuchet MS'; font-size:14pt; color:#000000; background-color:transparent;\">E</span><span style=\" font-family:'Trebuchet MS'; font-size:14pt; color:#000000; background-color:transparent;\">ntwicklung eines portablen KI-Koffers</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:"
                        "0px;\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#000000;\">Team:<br /></span><span style=\" font-size:14pt; color:#000000;\"><br />    </span><a name=\"docs-internal-guid-c850c127-7fff-a518-1398-972c0514618d\"></a><span style=\" font-family:'Arial'; font-size:14pt; font-style:italic; color:#000000; background-color:transparent;\">A</span><span style=\" font-family:'Arial'; font-size:14pt; font-style:italic; color:#000000; background-color:transparent;\">ndr\u00e9a Narja Heberling</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%;\"><span style=\" font-family:'Arial'; font-size:14pt; font-style:italic; color:#000000; background-color:transparent;\">    Anja B\u00fchler                   </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%;\""
                        "><span style=\" font-family:'Arial'; font-size:14pt; font-style:italic; color:#000000; background-color:transparent;\">    Marc Normann              </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:120%;\"><span style=\" font-family:'Arial'; font-size:14pt; font-style:italic; color:#000000; background-color:transparent;\">    Steven Bley                  </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

