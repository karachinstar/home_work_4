# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в
# порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m -кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
import random

n_set = set(random.randint(1, 10) for k in range(int(input('Введите кол-во элементов первого множества: '))))
print(n_set)
m_set = set(random.randint(1, 10) for i in range(int(input('Введите кол-во элементов второго множества: '))))
print(m_set)
s_set = sorted(n_set.intersection(m_set))
print(*s_set)
