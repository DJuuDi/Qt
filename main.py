from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
import secrets 
class PassGenerator(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.generate_password.clicked.connect(self.generet_password)

    def generet_password(self):
        password = secrets.token_hex(8)
        self.ui.password_labl.setText(password)
        with open("my_pass.txt", "w") as file:
            file.write(password)


app = QApplication([])
ex = PassGenerator()
ex.show()
app.exec_()