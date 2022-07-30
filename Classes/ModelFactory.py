from Classes import SVM
from Classes import neural_net
from Interfaces import IModel
import pickle
from Classes import decision_tree


# Diese Klasse entkoppelt das Laden der Modelle und den Controller. Damit kann sich jeder selber darum kümmern, dass
# seine Modelle richtig geladen werden. Die Factory sorgt auch dafür, dass immer ein gültiges Modell zurückgegeben wird,
# damit das Programm nicht unerwartet abstürzt. Wenn das Laden des Modells fehlschlägt oder ein falscher Parameter
# übergeben wird, wird eine Instanz von der IModel-Klasse zurückgegeben.
class ModelFactory:
    # Die Methode muss von dem Controller aufgerufen werden und der Parameter model_type muss ein String Literal sein.
    # Wenn der übergebene String zu einem der bekannten Modelle passt, wird das Modell geladen und an dem Controller
    # zurückgegeben. Bei einer Exception oder unbekannten String Literal wird das IModel zurückgegeben.
    @staticmethod
    def load_model(model_type):
        try:
            if model_type == 'svm':
                return SVM.SupportVectorMachine()

            if model_type == 'neural_network':
                return neural_net.NeuralNetwork()

            if model_type == 'decision_tree':
                return decision_tree.DecisionTree()

            return IModel.IModel()
        except Exception as e:
            print("Could not load model!")
            print("Error Message:", e)
            return IModel.IModel()
