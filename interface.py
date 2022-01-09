# -*- coding: utf-8 -*-
# Библиотеки
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.ttk import Combobox


# Основное окно
def window0(database):
    def clicked_1():
        window.destroy()
        window1(database)

    def clicked_2():
        window.destroy()
        window2(database)

    def clicked_3():
        window.destroy()
        window3(database)

    def clicked_4():
        window.destroy()

    # Окно
    window = Tk()
    window.title("Отдел продаж")

    # Кнопки
    bt_1 = Button(window, text="Просмотр доступных квартир ", width=30, command=clicked_1)
    bt_1.grid(row=0, pady=(20, 5), padx=20)

    bt_2 = Button(window, text="Расчёт стоимости квартиры", width=30, command=clicked_2)
    bt_2.grid(row=1, pady=5, padx=20)

    bt_3 = Button(window, text="Заполнение бланка оплаты", width=30, command=clicked_3)
    bt_3.grid(row=2, pady=5, padx=20)

    bt_4 = Button(window, text="Выйти", width=30, bg="red", fg="white", command=clicked_4)
    bt_4.grid(row=3, pady=(5, 20), padx=20)

    window.mainloop()


# Просмотр доступных квартир
def window1(database):
    def clicked_1():
        tf.delete(1.0, END)
        district = cm_1.get()
        if district == "По умолчанию":
            district = None
        rooms = cm_2.get()
        if rooms == "По умолчанию":
            rooms = None
        floor = cm_3.get()
        if floor == "По умолчанию":
            floor = None
        if district is None and rooms is None and floor is None:
            tf.insert(INSERT, "База данных слишком большая, выберите хотя бы одно условие")
        else:
            tf.insert(INSERT, f'{"Район": <20}{"Комнаты": <10}{"Этаж": <10}{"Цена": <10}{"ID": <10}\n')
            li = database.get(district=district, rooms=rooms, floor=floor)
            for line in li:
                tf.insert(INSERT, line + "\n")

    def clicked_2():
        window.destroy()
        window0(database)

    # Окно
    window = Tk()
    window.title("Просмотр доступных квартир")

    # Район
    lb_1 = Label(window, text="Район")
    lb_1.grid(column=0, row=1, pady=(20, 5), padx=20, sticky=W)

    cm_1 = Combobox(window)
    cm_1['values'] = (
        "По умолчанию", "Заводской", "Ленинский", "Московский", "Октябрьский",
        "Партизанский", "Первомайский", "Советский"
    )
    cm_1.current(0)
    cm_1.grid(column=1, row=1, pady=(20, 5), padx=20, sticky=E)

    # Комнаты
    lb_2 = Label(window, text="Комнаты")
    lb_2.grid(column=0, row=2, pady=5, padx=20, sticky=W)

    cm_2 = Combobox(window)
    cm_2['values'] = (
        "По умолчанию", "1", "2", "3", "4",
    )
    cm_2.current(0)
    cm_2.grid(column=1, row=2, pady=5, padx=20, sticky=E)

    # Этаж
    lb_3 = Label(window, text="Этаж")
    lb_3.grid(column=0, row=3, pady=5, padx=20, sticky=W)

    cm_3 = Combobox(window)
    cm_3['values'] = (
        "По умолчанию", "1", "2", "3", "4", "5",
        "6", "7", "8", "9", "10", "11", "12",
    )
    cm_3.current(0)
    cm_3.grid(column=1, row=3, pady=5, padx=20, sticky=E)

    # Поле
    tf = scrolledtext.ScrolledText(window, width=60, height=10)
    tf.grid(column=0, row=4, columnspan=2, pady=20, padx=20)
    tf.insert(INSERT, f'{"Район": <20}{"Комнаты": <10}{"Этаж": <10}{"Цена": <10}{"ID": <4}\n')

    # Кнопки
    bt_2 = Button(window, text="Назад", width=15, bg="red", fg="white", command=clicked_2)
    bt_2.grid(column=0, row=5, columnspan=2, pady=20, padx=20, sticky=W)

    bt_2 = Button(window, text="Поиск", width=15, command=clicked_1)
    bt_2.grid(column=1, row=5, columnspan=2, pady=20, padx=20, sticky=E)

    window.mainloop()


# Расчёт стоимости
def window2(database):
    def clicked_1():
        price = int(en_1.get())
        length = int(cm_1.get())
        first_payment = (price / 100) * 30
        lb_4.configure(text=(round(first_payment, 2)))
        lb_6.configure(text=(round(((price-first_payment)/length), 2)))

    def clicked_2():
        window.destroy()
        window0(database)

    # Окно
    window = Tk()
    window.title("Расчёт стоимости квартиры")

    # Ввод цены
    lb_1 = Label(window, text="Цена")
    lb_1.grid(column=0, row=0, pady=(20, 5), padx=20, sticky=W)

    en_1 = Entry(window, width=40)
    en_1.grid(column=1, row=0, pady=(20, 5), padx=20, sticky=E)

    # Месяцев на оплату
    lb_2 = Label(window, text="Месяцев на оплату")
    lb_2.grid(column=0, row=1, pady=5, padx=20, sticky=W)

    cm_1 = Combobox(window, width=20)
    cm_1['values'] = (
        "12", "24", "36", "48", "60",
        "120", "180", "240", "360",
    )
    cm_1.current(0)
    cm_1.grid(column=1, row=1, pady=5, padx=20, sticky=E)

    # Первый взнос
    lb_3 = Label(window, text="Первый взнос")
    lb_3.grid(column=0, row=2, pady=5, padx=20, sticky=W)

    lb_4 = Label(window, text="-")
    lb_4.grid(column=1, row=2, pady=5, padx=20, sticky=E)

    # Оплата в месяц
    lb_5 = Label(window, text="Оплата в месяц")
    lb_5.grid(column=0, row=3, pady=5, padx=20, sticky=W)

    lb_6 = Label(window, text="-")
    lb_6.grid(column=1, row=3, pady=5, padx=20, sticky=E)

    # Кнопки
    bt_1 = Button(window, text="Назад", width=15, bg="red", fg="white", command=clicked_2)
    bt_1.grid(column=0, row=4, pady=20, padx=20, sticky=W)

    bt_2 = Button(window, text="Расчитать", width=15, command=clicked_1)
    bt_2.grid(column=1, row=4, pady=20, padx=20, sticky=E)

    window.mainloop()


# Заполнение бланка оплаты
def window3(database):
    def clicked_1():
        if en_1.get() == "" or en_2.get() == "" or en_3.get() == "" \
                or en_4.get() == "" or en_5.get() == "" or en_6.get() == "":
            messagebox.showinfo('Уведомление', 'Заполните все поля')
        else:
            file = "Бланки/" + en_6.get() + ".txt"
            with open(file, mode='a', encoding="utf8") as file:
                file.write("ФИО " + en_1.get() + "\n")
                file.write("Почта " + en_2.get() + "\n")
                file.write("Карта " + en_3.get() + "\n")
                file.write("Срок " + en_4.get() + "\n")
                file.write("CVV " + en_5.get() + "\n")
                file.write("ID " + en_6.get() + "\n")
            messagebox.showinfo('Уведомление', 'Запись успешно создана')
            window.destroy()

    def clicked_2():
        window.destroy()
        window0(database)

    # Окно
    window = Tk()
    window.title("Заполнение бланка оплаты")

    # Ввод ФИО
    lb_1 = Label(window, text="Ф.И.О.")
    lb_1.grid(column=0, row=1, pady=(20, 5), padx=20, sticky=W)

    en_1 = Entry(window, width=40)
    en_1.grid(column=1, row=1, pady=(20, 5), padx=20, sticky=E)

    # Ввод почты
    lb_2 = Label(window, text="Почта")
    lb_2.grid(column=0, row=2, pady=5, padx=20, sticky=W)

    en_2 = Entry(window, width=40)
    en_2.grid(column=1, row=2, pady=5, padx=20, sticky=E)

    # Ввод данных карты
    lb_3 = Label(window, text="Номер карты")
    lb_3.grid(column=0, row=3, pady=5, padx=20, sticky=W)

    en_3 = Entry(window, width=40)
    en_3.grid(column=1, row=3, pady=5, padx=20, sticky=E)

    lb_4 = Label(window, text="Срок действия карты")
    lb_4.grid(column=0, row=4, pady=5, padx=20, sticky=W)

    en_4 = Entry(window, width=40)
    en_4.grid(column=1, row=4, pady=5, padx=20, sticky=E)

    lb_5 = Label(window, text="CVV код")
    lb_5.grid(column=0, row=5, pady=5, padx=20, sticky=W)

    en_5 = Entry(window, width=40)
    en_5.grid(column=1, row=5, pady=5, padx=20, sticky=E)

    # Идентификатор квартиры
    lb_6 = Label(window, text="ID квартиры")
    lb_6.grid(column=0, row=6, pady=5, padx=20, sticky=W)

    en_6 = Entry(window, width=40)
    en_6.grid(column=1, row=6, pady=5, padx=20, sticky=E)

    # Кнопки
    bt_1 = Button(window, text="Назад", width=15, bg="red", fg="white", command=clicked_2)
    bt_1.grid(column=0, row=7, pady=20, padx=20, sticky=W)

    bt_2 = Button(window, text="Подтвердить", width=15, command=clicked_1)
    bt_2.grid(column=1, row=7, pady=20, padx=20, sticky=E)

    window.mainloop()
