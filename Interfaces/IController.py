import abc


class IController(abc.ABC):
    # Methode existiert, damit die zirkuläre Abhängigkeit zwischen dem Controller und der GUI aufgelöst werden kann. Es
    # muss ein gültiges GUI Objekt bei dem Methodenaufruf übergeben werden. Die Methode gibt nichts zurück.
    @abc.abstractmethod
    def set_gui(self, gui):
        pass

    # Methode startet die GUI, wenn alle Objekte instanziiert wurden und alle benötigten Daten vorliegen. Die Methode
    # ruft die "start"-Methode von der GUI auf. Diese Methode gibt keinen Wert zurück und nimmt auch keine Parameter an.
    @abc.abstractmethod
    def start(self):
        print("Start method is not implemented yet.")

    # Diese Methode muss von der GUI aufgerufen werden, wenn der Benutzer ein KI-Modell ausgewählt hat. Es muss das
    # ausgewählte Modell als String übergeben werden. Aktuell kennt die Model-Factory die Werte 'svm',
    # 'neural_network' und 'decision_tree'. Es wird kein Wert zurückgegeben.
    @abc.abstractmethod
    def load_model(self, model):
        print("Load method is not implemented yet.")

    # Diese Methode muss von der GUI aufgerufen werden, wenn das Modell trainiert werden muss. Wenn das Modell es
    # unterstützt, können auch der Trainingsfortschritt angezeigt werden. Dazu muss der Methode der Parameter
    # show_training_steps der Wert True übergeben werden. Falls der Trainingsfortschritt angezeigt werden soll, muss die
    # GUI die Methode möglicherweise mehrmals aufrufen, damit das Modell durch alle Daten trainiert wurde.
    @abc.abstractmethod
    def train_model(self, show_training_steps=False):
        print("Training method is not implemented yet.")

    # Diese Methode muss von der GUI aufgerufen werden, wenn das Modell in der GUI angezeigt oder gezeichnet werden
    # soll. Es muss mindestens die axis der Matplotlib Figure übergeben werden, in der das Modell ihr Graph zeichnen
    # kann.
    @abc.abstractmethod
    def plot_model(self, axis):
        print("Plot method is not implemented yet.")

    # Diese Methode muss von der GUI aufgerufen werden, wenn der Benutzer eine Vorhersage durchführen möchte. Dafür muss
    # der Methode die Eingabedaten in einer Python Liste übergeben werden. Nachdem das KI-Modell die Ausgabe
    # berechnet hat, gibt die Methode einen nummerischen Wert zurück, der das Ergebnis der Vorhersage widerspiegelt.
    # Wenn die Vorhersage auch in der Grafik angezeigt werden soll, muss der Wert von dem Parameter draw_prediction wahr
    # sein.
    @abc.abstractmethod
    def predict(self, input_data, axis=None):
        print("Predict method is not implemented yet.")
