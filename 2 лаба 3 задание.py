a = input("Введите слово: ")
for x in a:
    if x == "ф":
        print("Ого! Это редкое слово")
        break
else:
    print("Эх! Это не очень редкое слово...")
