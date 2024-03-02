z = 0
n = 0
while n != 3:
    import random
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    c = a + b
    print("Решите пример: ", a, "+", b)
    d = int(input("Введите ответ: "))
    if d != c:
        print("Неверный ответ.Решите еще один пример:")
        n += 1
    else:
        print("Правильно!")
        z = z + 1

print("Игра окончена.Количество правильных ответов: ", z)
