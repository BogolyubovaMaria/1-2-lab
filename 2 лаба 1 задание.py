n = int(input("введите количество слов: "))
b = ""

for i in range(n):
    a = input("введите слово: ")
    b = b + a + " "
print("Результат:",b)