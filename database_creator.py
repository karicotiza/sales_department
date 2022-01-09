# -*- coding: utf-8 -*-
# Библиотеки
import random as rd

# Массивы со вспомогательными данными
districts = [
    "Заводской", "Ленинский", "Московский", "Октябрьский",
    "Партизанский", "Первомайский", "Советский"
]

apartments = []

# Ценовые коэффициенты
district_price_coefficient = {
    "Заводской": 1.3, "Ленинский": 0.9, "Московский": 1.2, "Октябрьский": 1.1,
    "Партизанский": 0.8, "Первомайский": 1.0, "Советский": 1.1
}

floor_price_coefficient = {
    "1": 1.2, "2": 1.1, "3": 1.1, "4": 1.0, "5": 1.0, "6": 1.0,
    "7": 1.0, "8": 1.0, "9": 1.1, "10": 0.1, "11": 1.2, "12": 1.4
}


# Подсчёт стоимости квартиры
def price_calculation(district, rooms, floor):
    total_price = (rooms * 6000) * district_price_coefficient[district] * floor_price_coefficient[str(floor)] + 10000
    return int(total_price)


def get_id():
    my_id = ""
    for _ in range(4):
        temp = rd.randint(1, 2)
        if temp == 1:
            char = rd.randint(0, 9)
        else:
            string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            char = rd.choice(string)
        my_id = str(my_id) + str(char)
    return my_id


# Конструктор класса
class Apartment:
    def __init__(self, district, rooms, floor):
        self.district = district
        self.rooms = rooms
        self.floor = floor
        self.price = price_calculation(self.district, self.rooms, self.floor)
        self.id = get_id()

    def __str__(self):
        information = str(
            str(self.district) + " " + str(self.rooms) + " " + str(self.floor)
            + " " + str(self.price) + " " + str(self.id)
        )
        return information


# Генерация данных
for _ in range(1000):
    element = Apartment(districts[rd.randint(0, 6)], rd.randint(1, 4), rd.randint(1, 12))
    apartments.append(element)

# Предварительный просмотр
print("Район Комнаты Этаж Цена Идентификатор")
for element in apartments:
    print(element)

# Заполнение файла данными
# log_file = "database.txt"
# with open(log_file, mode='a', encoding="utf8") as log_file:
#     log_file.write("Район Комнаты Этаж Цена Идентификатор")
#     log_file.write("\n")
#     for element in apartments:
#         log_file.write(str(element))
#         log_file.write("\n")
