from Interfaces import IController
from Classes import Factory


class Controller(IController.IController):
    def __init__(self):
        print("Initialize controller ...")
        self.model = None
        self.gui = None

    def set_gui(self, gui):
        self.gui = gui

    def start(self):
        self.gui.start()

    def load_model(self, model):
        if self.model is not None:
            del self.model
            self.model = Factory.load_model(model)
        else:
            self.model = Factory.load_model(model)
        # print("Loaded model of type {}.".format(self.model.get_type()))

    def train_model(self, show_training_steps=False):
        if self.model is not None:
            if show_training_steps:
                self.model.train(True)
            else:
                self.model.train(False)
        else:
            print("No model is loaded yet.")

    def plot_model(self, axis):
        if self.model is not None:
            self.model.plot(axis)
        else:
            print("No model is loaded yet.")

    def predict(self, input_data, axis=None):
        result = self.model.predict(input_data, axis)

        return result
