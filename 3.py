a = float(input("Введите длину стороны a:"))
b = float(input("Введите длину стороны b:"))
c = float(input("Введите длину стороны c:"))
if a+c > b and a+b > c and c+b > a:
    print("Треугольник существует.")
else:
    print("Треугольника не существует.")
