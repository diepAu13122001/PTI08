import json


def data_load_json():
    data = dict()
    with open("./spck/data/data.json", "r") as json_in:
        json_data = json.load(json_in)
        data = json_data
    return data


data = data_load_json()["users"]
print(data[4])


if True:
    print("a")
else:
    print("b")
print("a") if True else print("b")

rs = ""
for i in range(5):
    rs = rs + str(i) + ", "
rs1 = ""
rs1 = ", ".join([i.name for i in range(5) if i.completed == False])
if rs1 == "":
    print("All finished")


def sum(a, b):
    return a + b
# lambda
my_sum = lambda a, b: a + b
my_sum(1,2)

