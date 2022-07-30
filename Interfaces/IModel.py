import abc


class IModel(abc.ABC):
    # Diese Methode wird von dem Controller aufgerufen, wenn das KI-Modell trainiert werden muss. Wenn es möglich
    # und von dem Benutzer gewollt ist, kann der Fortschritt des Trainings Schritt für Schritt nachverfolgt werden. Wenn
    # der Parameter den show_training_steps den Wert True beinhaltet, kann der Trainingsfortschritt nachverfolgt werden.
    # Wenn dies gewünscht sein sollte, muss diese Methode mehrmals mit den gleichen Parametern aufgerufen werden. Diese
    # Methode gibt keinen Wert zurück.
    @abc.abstractmethod
    def train(self, show_training_steps=False):
        print("Fit method not implemented!")

    # Diese Methode wird von dem Controller aufgerufen, wenn das Modell visuell dargestellt werden soll. Der Controller
    # übergibt der Methode eine Axis von einer Matplotlib Figure, in der die Instanz des Modells das Modell grafisch
    # darstellen kann. Die Methode gibt keinen Wert zurück.
    @abc.abstractmethod
    def plot(self, axis):
        print("Plot method is not implemented!")

    # Diese Methode wird von dem Controller aufgerufen, wenn der Benutzer eigene Daten über die GUI eingibt und dessen
    # Ergebnis sehen möchten. Wenn das Modell es unterstützt, kann das Ergebnis auch in dem Graphen angezeigt werden.
    # Damit der Graph nicht mit Vorhersagen überflutet wird, sollte die Methode aufgerufen werden, nach dem die
    # plot-Methode aufgerufen wurde, falls die Vorhersagen angezeigt werden soll.
    @abc.abstractmethod
    def predict(self, features, axis=None):
        print("Predict method not implemented!")

    @abc.abstractmethod
    def get_type(self):
        return "IModel"
