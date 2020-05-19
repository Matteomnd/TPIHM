from PySide2.QtWidgets import QVBoxLayout,QWidget,QTextEdit,QPushButton,QApplication, QLabel, QProgressBar, QLineEdit
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt
class Barre(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(300,400)
        self.setWindowTitle("barre d'évolution")

        self.flag = QIcon("fr-flag (1).png")
        self.setWindowIcon(self.flag)


        self.layout = QVBoxLayout()
        self.label = QLabel("Bonjour")
        self.label.setAlignment(Qt.AlignCenter)

        self.barre = QProgressBar()
        self.barre.setValue(100)

        self.line = QLineEdit()
        self.button = QPushButton("progression")
        self.button.setToolTip(" end")



        self.layout.addWidget(self.label)
        self.layout.addWidget(self.barre)
        self.layout.addWidget(self.line)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

if __name__ == "__main__":
   app = QApplication([])
   win = Barre()
   win.show()
   app.exec_()
