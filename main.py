# -*- coding: utf-8 -*-
# Python 3.8

# Библиотеки
from database import Database
from interface import *


# Подключённая база данных
database = Database("database.txt")


# Вызов окна
window0(database)
