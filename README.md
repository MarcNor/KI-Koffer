# KI-Koffer

Um Künstliche Intelligenz fachfremden Personen einfach und verständlich zu erklären, soll im Rahmen des Masterprojekts der Nordakademie in Zusammenarbeit mit dem ARIC ein portables Erklärungstool, der KI-Koffer, entstehen. Als Richtwert dient hierbei ein Vortrag von 10 bis 15 Minuten. 

Der KI-Koffer wird hierbei an einem Fallbeispiel einer Ladenbesitzerin aufgebaut. So soll herausgefunden werden, ob und wie viele Leute Maske tragen und zu welchem Einkaufsverhalten die Kunden tendieren. Dies bietet die Möglichkeit, zwei unterschiedliche Methoden der künstlichen Intelligenz zu erklären: Mustererkennung mittels Neuronalem Netz und Mustervorhersage mittels Decision Tree. Als Ziel wird hierfür eine Native App für den Computer angestrebt, die mittels Python aufgebaut ist. 

Die Erklärungen richten sich hierbei an das Prinzip der Schichten. Es soll zunächst für die beiden Methoden eine funktionierende KI aufgebaut werden, an der der Interessent das System ausprobieren kann. Hierbei werden noch keine Erklärungen gezeigt, lediglich das Ergebnis. Anschließend soll der Interessent die Möglichkeit bekommen, sich tiefer in die Materie einzuarbeiten. So wird für das Neuronale Netz vorgesehen, zunächst die Bildverarbeitung und Erkennung von Gesichtsmerkmalen zu zeigen, anschließend in einer nächsten Stufe das Neuronale Netz und die Verarbeitung darin selbst und das Training der Knoten, bevor auf der untersten Schicht die Mathematik erklärt wird. Für den Decision Tree soll anfangs der Pfad angezeigt werden, wonach die Vorhersage getroffen wurde, bevor anschließend gezeigt werden soll, wie ein Decision Tree selbst aufgebaut wird.

Ziel ist es, das System interaktiv zu gestalten und unterschiedliche Sichten und Tiefen der Erklärung zu zulassen, sodass anhand des Interessenten entschieden werden kann, wie tief in die Technik eingestiegen werden soll.

---

##Systemvoraussetzungen
Damit die Anwendung ausgeführt werden kann, werden folgende Programme und Bibliotheken benötigt. 

- Python 3.8.6
- Keras 2.4.3
- PySide2 5.15.2
- matplotlib 3.3.3
- numpy 1.18.5
- pandas 1.1.4
- scikit-learn 0.23.2
- tensorflow 2.3.1

Die Anwendung wurde auf einem Windows 10 x64 Betriebssystem mit dem oben genannten Voraussetzungen erfolgreich getestet. 