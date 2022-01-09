# -*- coding: utf-8 -*-
class Database:
    def __init__(self, file):
        self.file = file

    def read(self):
        with open(self.file, mode='r', encoding="utf8") as file:
            for line in file:
                split = line[:-1]
                split = split.split(" ")
                print(f'{split[0]: <20}{split[1]: <10}{split[2]: <10}{split[3]: <10}{split[4]: <10}')

    def get(self, district=None, rooms=None, floor=None):
        li = []
        with open(self.file, mode='r', encoding="utf8") as file:
            for line in file:
                split = line[:-1]
                split = split.split(" ")
                if split[0] == district or district is None:
                    if split[1] == str(rooms) or rooms is None:
                        if split[2] == str(floor) or floor is None:
                            temp = f'{split[0]: <20}{split[1]: <10}{split[2]: <10}{split[3]: <10}{split[4]: <10}'
                            li.append(temp)
        return li
