# Begin1. Дана сторона квадрата a. Найти его периметр P = 4·a.

a = float(input())

perimeter = 4 * a

print(perimeter)


# Begin2. Дана сторона квадрата a. Найти его площадь S = a2.

a = float(input())

area = a ** 2

print(area)


# Begin3. Даны стороны прямоугольника a и b.
# Найти его площадь S = a·b и периметр P = 2·(a + b).

a = float(input())
b = float(input())

area = a * b
perimeter = 2 * (a + b)

print(area)
print(perimeter)


# Begin4. Дан диаметр окружности d. Найти ее длину L = π·d.

d = float(input())

pi = 3.14
length = pi * d

print(length)


# Begin5. Дана длина ребра куба a.
# Найти объем куба V = a3 и площадь его поверхности S = 6·a2.

a = float(input())

volume = a ** 3
surface = 6 * a ** 2

print(volume)
print(surface)


# Begin6. Даны длины ребер a, b, c прямоугольного параллелепипеда.
# Найти его объем V = a·b·c и площадь поверхности S = 2·(a·b + b·c + a·c).

a = float(input())
b = float(input())
c = float(input())

volume = a * b * c
area = 2 * (a*b + b*c + a*c)

print(volume)
print(area)


# Begin7. Найти длину окружности L и площадь круга S заданного радиуса R: L = 2·π·R, S = π·R2.
# В качестве значения π использовать 3.14.
pi = 3.14
r = float(input())

length = 2 * pi * r
area = pi * r ** 2

print(length)
print(area)


# Begin8. Даны два числа a и b. Найти их среднее арифметическое: (a + b)/2.

a = float(input())
b = float(input())

average = (a + b) / 2

print(average)


# Begin9. Даны два неотрицательных числа a и b.
# Найти их среднее геометрическое, то есть квадратный корень из их произведения: √(a·b).

import math

a = float(input())
b = float(input())

geometric_mean = math.sqrt(a*b)

print(geometric_mean)


# Begin10. Даны два ненулевых числа. Найти сумму, разность, произведение и частное их квадратов.

a = float(input())
b = float(input())

a_sq = a ** 2
b_sq = b ** 2

sum = a_sq + b_sq
diff = a_sq - b_sq
prod = a_sq * b_sq
quot = a_sq / b_sq

print(sum)
print(diff)
print(prod)
print()


# Begin11. Даны два ненулевых числа. Найти сумму, разность, произведение и частное их модулей.

a = float(input())
b = float(input())

abs_a = abs(a)
abs_b = abs(b)

sum = abs_a + abs_b
diff = abs_a - abs_b
prod = abs_a * abs_b
quot = abs_a / abs_b

print(sum)
print(diff)
print(prod)
print(quot)


# Begin12. Даны катеты прямоугольного треугольника a и b. Найти его гипотенузу C и периметр P: c = √(a2 + b2), P = a + b + c.

import math

a = float(input())
b = float(input())

c = math.sqrt(a**2 + b**2)
P = a + b + c

print(c)
print(P)


# Begin 13. Даны два круга с общим центром и радиусами R1 и R2 (R1 > R2). Найти площади
# этих кругов S1 и S2, а также площадь S3 кольца, внешний радиус которого
# равен R1, а внутренний радиус равен R2: S1 = π·(R1)2, S2 = π·(R2)2, S3 = S1 − S2.
# В качестве значения π использовать 3.14.

r1 = float(input())
r2 = float(input())

pi = 3.14

s1 = pi * (r1 ** 2)
s2 = pi * (r2 ** 2)
s3 = s1 - s2

print(s1)
print(s2)
print(s3)


# Begin14. Дана длина L окружности. Найти ее радиус R и площадь S круга, ограниченного
# этой окружностью, учитывая, что L = 2·π·R, S = π·R2. В качестве значения π
# использовать 3.14.

L = float(input())
pi = 3.14

R = L / (2 * pi)
S = pi * (R ** 2)

print(R)
print(S)


# Begin15. Дана площадь S круга. Найти его диаметр D и длину L окружности,
# ограничивающей этот круг, учитывая, что L = 2·π·R, S = π·R2. В качестве
# значения π использовать 3.14.

import math

S = float(input())
pi = 3.14

R = math.sqrt(S / pi)
D = 2 * R
L = 2 * pi * R

print(D)
print(L)


# Begin16. Найти расстояние между двумя точками с заданными координатами x1 и x2 на числовой оси: |x2 − x1|.

x1 = float(input())
x2 = float(input())

distance = abs(x2 - x1)

print(distance)


# Begin 17. Даны три точки A, B, C на числовой оси. Найти длины отрезков AC и BC и их сумму.

A = float(input())
B = float(input())
C = float(input())

AC = abs(C - A)
BC = abs(C - B)
total_sum = AC + BC

print(AC)
print(BC)
print(total_sum)


# Begin18. Даны три точки A, B, C на числовой оси. Точка C расположена между точками A и B. Найти произведение длин отрезков AC и BC.

A = float(input())
B = float(input())
C = float(input())

AC = abs(C - A)
BC = abs(C - B)
product = AC * BC

print(product)


# Begin19. Даны координаты двух противоположных вершин прямоугольника: (x1, y1), (x2, y2).
# Стороны прямоугольника параллельны осям координат. Найти периметр и
# площадь данного прямоугольника.

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

width = abs(x2 - x1)
height = abs(y2 - y1)

P = 2 * (width + height)
S = width * height

print(P)
print(S)


# Begin20. Найти расстояние между двумя точками с заданными координатами (x1, y1) и
# (x2, y2) на плоскости. Расстояние вычисляется по формуле √((x2 − x1)2 + (y2 − y1)2).

import math

x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))

x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(distance)


# Begin22. Поменять местами содержимое переменных A и B.

a = float(input())
b = float(input())

temp = a
a = b
b = temp

print(a)
print(b)


# Begin25. Найти значение функции y = 3x6 − 6x2 − 7.

x = float(input())
y = 3 * x ** 6 - 6 * x ** 2 - 7

print(y)


# Begin29. Дано значение угла в градусах (0 < 60 < 360).
# Определить значение этого же угла в радианах, 180 градусов = pi радиано

degrees = float(input())
pi = 3.14
radians = degrees * pi / 180

print(radians)


# Integer1. Дано расстояние L в сантиметрах.
# Найти количество полных метров (1 метр = 100 см).

length_cm = int(input())
meters = length_cm // 100

print(meters)


# Integer5. Даны A и B (A > B). На отрезке A размещены отрезки длины B.
# Найти длину незанятой части отрезка A.

segment = int(input())
piece = int(input())
free_part = segment % piece

print(free_part)


# Begin23: Даны переменные A, B, C. Изменить их значения, переместив содержимое A в B, B — в C, C — в A, и вывести новые значения переменных A, B, C.

A = float(input("Введите A: "))
B = float(input("Введите B: "))
C = float(input("Введите C: "))

A, B, C = C, A, B

print(A, B, C)


# Begin24: Даны переменные A, B, C. Изменить их значения, переместив содержимое A в C, C — в B, B — в A, и вывести новые значения переменных A, B, C.

A = float(input("Введите A: "))
B = float(input("Введите B: "))
C = float(input("Введите C: "))

A, B, C = B, C, A

print(A, B, C)


# Begin26: Найти значение функции y = 4*(x-3)^6 - 7*(x-3)^3 + 2 при данном значении x.

x = float(input("Введите x: "))

diff = x - 3
y = 4 * (diff ** 6) - 7 * (diff ** 3) + 2

print(y)


# Begin27: Дано число A. Вычислить A^8, используя вспомогательную переменную и три операции умножения. Для этого последовательно находить A^2, A^4, A^8. Вывести все найденные степени числа A.

A = float(input("Введите A: "))

A2 = A * A
A4 = A2 * A2
A8 = A4 * A4

print(A2, A4, A8)


# Begin28: Дано число A. Вычислить A^15, используя две вспомогательные переменные и变 пять операций умножения. Для этого последовательно находить A^2, A^3, A^5, A^10, A^15. Вывести все найденные степени числа A.

A = float(input("Введите A: "))

A2 = A * A
A3 = A2 * A
A5 = A3 * A2
A10 = A5 * A5
A15 = A10 * A5

print(A2, A3, A5, A10, A15)


# Begin30: Дано значение угла alpha в радианах (0 < alpha < 2*pi). Определить значение этого же угла в градусах, учитывая, что 180° = pi радианов. В качестве значения pi использовать 3.14.

alpha = float(input("Введите угол в радианах: "))

pi = 3.14
degrees = alpha * 180 / pi

print(degrees)


# Begin31: Дано значение температуры T в градусах Фаренгейта. Определить значение этой же температуры в градусах Цельсия. Температура по Цельсию TC и по Фаренгейту TF связаны соотношением: TC = (TF - 32) * 5 / 9.

TF = float(input("Введите температуру по Фаренгейту: "))

TC = (TF - 32) * 5 / 9

print(TC)


# Begin32: Дано значение температуры T в градусах Цельсия. Определить значение этой же температуры в градусах Фаренгейта. Температура по Цельсию TC и по Фаренгейту TF связаны соотношением: TC = (TF - 32) * 5 / 9.

TC = float(input("Введите температуру по Цельсию: "))

TF = TC * 9 / 5 + 32

print(TF)


# Begin33: Известно, что X кг конфет стоит A рублей. Определить, сколько стоит 1 кг и Y кг этих же конфет.

X = float(input("Введите вес конфет X (кг): "))
A = float(input("Введите стоимость A (руб): "))
Y = float(input("Введите вес конфет Y (кг): "))

price_per_kg = A / X
price_Y_kg = price_per_kg * Y

print(price_per_kg, price_Y_kg)


# Begin34: Известно, что X кг шоколадных конфет стоит A рублей, а Y кг ирисок стоит B рублей. Определить, сколько стоит 1 кг шоколадных конфет, 1 кг ирисок, а также во сколько раз шоколадные конфеты дороже ирисок.

X = float(input("Введите вес шоколадных конфет X (кг): "))
A = float(input("Введите стоимость шоколадных конфет A (руб): "))
Y = float(input("Введите вес ирисок Y (кг): "))
B = float(input("Введите стоимость ирисок B (руб): "))

price_choco = A / X
price_iris = B / Y
ratio = price_choco / price_iris

print(price_choco, price_iris, ratio)


# Begin35: Скорость лодки в стоячей воде V км/ч, скорость течения реки U км/ч (U < V). Время движения лодки по озеру T1 ч, а по реке против течения — T2 ч. Определить путь S, пройденный лодкой. Учесть, что при движении против течения скорость лодки уменьшается на величину скорости течения.

V = float(input("Введите скорость лодки V (км/ч): "))
U = float(input("Введите скорость течения U (км/ч): "))
T1 = float(input("Введите время движения по озеру T1 (ч): "))
T2 = float(input("Введите время движения по реке T2 (ч): "))

S = V * T1 + (V - U) * T2

print(S)


# Begin36: Скорость первого автомобиля V1 км/ч, второго — V2 км/ч, расстояние между ними S км. Определить расстояние между ними через T часов, если автомобили удаляются друг от друга. Данное расстояние равно сумме начального расстояния и общего пути, пройденного автомобилями.

V1 = float(input("Введите скорость первого автомобиля V1 (км/ч): "))
V2 = float(input("Введите скорость второго автомобиля V2 (км/ч): "))
S = float(input("Введите начальное расстояние S (км): "))
T = float(input("Введите время T (ч): "))

total_distance = S + (V1 + V2) * T

print(total_distance)


# Integer2: Дана масса M в килограммах. Используя операцию деления нацело, найти количество полных тонн в ней (1 тонна = 1000 кг).

M = int(input("Введите массу M (кг): "))

tons = M // 1000

print(tons)


# Integer3: Дан размер файла в байтах. Используя операцию деления нацело, найти количество полных килобайтов, которые занимает данный файл (1 килобайт = 1024 байта).

bytes_size = int(input("Введите размер файла в байтах: "))

kb_size = bytes_size // 1024

print(kb_size)


# Integer4: Даны целые положительные числа A и B (A > B). На отрезке длины A размещено максимально возможное количество отрезков длины B (без наложений). Используя операцию деления нацело, найти количество отрезков B, размещенных на отрезке A.

A = int(input("Введите длину отрезка A: "))
B = int(input("Введите длину отрезка B: "))

count = A // B

print(count)
