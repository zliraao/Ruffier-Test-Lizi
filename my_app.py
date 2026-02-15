from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,QPushButton, QLabel, QVBoxLayout)
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def initUI(self):
        self.btn_next = QPushButton('next')
        self.hello_text = QLabel('Welcome to the Health status detection program!')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.btn_next, alignment = Qt.AlignCenter)         
        self.setLayout(self.layout)
    def set_appear(self):
        self.setWindowTitle('Health')
        self.resize(1000, 600)
        self.move(100, 100)
def main():
    app = QApplication([])
    mw = MainWin()
    app.exec_()
main()# write the code for main app and first screen# write the code for main app and first screen
