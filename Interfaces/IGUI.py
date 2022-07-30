import abc


class IGUI(abc.ABC):
    # Diese Methode wird von dem Controller aufgerufen, wenn die Anwendung bereit ist und die GUI für den Benutzer
    # gestartet werden kann. Die Methode benötigt keine Parameter und gibt auch keinen Wert zurück.
    @abc.abstractmethod
    def start(self):
        print("Start method is not implemented yet.")
