from PySide2.QtWidgets import *
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QGridLayout()
        self.button1= QPushButton("valider")
        self.line = QLineEdit()
        self.button2 = QPushButton("annuler")

        self.layout.addWidget(self.button1,1,0)
        self.layout.addWidget(self.line,0,0,1,2)
        self.layout.addWidget(self.button2,1,1)

        self.setLayout(self.layout)

if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   app.exec_()








