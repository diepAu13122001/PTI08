from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt6.QtCore import Qt
import sys
from PyQt6 import uic
import os

# Add the project root (or a directory containing 'spck') to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# Now import the UserController
from spck.app.controllers.user_controller import UserController

class SignupWindow(QMainWindow):
    def __init__(self):
        super(SignupWindow, self).__init__()
        # load ui
        self.ui = uic.loadUi("spck/app/ui/signup.ui", self)
        # bat su kien cho button
        
        
        # hien thi man hinh
        self.show()
     
        
app = QApplication(sys.argv)
window = SignupWindow()
# Run the application
sys.exit(app.exec())
        
        