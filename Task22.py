# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.

# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)

# Output: 6 12

import random

first_len = int(input("Введите длину первого ряда чисел: "))
second_len = int(input("Введите длину второго ряда чисел: "))

first_list = []
second_list = []

for i in range (first_len):
    first_list.append(random.randint(0, 10))

for i in range (second_len):
    second_list.append(random.randint(0, 10))

print(first_list)
print(second_list)

result = set(first_list) & set(second_list)
result = sorted(result)

if len(result) > 0:
    print(f"В обоих наборах есть числа: {result}")
else:
    print("Одинакивых чисел в наборах нет")
