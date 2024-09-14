from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import Qt
import sys
from PyQt6 import uic
import os

# Add the project root (or a directory containing 'spck') to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# Now import the UserController
from spck.app.controllers.user_controller import UserController


class SearchWindow(QMainWindow):
    def __init__(self):
        super(SearchWindow, self).__init__()
        self.ui = uic.loadUi("spck/app/ui/search.ui", self)

        # khai bao 1 controller de su dung
        self.user_controller = UserController()

        self.userEmailList = []
        self.setUserEmailList()
        self.ui.list_widget.addItems(self.userEmailList)
        # bat su kien cho nut search
        self.ui.search_btn.clicked.connect(self.searchEmail)
        self.show()

    def setUserEmailList(self):
        user_list = self.user_controller.get_user_list()
        for user in user_list:
            self.userEmailList.append(user["email"])

    def searchEmail(self):
        # lay du lieu tu line edit
        search_key = self.ui.search_input.text()
        # kiem tra neu co du lieu => tim kiem
        if search_key:
            user = self.user_controller.search_by_email(search_key)
            if user:
                # gan vao cho label clicked
                self.ui.clicked_value.setText(
                    user["username"] + ": " + user["password"]
                )
            else:
                # bao loi khong tim thay
                self.ui.clicked_value.setText("Khong tim thay du lieu phu hop")


app = QApplication(sys.argv)
window = SearchWindow()

# # Show the window (in case it's not automatically shown)
# window.show()

# Run the application
sys.exit(app.exec())
