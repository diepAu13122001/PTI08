class User:
    count_id = 0

    def __init__(self, username, password, email, avatar, rated_list):
        # khai bao thuoc tinh cho user + gan gia tri
        self.username = username
        self.password = password
        self.email = email
        self.avatar = avatar
        self.rated_list = rated_list
        # add id
        

    # cap nhat id tu dong
    @staticmethod
    def create_id():
        count_id = count_id + 1
        return count_id

    # getter ---------------------
    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_email(self):
        return self.email

    def get_avatar(self):
        return self.avatar

    def get_rated_list(self):
        return self.rated_list

    # setter ---------------------
    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def set_email(self, email):
        self.email = email

    def set_avatar(self, avatar):
        self.avatar = avatar

    def set_rated_list(self, rated_list):
        self.rated_list = rated_list


# getter + setter: the hien tinh dong goi cua OOP

