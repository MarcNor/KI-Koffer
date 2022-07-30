from Interfaces import IModel
import pickle
import pandas as pd

class DecisionTree(IModel.IModel):
    def __init__(self):
        self.model_type = 'decision_tree'

        self.model = self.loadTree()

    def get_type(self):
        return "Decision Tree"

    def loadTree(self):        
        with open('./Resources/decision_tree.pkl', 'rb') as file:
            model = pickle.load(file)
        return model

    def plot(self):
        return null

    def train(self):
        return null
    
    def transformInput(self, input_data):
        if input_data[0] == "weiblich":
            gender = 0
        else:
            gender = 1
        age = input_data[1]
        if input_data[2] == "Jan":
            month = 1
        elif input_data[2] == "Feb":
            month = 2
        elif input_data[2] == "Mär":
            month = 3
        elif input_data[2] == "Apr":
            month = 4
        elif input_data[2] == "Mai":
            month = 5
        elif input_data[2] == "Jun":
            month = 6
        elif input_data[2] == "Jul":
            month = 7
        elif input_data[2] == "Aug":
            month = 8
        elif input_data[2] == "Sep":
            month = 9
        elif input_data[2] == "Okt":
            month = 10
        elif input_data[2] == "Nov":
            month = 11
        else:
            month = 12
        hour = input_data[3][:2]
        return pd.DataFrame([[gender,age,month,hour]])

    def predict(self, input_data, axis):
        data = self.transformInput(input_data)
        result = self.model.predict(data)
        if result[0] == 0:
            return "Bier"
        elif result[0] == 1:
            return "Cola"
        elif result[0] == 2:
            return "Salat"
        elif result[0] == 3:
            return "Hackfleisch"
        elif result[0] == 4:
            return "Glühwein"
        elif result[0] == 5:
            return "Lebkuchen"
        elif result[0] == 6:
            return "Zimt"
        elif result[0] == 7:
            return "Taschentücher"
        elif result[0] == 8:
            return "Zitronen"
        elif result[0] == 9:
            return "Tee"
        elif result[0] == 10:
            return "Fruchtgummi"
        elif result[0] == 11:
            return "Kekse"
        elif result[0] == 12:
            return "Reis"
        elif result[0] == 13:
            return "Radler"
        elif result[0] == 14:
            return "Pralinen"
        elif result[0] == 15:
            return "Äpfel"
        elif result[0] == 16:
            return "Whiskey"
        elif result[0] == 17:
            return "Vodka"
        elif result[0] == 18:
            return "Eis"
        elif result[0] == 19:
            return "Limonade"
        elif result[0] == 20:
            return "Chips"
        elif result[0] == 21:
            return "Christstollen"
        elif result[0] == 22:
            return "Brot"
        else:
            return "Hefe"