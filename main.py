import PyQt6.QtWidgets as pyqt
import sys

class ChatbotWindow(pyqt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(800, 600)

        self.chatarea = pyqt.QTextEdit(self)
        self.chatarea.setGeometry(10, 10, 780, 400)

        self.inputfield  = pyqt.QLineEdit(self)
        self.inputfield.setGeometry(10, 470, 780, 50)

        self.button = pyqt.QPushButton('Send', self)
        self.button.setGeometry(690, 530, 100, 50)

        self.show()


app = pyqt.QApplication(sys.argv)
mainwin = ChatbotWindow()
sys.exit(app.exec())
