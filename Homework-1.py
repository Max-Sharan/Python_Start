# 6. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

n = int(input('Введите число, обозначающее день недели: '))
while n not in range(1,8):
    print()
    print('Прости, друг! В неделе только 7 дней!')
    n = int(input('Введите число, обозначающее день недели: '))
if n <= 7 and n >= 6:
    print()
    print('Сегодня выходной день. Отдыхаем!')
else:
    print()
    print('Сегодня рабочий день, хватит прохлаждаться!')

print('--------------- || --------------------')

# 7. Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('--------------- || --------------------')

# 8. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print('--------------- || --------------------')

# 9. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

print('--------------- || --------------------')

# 10. Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21