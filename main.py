a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))
c = int(input("Введите 3 число: "))

if (a == b and b == c) or (b == c and a == c) or (c == b and a == b):
    print('Равносторонний треуголник')
else:
    if (a == b and b != c) or (b == c and c != a) or (c == b and b != a) or (a!=b and a==c):
        print('Равнобедренный треугольник')
    else:
        if (a != b and b != c) or (b != a and b != c) or (c != b and b != a):
            print('Не равнобедренный и не равносторонний треугольник')