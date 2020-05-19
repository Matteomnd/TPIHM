from PySide2.QtWidgets import QGridLayout,QWidget,QTextEdit,QPushButton,QApplication, QLabel
class Display(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('IHM')
        self.layout = QGridLayout()


        self.label = QLabel("bonjour")
        self.text = QTextEdit("Laisser un commentaire")
        self.button1=QPushButton("success")
        self.button2=QPushButton("cancel")

        
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)


        self.setLayout(self.layout)


if __name__ == "__main__":
   app = QApplication([])
   win = Display()
   win.show()
   app.exec_()
