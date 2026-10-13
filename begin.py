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