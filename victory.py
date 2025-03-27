"""
14. (МОДУЛЬ 6) В проекте создать новый модуль victory.py
15. Используя любые средства написать программу викторина:
Выбрать минимум 5 известных людей и узнать их год рождения. Программа должна по очереди спрашивать у пользователя год рождения знаменитости. После того как пользователь ввел все ответы, программа считает и выводит на экран:
- количество правильных ответов
- количество ошибок
- процент правильных ответов (можно посчитать как ПРАВИЛЬНЫЕ ОТВЕТЫ*100/ВСЕГО ВОПРОСОВ)
- процент неправильных ответов
После вывода информации программа спрашивает

пользователя хочет ли он начать игру сначала, если да - то повторяем все сначала, если ответ нет - выходим из программы

- В программе с помощью комментариев написать подсказки - правильные ответы для каждой знаменитости
"""

# victory.py

def victory_game():
    # Список знаменитостей и их годов рождения
    celebrities = [
        {"name": "А.С. Пушкин", "year": 1799},  # Правильный ответ: 1799
        {"name": "Л.Н. Толстой", "year": 1828},  # Правильный ответ: 1828
        {"name": "Ф.М. Достоевский", "year": 1821},  # Правильный ответ: 1821
        {"name": "В.И. Ленин", "year": 1870},  # Правильный ответ: 1870
        {"name": "А.А. Ахматова", "year": 1889},  # Правильный ответ: 1889
    ]

    while True:
        correct_answers = 0
        incorrect_answers = 0

        for celebrity in celebrities:
            try:
                answer = int(input(f"Введите год рождения {celebrity['name']}: "))
                if answer == celebrity["year"]:
                    correct_answers += 1
                else:
                    incorrect_answers += 1
            except ValueError:
                print("Неверный формат ввода. Пожалуйста, введите целое число.")

        total_questions = len(celebrities)
        correct_percentage = (correct_answers / total_questions) * 100
        incorrect_percentage = (incorrect_answers / total_questions) * 100

        print(f"Количество правильных ответов: {correct_answers}")
        print(f"Количество ошибок: {incorrect_answers}")
        print(f"Процент правильных ответов: {correct_percentage:.2f}%")
        print(f"Процент неправильных ответов: {incorrect_percentage:.2f}%")

        play_again = input("Хотите ли вы начать игру сначала? (да/нет): ")
        if play_again.lower() != "да":
            break

if __name__ == "__main__":
    victory_game()
