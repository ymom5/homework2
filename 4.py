a = int(input("Введите время суток:"))
if  5<=a<=10:
    print("Утро.")
elif 12<=a<=17:
    print("День.")
elif 18<=a<=22:
    print("Вечер.")
elif 23<= a<=4:
    print("Ночь.")
else:
    print("Ошибка.")
