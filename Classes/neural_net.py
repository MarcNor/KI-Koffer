from Interfaces import IModel
import tensorflow.keras as keras

class NeuralNetwork(IModel.IModel):
    def __init__(self):
        self.model_type = 'neural_network'

        self.model = self.loadNeuralNetwork()

    def get_type(self):
        return "Neural Network"

    def loadNeuralNetwork(self):        
        model = keras.models.load_model('./Resources/')
        return model

    def plot(self):
        return null

    def train(self):
        return null

    def predict(self, input_data, axis):
        prediction = self.model.predict(input_data.reshape(1, 30000))
        if prediction[0][0] >= 0.5:
            return "Maske erkannt."
        elif prediction[0][0] < 0.5:
            return "Keine Maske erkannt."