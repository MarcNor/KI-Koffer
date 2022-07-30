from Classes.MainApplication import Ui_MainWindow
from PySide2 import QtCore, QtGui, QtWidgets
from cv2 import *
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2 as cv
from Classes.NN import *
from Classes.DT import *
from Classes.About import *
from Classes.Model import *
import sys
from Interfaces import IGUI


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """docstring for ClassName"""

    def __init__(self, controller):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.controller = controller

        self.radioButton_NN.clicked.connect(self.NN)
        self.radioButton_DT.clicked.connect(self.DT)
        self.actionAbout.triggered.connect(self.About)
        self.actionModelle.triggered.connect(self.Model)

    def NN(self):
        self.controller.load_model('neural_network')
        self.window = choiceNN(self.controller)
        self.window.show()

    def DT(self):
        self.controller.load_model('decision_tree')
        self.window = choiceDT(self.controller)
        self.window.show()

    def About(self):
        self.window = choiceAbout()
        self.window.show()

    def Model(self):
     	self.window =  choiceModel()
     	self.window.show()


# Call the form "NN", which stands for "Neural Network", when the radioButton_NN is clicked.
class choiceNN(QtWidgets.QWidget, Ui_NN_Form):
    """docstring for ClassName"""

    def __init__(self, controller):
        super(choiceNN, self).__init__()
        self.setupUi(self)
        self.controller = controller

        # Get all input values from user at the tab "Analyse" and save them in variables
        def inputNNA(self):

            camera = VideoCapture(0)
            retval, image = camera.read()
            camera.release()

            height, width, channel = image.shape
            bytesPerLine = 3 * width
            pixmap = QPixmap(QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888))

            image = cv.resize(image, (100,100))
            image = (np.expand_dims(image,0))
            image = image / 255
            image = image.reshape(1, -1).T

            result = self.controller.predict(image)

            self.NN_A_Ergebnis_textBrowser.setPlainText(result)
            self.NN_A_input_Camera_textBrowser.setPixmap(pixmap.scaled(250, 250, QtCore.Qt.KeepAspectRatio))
            self.NN_A_input_Camera_textBrowser.show()

        # Submit the input from the camera to be evaluated by the Model Neural Network
        self.NN_A_Submit_pushButton.clicked.connect(lambda: inputNNA(self))

        # Get all input values from user at the tab "Math" and save them in variables
        def inputNNM(self):
            self.x1 = self.NN_M_x1_plainTextEdit.toPlainText()
            self.x2 = self.NN_M_x2_plainTextEdit.toPlainText()
            self.x3 = self.NN_M_x1_plainTextEdit.toPlainText()
            self.a1 = self.NN_M_a1_plainTextEdit.toPlainText()
            self.a2 = self.NN_M_a2_plainTextEdit.toPlainText()
            self.a3 = self.NN_M_a1_plainTextEdit.toPlainText()
            self.HwBx = self.NN_M_HwBx_plainTextEdit.toPlainText()
            print(self.x1, self.x2, self.x3, self.a1, self.a2, self.a3, self.HwBx)

        # Submit the input from the user to be evaluated by the Model Neural Network
        self.NN_M_Submit_pushButton.clicked.connect(lambda: inputNNM(self))


# Call the form "DT", which stands for "Decision Tree", when the radioButton_DT is clicked.
class choiceDT(QtWidgets.QWidget, Ui_DT_Form):
    """docstring for ClassName"""

    def __init__(self, controller):
        super(choiceDT, self).__init__()
        self.setupUi(self)
        self.controller = controller

        # Get all input values from user at the tab "Analyse" and save them in variables
        def inputDTA(self):
            self.geschlecht = self.DT_A_Geschlecht_comboBox.currentText()
            self.DT_DT_Geschlecht_plainTextEdit.setPlainText(self.geschlecht)
            self.alter = self.DT_A_Alter_plainTextEdit.toPlainText()
            self.DT_DT_Alter_plainTextEdit.setPlainText(self.alter)
            self.monat = self.DT_A_Monat_comboBox.currentText()
            self.DT_DT_Monat_plainTextEdit.setPlainText(self.monat)
            self.uhrzeit = self.DT_A_Uhrzeit_timeEdit.time()
            self.uhrzeit1 = self.uhrzeit.toString("HH:mm")
            self.DT_DT_Uhrzeit_plainTextEdit.setPlainText(self.uhrzeit1)

            input_data = [self.geschlecht, self.alter, self.monat, self.uhrzeit1]

            result = self.controller.predict(input_data)

            self.DT_A_Ergebnis_textBrowser.setPlainText(result)

        # Submit the input from the user to be evaluated by the Model Decision Tree
        self.DT_A_pushButton.clicked.connect(lambda: inputDTA(self))


# Call the form "About", which stands for "About us", when the manu.actionAbout is clicked.
class choiceAbout(QtWidgets.QWidget, Ui_About_Form):
    """docstring for ClassName"""

    def __init__(self):
        super(choiceAbout, self).__init__()
        self.setupUi(self)


# Call the form "Model", when the manu.actionModelle is clicked.
class choiceModel (QtWidgets.QWidget, Ui_ModelForm):
    """docstring for ClassName"""
    def __init__(self):
        super(choiceModel, self).__init__()
        self.setupUi(self)

        # Get all input values from user at the Model and save them in variables
        def inputModel(self):
            self.M_EF = self.M_EF_plainTextEdit.toPlainText()
            self.M_ZF = self.M_ZF_plainTextEdit.toPlainText()
            # self.M_V = self.M_V_plainTextEdit.setPlainText(functionVorhersage)
            print(self.M_EF, self.M_ZF)

        # Submit the input from the user to be evaluated by the Model
        # self.M_ENT_pushButton.clicked.connect(function_M_ENT)
        # self.M_ZNT_pushButton.clicked.connect(function_M_ZNT)
        self.M_V_pushButton.clicked.connect(lambda: inputModel(self))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())


class GUI(IGUI.IGUI):
    def __init__(self, controller):
        self.controller = controller
        self.app = QtWidgets.QApplication()
        self.ui = MainWindow(self.controller)

    def start(self):
        self.ui.show()
        self.app.exec_()
