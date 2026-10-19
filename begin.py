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


# Boolean1. Проверить истинность высказывания:
# «Число A является положительным».

a = int(input())

print(a > 0)


# Boolean6. Проверить истинность высказывания:
# «Справедливо двойное неравенство A < B < C».

a = int(input())
b = int(input())
c = int(input())

print(a < b < c)


# Boolean12. Проверить истинность высказывания:
# «Каждое из чисел A, B, C положительное».

a = int(input())
b = int(input())
c = int(input())

print(a > 0 and b > 0 and c > 0)


# Boolean14. Проверить истинность высказывания:
# «Ровно одно из чисел A, B, C положительное».

a = int(input())
b = int(input())
c = int(input())

count = (a > 0) + (b > 0) + (c > 0)
print(count == 1)


# If3. Если число положительное — прибавить 1; если отрицательное —
# вычесть 2; если нулевое — заменить на 10.

number = int(input())

if number > 0:
    number += 1
elif number < 0:
    number -= 2
else:
    number = 10

print(number)


# Boolean2: Дано целое число A. Проверить истинность высказывания: «Число A является нечетным».

A = int(input("Введите число A: "))
is_odd = A % 2 != 0
print(is_odd)


# Boolean3: Дано целое число A. Проверить истинность высказывания: «Число A является четным».

A = int(input("Введите число A: "))
is_even = A % 2 == 0
print(is_even)


# Boolean4: Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы неравенства A > 2 и B <= 3».

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
result = (A > 2) and (B <= 3)
print(result)


# Boolean5: Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы неравенства A >= 0 или B < -2».

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
result = (A >= 0) or (B < -2)
print(result)


# Boolean7: Даны три целых числа: A, B, C. Проверить истинность высказывания: «Число B находится между числами A и C».

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
C = int(input("Введите число C: "))
result = (A < B < C) or (C < B < A)
print(result)


# Boolean8: Даны два целых числа: A, B. Проверить истинность высказывания: «Каждое из чисел A и B нечетное».

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
result = (A % 2 != 0) and (B % 2 != 0)
print(result)


# Boolean9: Даны два целых числа: A, B. Проверить истинность высказывания: «Хотя бы одно из чисел A и B нечетное».

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
result = (A % 2 != 0) or (B % 2 != 0)
print(result)


# Boolean10: Даны два целых числа: A, B. Проверить истинность высказывания: «Ровно одно из чисел A и B нечетное».

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
result = (A % 2 != 0) != (B % 2 != 0)
print(result)


# Boolean11: Даны два целых числа: A, B. Проверить истинность высказывания: «Числа A и B имеют одинаковую четность».

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
result = (A % 2) == (B % 2)
print(result)


# Boolean13: Даны три целых числа: A, B, C. Проверить истинность высказывания: «Хотя бы одно из чисел A, B, C положительное».

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
C = int(input("Введите число C: "))
result = (A > 0) or (B > 0) or (C > 0)
print(result)


# Boolean15: Даны три целых числа: A, B, C. Проверить истинность высказывания: «Ровно два из чисел A, B, C являются положительными».

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
C = int(input("Введите число C: "))
result = (int(A > 0) + int(B > 0) + int(C > 0)) == 2
print(result)


# If1: Дано целое число. Если оно является положительным, то прибавить к нему 1; в противном случае не изменять его. Вывести полученное число.

number = int(input("Введите целое число: "))
if number > 0:
    number += 1
print(number)


# If2: Дано целое число. Если оно является положительным, то прибавить к нему 1; в противном случае вычесть из него 2. Вывести полученное число.

number = int(input("Введите целое число: "))
if number > 0:
    number += 1
else:
    number -= 2
print(number)


# If4: Даны три целых числа. Найти количество положительных чисел в исходном наборе.

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

count = 0
if a > 0:
    count += 1
if b > 0:
    count += 1
if c > 0:
    count += 1

print(count)


# If5: Даны три целых числа. Найти количество положительных и количество отрицательных чисел в исходном наборе.

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

pos_count = 0
neg_count = 0

if a > 0:
    pos_count += 1
elif a < 0:
    neg_count += 1

if b > 0:
    pos_count += 1
elif b < 0:
    neg_count += 1

if c > 0:
    pos_count += 1
elif c < 0:
    neg_count += 1

print(pos_count)
print(neg_count)


# For7. Даны A и B (A < B). Найти сумму всех целых чисел от A до B включител
a = int(input())
b = int(input())
total = 0
for i in range(a, b + 1):
    total += i
print(total)


# For1. Даны целые числа K и N (N > 0). Вывести N раз число K.

k = int(input())
n = int(input())
for _ in range(n):
    print(k)


# For3. Даны A и B (A < B). Вывести в порядке убывания все целые числа
# между A и B (не включая A и B) и их количество.

a = int(input())
b = int(input())

count = 0

for i in range(b - 1, a, -1):
    print(i)
count += 1

print(count)


# For10. Дано N (> 0). Найти сумму 1 + 1/2 + 1/3 + ... + 1/N.

n = int(input())


total = 0.0
for i in range(1, n + 1):
    total += 1 / i

print(total)


# For14. Дано N (> 0). Найти N2 по формуле: N2 = 1 + 3 + 5 + ... + (2·N −

n = int(input())

square = 0

for i in range(1, 2 * n, 2):
    square += i

print(square)


# For2: Даны два целых числа A и B (A < B). Вывести в порядке возрастания все целые числа, расположенные между A и B (включая сами числа A и B), а также количество N этих чисел.

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

count = 0
for i in range(A, B + 1):
    print(i)
    count += 1

print(count)


# For4: Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1, 2, ..., 10 кг конфет.

price = float(input("Введите цену 1 кг конфет: "))

for kg in range(1, 11):
    cost = kg * price
    print(f"{kg} кг = {cost:.2f}")


# For5: Дано вещественное число — цена 1 кг конфет. Вывести стоимость 0.1, 0.2, ..., 1 кг конфет.

price = float(input("Введите цену 1 кг конфет: "))

for i in range(1, 11):
    kg = i / 10
    cost = kg * price
    print(f"{kg:.1f} кг = {cost:.2f}")


# For6: Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1.2, 1.4, ..., 2 кг конфет.

price = float(input("Введите цену 1 кг конфет: "))

for i in range(12, 21, 2):
    kg = i / 10
    cost = kg * price
    print(f"{kg:.1f} кг = {cost:.2f}")


# For8: Даны два целых числа A и B (A < B). Найти произведение всех целых чисел от A до B включительно.

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

product = 1
for i in range(A, B + 1):
    product *= i

print(product)


# For9: Даны два целых числа A и B (A < B). Найти сумму квадратов всех целых чисел от A до B включительно.

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

total_sum = 0
for i in range(A, B + 1):
    total_sum += i ** 2

print(total_sum)


# For11: Дано целое число N (> 0). Найти сумму N² + (N + 1)² + (N + 2)² + ... + (2·N)².

N = int(input("Введите число N: "))

total_sum = 0
for i in range(N, 2 * N + 1):
    total_sum += i ** 2

print(total_sum)


# For12: Дано целое число N (> 0). Найти произведение 1.1 · 1.2 · 1.3 · ... (N сомножителей).

N = int(input("Введите число N: "))

product = 1.0
for i in range(1, N + 1):
    multiplier = 1.0 + (i / 10)
    product *= multiplier

print(f"{product:.4f}")


# For13: Дано целое число N (> 0). Найти значение выражения 1.1 - 1.2 + 1.3 - ... (N слагаемых, знаки чередуются).

N = int(input("Введите число N: "))

total_sum = 0.0
sign = 1.0

for i in range(1, N + 1):
    term = 1.0 + (i / 10)
    total_sum += sign * term
    sign = -sign

print(f"{total_sum:.4f}")


# For15: Дано вещественное число A и целое число N (> 0). Найти A в степени N: A^N = A * A * ... * A (число A перемножается N раз).

A = float(input("Введите число A: "))
N = int(input("Введите число N: "))

result = 1.0
for _ in range(N):
    result *= A

print(result)


# While9. Дано целое число N (> 1). Найти наименьшее целое K,
# при котором выполняется неравенство 3^K > N.

n = int(input())
power = 1
k = 0
while power <= n:
    power *= 3
    k += 1
print(k)


# While1. Даны положительные A и B (A > B). Не используя * и /,
# найти длину незанятой части отрезка A после укладки отрезков B.

a = int(input())
b = int(input())
free = a
while free >= b:
    free -= b
print(free)


# While3. Даны положительные N и K. Только через + и -:
# найти частное от деления нацело и остаток.

n = int(input())
k = int(input())
quotient = 0
rest = n
while rest >= k:
    rest -= k
    quotient += 1
print(quotient)
print(rest)


# While8. Дано N (> 0). Найти наибольшее K, для которого K*K <= N.
n = int(input())
k = 0
while (k + 1) * (k + 1) <= n:
    k += 1
print(k)


# While8. Дано N (> 0). Найти наибольшее K, для которого K*K <= N.

n = int(input())
k = 0
while (k + 1) * (k + 1) <= n:
    k += 1
print(k)


# While15. Вклад 1000 руб. растёт на P процентов в месяц.
# Найти, через сколько месяцев он превысит 1100 руб.

p = float(input())
deposit = 1000.0
months = 0
while deposit <= 1100:
    deposit = deposit * (1 + p / 100)
    months += 1
print(months)
print(deposit)


# While2: Даны положительные числа A и B (A > B). На отрезке длины A размещено максимально возможное количество отрезков длины B (без наложений). Не используя операции умножения и деления, найти количество отрезков B, размещенных на отрезке A.

A = float(input("Введите число A: "))
B = float(input("Введите число B: "))

count = 0
temp_A = A
while temp_A >= B:
    temp_A -= B
    count += 1

print(count)


# While4: Дано целое число N (> 0). Если оно является степенью числа 3, то вывести TRUE, если не является – вывести FALSE.

N = int(input("Введите число N: "))

temp = N
while temp > 1 and temp % 3 == 0:
    temp //= 3

result = temp == 1
print(result)


# While5: Дано целое число N (> 0), являющееся некоторой степенью числа 2: N = 2^K. Найти целое число K – показатель этой степени.

N = int(input("Введите число N: "))

K = 0
temp = N
while temp > 1:
    temp //= 2
    K += 1

print(K)


# While6: Дано целое число N (> 0). Найти двойной факториал N: N!! = N·(N–2)·(N–4)·... (последний сомножитель равен 2, если N – четное, и 1, если N – нечетное). Чтобы избежать целочисленного переполнения, вычислять это произведение с помощью вещественной переменной и вывести его как вещественное число.

N = int(input("Введите число N: "))

factorial = 1.0
temp = N
while temp > 0:
    factorial *= temp
    temp -= 2

print(factorial)


# While7: Дано целое число N (> 0). Найти наименьшее целое положительное число K, квадрат которого превосходит N: K² > N. Функцию извлечения квадратного корня не использовать.

N = int(input("Введите число N: "))

K = 1
while K ** 2 <= N:
    K += 1

print(K)


# While9: Дано целое число N (> 1). Найти наименьшее целое число K, при котором выполняется неравенство 3^K > N.

N = int(input("Введите число N: "))

K = 1
while 3 ** K <= N:
    K += 1

print(K)


# While10: Дано целое число N (> 1). Найти наибольшее целое число K, при котором выполняется неравенство 3^K < N.

N = int(input("Введите число N: "))

K = 0
while 3 ** (K + 1) < N:
    K += 1

print(K)


# While12: Дано целое число N (> 1). Вывести наибольшее из целых чисел K, для которых сумма 1 + 2 + ... + K будет меньше или равна N, и саму эту сумму.

N = int(input("Введите число N: "))

total_sum = 0
K = 0
while total_sum + (K + 1) <= N:
    K += 1
    total_sum += K

print(K)
print(total_sum)


# While13: Дано число A (> 1). Вывести наименьшее из целых чисел K, для которых сумма 1 + 1/2 + ... + 1/K будет больше A, и саму эту сумму.

A = float(input("Введите число A: "))

total_sum = 0.0
K = 0
while total_sum <= A:
    K += 1
    total_sum += 1 / K

print(K)
print(f"{total_sum:.4f}")


# While14: Дано число A (> 1). Вывести наибольшее из целых чисел K, для которых сумма 1 + 1/2 + ... + 1/K будет меньше A, и саму эту сумму.

A = float(input("Введите число A: "))

total_sum = 0.0
K = 0
while total_sum + (1 / (K + 1)) < A:
    K += 1
    total_sum += 1 / K

print(K)
print(f"{total_sum:.4f}")


# Err7. Читать ввод, пока не будет введено целое число.
# Некорректный ввод не считается и не роняет программу.

while True:
    try:
        number = int(input())
        break
    except ValueError:
        print("Это не число. Попробуй ещё:")
print(number)


# Err1. Прочитать целое число и вывести его.
# Если введено не число — вывести "Ошибка ввода".

try:
    number = int(input())
    print(number)
except ValueError:
    print("Ошибка ввода")


# Err3. Прочитать два целых числа и вывести частное.
# Нечисловой ввод — "Ошибка ввода", ноль в делителе —
# "Делить на ноль нельзя".

try:
    a = int(input())
    b = int(input())
    print(a / b)
except ValueError:
    print("Ошибка ввода")
except ZeroDivisionError:
    print("Делить на ноль нельзя")


# Err4. Прочитать целое число; в else вывести 100 / n,
# в finally вывести "Вычисление завершено".

try:
    n = int(input())
    result = 100 / n
except ValueError:
    print("Ошибка ввода")
except ZeroDivisionError:
    print("Делить на ноль нельзя")
else:
    print(result)
finally:
    print("Вычисление завершено")


# Err8. Читать числа до пустой строки; нечисловые строки
# пропускать со счётом. Вывести сумму и число пропусков.

total = 0
skipped = 0
while True:
    line = input()
    if line == "":
        break
try:
    total += int(line)
except ValueError:
    skipped += 1
    print("Пропущено: не число")
print(total)
print(skipped)


# Err10. Читать пункт меню 1..5 с двумя уровнями проверки:
# формат и диапазон. Вывести выбранный пункт.

while True:
    try:
        choice = int(input())
    except ValueError:
        print("Введите число")
        continue
    if 1 <= choice <= 5:
        break
    print("Такого пункта нет")
print(choice)


# Err2: Прочитать два целых числа и вывести их частное с одним знаком после точки. При делении на ноль вывести «Делить на ноль нельзя». Нечисловой ввод обрабатывать не требуется.

try:
    a = int(input())
    b = int(input())
    result = a / b
    print(f"{result:.1f}")
except ZeroDivisionError:
    print("Делить на ноль нельзя")


# Err5: Прочитать строку и целое число – индекс. Вывести символ строки под этим индексом. Если индекса нет, вывести «Нет такого символа». Нечисловой ввод обрабатывать не требуется.

s = input()
try:
    index = int(input())
    print(s[index])
except IndexError:
    print("Нет такого символа")


# Err6: Та же задача, что Err5, но с двумя ветками: нечисловой индекс – «Ошибка ввода», индекс вне границ – «Нет такого символа».

s = input()
try:
    index = int(input())
    print(s[index])
except ValueError:
    print("Ошибка ввода")
except IndexError:
    print("Нет такого символа")


# Err7: Читать ввод, пока не будет введено целое число. Некорректный ввод не роняет программу и не считается: печатается «Это не число. Попробуй ещё:», чтение повторяется. Вывести полученное число.

while True:
    try:
        number = int(input())
        print(number)
        break
    except ValueError:
        print("Это не число. Попробуй ещё:")


# Err9 СЛОЖНОЕ: Прочитать возраст. Если число отрицательное или больше 120, поднять ValueError с текстом «Возраст вне допустимого диапазона» и поймать его же: в except вывести «Отклонено:» и текст ошибки. Корректный возраст вывести как «Принято:» и число.

try:
    age = int(input())
    if age < 0 or age > 120:
        raise ValueError("Возраст вне допустимого диапазона")
    print(f"Принято: {age}")
except ValueError as e:
    print(f"Отклонено: {e}")


# Err11: Прочитать два числа и вывести их частное. Обе возможные ошибки обработать одним кортежем в except с сообщением «Посчитать не удалось»; при успехе в else вывести частное с двумя знаками после точки.

try:
    a = float(input())
    b = float(input())
    result = a / b
except (ValueError, ZeroDivisionError):
    print("Посчитать не удалось")
else:
    print(f"{result:.2f}")


# Err12 СЛОЖНОЕ: Прочитать целое число. При ошибке вывести текст исключения и его тип отдельными строками, пользуясь as e и type(e). При успехе вывести само число.

try:
    number = int(input())
    print(number)
except Exception as e:
    print(e)
    print(type(e))


# List5

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
d = int(input())
a.append(d)
print(a)
print(len(a))


# List1

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
print(len(a))
print(a[0])


# List4

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
imax = 0
for i in range(len(a)):
    if a[i] > a[imax]:
        imax = i
print(imax)
print(a[imax])


# List6

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k1 = int(input())
k2 = int(input())
b = a[k1:k2 + 1]
print(b)
s = 0
for x in b:
    s = s + x
print(s)

# List8

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
d = int(input())
if d in a:
    a.remove(d)
print(a)
print(len(a))


# List11

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = 0
for i in range(len(a)):
    if a[i] < 0:
        a[i] = 0
        k = k + 1
print(a)
print(k)


# List2

A = list(map(int, input().split()))
K = int(input())

print(A[K])
print(A[-1])
print(K)


# List3

A = list(map(int, input().split()))

even_indexed_elements = A[0::2]

sum_even = sum(even_indexed_elements)
prod_even = 1
for x in even_indexed_elements:
    prod_even *= x

print(sum_even)
print(prod_even)


# List5

A = list(map(int, input().split()))
D = int(input())

A.append(D)
print(A)
print(len(A))


# List7

A = list(map(int, input().split()))

print(A[::-1])
print(A)


# List9

A = list(map(int, input().split()))

average = sum(A) / len(A)
filtered_elements = [x for x in A if x > average]

print(filtered_elements)
print(len(filtered_elements))


# List10

A = input().split()

longest = A[0]
shortest = A[0]

for s in A:
    if len(s) > len(longest):
        longest = s
    if len(s) < len(shortest):
        shortest = s

print(longest, len(longest))
print(shortest, len(shortest))


# List12

A = list(map(int, input().split()))
K = int(input())

A.insert(K, 0)
print(A)
print(len(A))


# List13

A = list(map(int, input().split()))

removed = A.pop()
print(removed)
print(A)


# List14

A = list(map(int, input().split()))
D = int(input())

count_D = A.count(D)
first_index = A.index(D) if D in A else -1

print(count_D)
print(first_index)


# List15

A = list(map(int, input().split()))

odd_positions_elements = A[0::2]
print(odd_positions_elements)
print(sum(odd_positions_elements))
