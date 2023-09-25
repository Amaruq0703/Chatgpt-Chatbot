import PyQt6.QtWidgets as pyqt
import sys
import backend

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
        self.button.clicked.connect(self.chat)

        self.show()

    def chat(self):
        
        userinput = self.inputfield.text().strip()
        self.chatarea.append(f'<p style="color:#333333">Me: {userinput}</p>')
        self.inputfield.clear()

        
        chatter = backend.Chatbot()
        response = chatter.getresponse(userinput)
        self.chatarea.append(f'<p style="color:#333333; background-color: #E9E9E9">Bot: {response}</p>')



app = pyqt.QApplication(sys.argv)
mainwin = ChatbotWindow()
sys.exit(app.exec())
