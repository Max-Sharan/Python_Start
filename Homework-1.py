# 6. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
from cmath import sqrt


print('--------------- | TASK 1 | --------------------')

n = int(input('Введите число, обозначающее день недели: '))
while n not in range(1, 8):
    print()
    print('Прости, друг! В неделе только 7 дней!')
    n = int(input('Введите число, обозначающее день недели: '))
if n == 7 or n == 6:
    print()
    print('Сегодня выходной день. Отдыхаем!')
else:
    print()
    print('Сегодня рабочий день, хватит прохлаждаться!')

print('--------------- | TASK 2 | --------------------')

# 7. Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            left = not (x or y or z)
            right = not x and not y and not z
            print(left == right)

print('--------------- | TASK 3 | --------------------')

# 8. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите координату X: '))
y = int(input('Введите координату Y: '))

while x == 0 or y == 0:
    print()
    print('Введите не нулевые значения!')
    x = int(input('Введите координату X: '))
    y = int(input('Введите координату Y: '))
if x > 0 and y > 0:
    print('Ваша точка находится в 1й четверти!')
elif x < 0 and y > 0:
    print('Ваша точка находится во 2й четверти!')
elif x < 0 and y < 0:
    print('Ваша точка находится в 3й четверти!')
else:
    print('Ваша точка находится в 4й четверти!')

print('--------------- | TASK 4 | --------------------')

# 9. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

q = int(input('Введите номер четверти Q: '))
while q not in range(1, 5):
    print()
    print('Номер четверти принимает значения от 1 до 4!')
    q = int(input('Введите номер четверти Q: '))
text_x = 'Координата X точки'
text_y = 'Координата Y точки'
if q == 1:
    print(text_x, '> 0')
    print(text_y, '> 0')
elif q == 2:
    print(text_x, '< 0')
    print(text_y, '> 0')
elif q == 3:
    print(text_x, '< 0')
    print(text_y, '< 0')
else:
    print(text_x, '> 0')
    print(text_y, '< 0')

print('--------------- | TASK 5 | --------------------')

# 10. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print('Введите координаты 1й точки')
x1 = int(input('Введите координату X: '))
y1 = int(input('Введите координату Y: '))

print('Введите координаты 2й точки')
x2 = int(input('Введите координату X: '))
y2 = int(input('Введите координату Y: '))

dist_ab = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(round(dist_ab, 2))
