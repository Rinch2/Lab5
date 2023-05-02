from random import randint
def one():
    nums = [2, 8, 15, 21, 36]
    num  = int(input("Введите число: "))
    if num in nums:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")


def two():
    a = list('123456789031')
    b = set([i for i in a if a.count(i) > 1])
    if len(b) > 0:
        print(b)
    else:
        print('Повторяющихся элементов нет')


def three():
    weekdays = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
    i = 0
    while not (1 <= i <= 6):
        i = int(input("Сколько выходных на недели вы хотите? "))
        if not (1 <= i <= 6):
            print("Ошибка")

    print("Ваши выходные дни: ", weekdays[-i::])
    print("Ваши рабочие дни: ", weekdays[:7 - i:])


def four():
    import random
    N = ["Давлетов", "Выдровский", "Лащёв", "Федорова", "Хавалиц", "Юринов", "Семёнов", "Долмацын", "Москвитина", "Сергеев"]
    M = ["Иванова", "Нимаев", "Хомяков", "Родионов", "Иванов", "Хертухеев", "Попов", "Васильев", "Аюшеев", "Перфильева"]
    k = ()

    while len(k) < 2:
        i = random.choice(N)
        if not (i in k):
            k += (i,)
    while len(k) < 5:
        i = random.choice(M)
        if not (i in k):
            k += (i,)
    family = "Иванов" in k
    j = k.count("Иванов")

    print("Изначальные списки:\n", N, "\n", M, "\nПолучившийся кортеж: ", k, "\n", "Его длина:", len(k),
          "\nВ алфавитном порядке: ", sorted(k), "\nФамилия Иванов встречается: ", "«", j, "»" , "раз")

# one()
# two()
# three()
# four()