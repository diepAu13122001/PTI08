import json

class DAO:
    # khai bao bien url
    json_url = "spck/data/data.json"

    @classmethod
    def load_json_data(cls):
        data = dict()
        # doc du lieu => gan vao bien data
        with open(cls.json_url, "r") as json_file:
            data = json.load(json_file)
        return data

    @classmethod
    def write_json_data(cls, new_data, object):
        # ghi de du lieu cho 1 thuoc tinh trong data
        data = cls.load_json_data()
        data[object] = new_data
        with open(cls.json_url, "w") as json_file:
            json.dump(data, json_file)
        print("successful writing!")