import time


def num1(number):
    print('')
    print(f"Введённое число: {number}\n"
    f"Тип числа: {type(number)}\n"
    f"Длина числа: {len(number)}\n"
    f"Id  числа: {id(number)}")
    print("======================================")

def phrase1(phrase):
    print(f"Сама фраза: {phrase}\n"
    f"Первая буква: {phrase[0]}\n"
    f"Последняя буква: {phrase[-1]}\n"
    f"Длина фразы: {len(phrase)}")

def check_all(number, phrase):
    if number.isnumeric() and phrase.isnumeric() == False:
        time.sleep(1)
        num1(number)
        phrase1(phrase)
    else:
        print('Вы ввели неправильно данные.')
        exit()


if __name__ == '__main__':
    number = input("Привет, введи пожалуйста число:")
    time.sleep(1)
    phrase = input("Хорошо, теперь введи какую-нибудь фразу:")
    check_all(number, phrase)
