b = ""
a = input("Введите слово: ")
while a != "stop":
    b = b + a + " "
    a = input("Введите слово: ")

print(b)