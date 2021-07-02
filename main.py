# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json

import anmion

msg = "helle,word"
strings = '123456789'

first_name = "zhu"
last_name = "gq"
all_name = f"{first_name} {last_name}"
number_meany = 14_000_000_000
bicycles = ["跑狼", "永久", "上海"]
numbers = list(range(0, 40, 2))

maps = {"color": "red", "name": "zhangsan"}

listInMap = {"name": "zhangsan", "color": ["green", "yellow"]}
mapInList = [listInMap]
mapInMap = {"book": {"zhangsan": "java", "ls": "C++", "ww": "python"},
            "colors": {"zs": "red", "ls": "yellow", "ww": "back"}}
current_number = 1


class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
        print("----")

    def get_all_fun(self):
        print(f"{self.color}{self.model}")


class DCar(Car):
    def __init__(self, color, model):
        self.battery = 75
        super().__init__(color, model)

    def get_battery(self):
        print(self.battery)

    def get_all_fun(self):
        print(f"{self.color}{self.model}--{self.battery}")


def user_one(name, age):
    person = {"name": name, "age": age}
    return person


def add_list(lists):
    for data in lists:
        print_hi(data)


def auto_fun(*name):
    print(name)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


file_path = '/Users/hdyjzgq/Desktop/5月加班.txt'
file_name = "name.json"

# Press the green button in the gutter to run the script.

if __name__ == '__main__':

    with open(file_name, "w", encoding="utf-8") as file_json:
        json.dump(bicycles, file_json)

    with open(file_name) as r_file:
        print(json.load(r_file))
    print(user_one("zs", age="16"))
    add_list(bicycles)
    auto_fun("a", "b")
    _dog = anmion.Dog("xiao", "12")
    _dog.sit()
    _car = Car("red", "bz")
    _car.color = "yellow"
    _car.get_all_fun()
    _d_car = DCar("red", "bz")
    _d_car.get_all_fun()
    _d_car.get_battery()

    with open(file_path, "w") as new_file:
        new_file.write("5.13 10:00-18:00 公休")

    with open(file_path) as file_object:
        for line in file_object:
            print(line.rstrip())

    # try:
    #     print(5 / 1)
    # except ZeroDivisionError:
    #     print("0000")
    # else:
    #     print("1111")

    # print_hi(keyword.kwlist)
    # print_hi(strings[0:-1])
    # print_hi(msg)
    # msg = "see you word"
    # print_hi(msg)
    # print_hi(all_name)
    # print(4 / 2)
    # print_hi(number_meany)
    # print(bicycles[-1].title())
    # # 自动添加到尾处
    # bicycles.append("凤凰")
    # b = bicycles.pop(0)
    # print_hi(f"my first bicycle is {b}")
    # print_hi(len(bicycles))
    # for bicycle in bicycles:
    #     print_hi(bicycle)
    #
    # for value in range(0, 10):
    #     if value != 6 and value < 8 or value == 7:
    #         print_hi("hehe")
    #     elif value == 0:
    #         print("heihei")
    #     else:
    #         print("heihei")
    #     print_hi(value)
    #
    # print_hi(numbers)
    # print_hi(min(numbers))
    # print_hi(max(numbers))
    # print_hi(sum(numbers))
    # squ = [value ** 2 for value in range(0, 11)]
    # squ2 = squ[:]
    # print_hi(squ)
    # print_hi(squ2)
    #
    # car = "bus"
    # print("Is car == 'bus' ? I p True")
    # print(car == "bus")

    # maps["age"] = 3
    # print_hi(maps["age"])
    # for key, value in maps.items():
    #     print(key)
    #     print(value)
    # del maps["name"]
    # print(maps.get("samll", "bucunzai"))
    # print(maps)
    # # while mapInMap:
    # #     print(mapInMap.keys())
    #
    # while current_number <= 5:
    #     print_hi(current_number)
    #     current_number += 1
    #
    # print("see you")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
