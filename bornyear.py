"""
6. (МОДУЛЬ 2) В проекте создать новый модуль bornyear.py
7. Написать программу используя условные операторы:
- Спросить у пользователя год рождения А.С Пушкина
- Если пользователь ввел верный год вывести 'Верно'
- Если пользователь ошибся вывести 'Неверно'
"""
def check_born_date():
    pushkin_bornyear = 1799
    try:
        born_year = int(input("Введите год рождения А.С. Пушкина: "))
        if born_year == pushkin_bornyear:
            print("Верно")
        else:
            print("Неверно")
    except ValueError:
        print("Неверный формат ввода")

if __name__ == "__main__":
    check_born_date()