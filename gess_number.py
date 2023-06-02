from random import randint
from time import sleep
print('Добро пожаловать в числовую угадайку!')
sleep(0.5)


def is_valid(number_input, first, end):
    """
    Проверяет, являются ли вводимые данные целыми числоми и в выбранном диапазоне.
    Возвращает True, если введено число. Иначе False.
    """
    return number_input.isdigit() and first.isdigit() and end.isdigit() and int(first) <= int(number_input) <= int(end)

def game_zabava():


    def binary_search(start, end):

        if start > end:
            return None
        mid = (start + end) // 2
        print("Это число " + str(mid) + "?")
        answer = input("Введите 'да', '>', '<': ")
        binary_search.counter += 1
        if answer == "да":
            return mid
        elif answer == ">":
            return binary_search(mid + 1, end)
        elif answer == "<":
            return binary_search(start, mid - 1)
        else:
            print("Некорректный ввод")
            return binary_search(start, end)

    start = input('Введи начало диапазона:')
    end = input('Введи конец диапазона:')
    start = int(start)
    end = int(end)
    print(f'''Загадайте число от {start} до {end}. 
    Если я удагаю число, напечатай: "да".
    Если я укажу неверное число, используй знаки ">", "<" на клавиатуре , чтобы показать мне: твое число больше или меньше.''')
    binary_search.counter = 0
    result = binary_search(start, end)

    if result is not None:
        print(f'Компьютер угадал число: {result} за {binary_search.counter} попыток.')
    else:
        print("Компьютер не смог угадать число.")

    if input('Хочешь сыграть еще раз?').lower() in ['да', 'lf']:
        game_zabava()
    else:
        if input('Опять поменяемся: я буду загадывать, а ты отгадывать?/nНапиши: "да" или "нет"').lower() in ['да', 'lf']:
            game_player()

def game_player():
    """
    Старт игры.
    Забава загадывает число.
    Игрок вводит свои варианты числа.
    """
    first = input('Введи начало диапазона:')
    end = input('Введи конец диапазона:')
    search_number = randint(int(first), int(end))
    # print(search_number)
    print(f'Я загадала число от {first} до {end }. Угадай его.\nВведи СТОП, если захочешь закончить игру.')
    counter = 0
    while True:
        number_input = input(f'Введи целое число от {first} до {end}.')
        if is_valid(number_input, first, end):

            if int(number_input) > search_number:
                print('Слишком много, попробуй еще раз')
                counter += 1
                continue
            elif int(number_input) < search_number:
                print('Слишком мало, попробуй еще раз')
                counter += 1
                continue
            else:
                print(f'Молодец! Ты угадал! Число попыток: {counter+1}')
                break
        elif number_input == 'СТОП':
            break
        else:
            print('''
            Неверный ввод. 
            Введеное значение не является целым числом или находится вне доступного диапазона.
            ''')

    if input('Хочешь сыграть еще раз?').lower() in ['да', 'lf']:
        game_player()
    else:
        if input('А давай поменяемся: ты будешь загадывать, а я отгадывать?/nНапиши: "да" или "нет"').lower() in ['да', 'lf']:
            game_zabava()


def greeting():
    print('''
    Привет!
    Меня зовут Забава.
    Хочешь поиграть со мной в игру Числовая угадайка?
    Правила простые: я загадываю число из указанного тобой диапазона, а ты пробуешь его отгадать.
    Начнем игру? 
    ''')
    sleep(0.5)


def answer():
    answer_question = input('Напиши: "да" или "нет" ')
    if answer_question.lower() in ['да', 'lf']:
        game_player()
    else:
        return print('Очень жаль. Поиграем в другой раз.')


greeting()
answer()
print('Заглядывай почаще.\nДо скорой встречи.')
















