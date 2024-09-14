import os
import sys

# Add the project root (or a directory containing 'spck') to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from spck.app.models.user import User
from spck.app.DAO import DAO


class UserController:
    # create ----------------
    def __init__(self):
        self.user_list = []
        self.generate_user_list()
        # self.user_list = list()

    # getter + setter ---------
    def generate_user_list(self):
        # get from data json
        self.user_list = DAO.load_json_data()["users"]

    # def set_user_list(self, user_list):
    #     self.user_list = user_list

    def get_user_list(self):
        return self.user_list

    # read ---------------------
    def search_by_id(self, user_id):
        # tra ve mot user co id tuong ung
        for user in self.user_list:
            if user["id"] == user_id:
                return user
        return None

    def search_by_username(self, user_username):
        # tra ve 1 user co username tuong ung
        for user in self.user_list:
            if user["username"] == user_username:
                return user
        return None

    def search_by_email(self, user_email):
        # tra ve 1 user co email tuong ung
        for user in self.user_list:
            if user["email"] == user_email:
                return user
        return None

    # update -------------------
    def add_user(self, user: User):
        # them user moi vao cuoi cung cua danh sach
        self.user_list.append(user)
        # thay doi du lieu cho file json
        DAO.write_json_data(new_data=self.user_list, object="users")

    def update_user(self, user: User):
        # chinh sua bang user_id
        for i in range(len(self.user_list)):
            if self.user_list[i].id == user.id:
                self.user_list[i] = user  # cap nhat
        # thay doi du lieu cho file json
        DAO.write_json_data(new_data=self.user_list, object="users")

    # delete ------------------
    def delete_user_by_id(self, user_id):
        for i in range(len(self.user_list)):
            if self.user_list[i].id == user_id:
                self.user_list.remove(self.user_list[i])  # xoa trong list
        # thay doi du lieu cho file json
        DAO.write_json_data(new_data=self.user_list, object="users")

    # sort --------------------
    def sort_by_username(self):
        # function 1 dong => lambda
        get_username = lambda user: user["username"]
        # key yeu cau truyen vao 1 ham tra ve username khi loc qua tung user
        return self.user_list.sort(key=get_username)

    def sort_by_email(self):
        return self.user_list.sort(key=lambda user: user["email"])
