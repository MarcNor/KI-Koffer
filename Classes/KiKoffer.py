from Classes import Controller, Start


class KiKoffer:
    def __init__(self):
        print("Initialize KI-Koffer")
        self.controller = Controller.Controller()
        self.gui = Start.GUI(self.controller)
        self.controller.set_gui(self.gui)

    def start(self):
        self.controller.start()
