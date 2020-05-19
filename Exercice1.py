from PySide2.QtWidgets import QWidget,QVBoxLayout, QPushButton, QCheckBox, QApplication, QLineEdit
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QVBoxLayout()
        self.button1= QPushButton("valider")
        self.line = QLineEdit()
        self.button2 = QPushButton("annuler")

        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.line)
        self.layout.addWidget(self.button2)

        self.setLayout(self.layout)

if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   app.exec_()








