"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
import random
from timeit import timeit


def median(a):
    i = 1
    j = 2
    while i < len(a):
        if a[i - 1] < a[i]:
            i = j
            j = j + 1
        else:
            a[i - 1], a[i] = a[i], a[i - 1]
            i = i - 1
            if i == 0:
                i = j
                j = j + 1
    return a[len(a) // 2]


if __name__ == "__main__":
    mass_1 = [2 * m + 1 for m in range(10)]
    random.shuffle(mass_1)
    mass_2 = [2 * m + 1 for m in range(100)]
    random.shuffle(mass_2)
    mass_3 = [2 * m + 1 for m in range(1000)]
    random.shuffle(mass_3)
    print(timeit("median(mass_1[:])", globals=globals(), number=100))
    print(timeit("median(mass_2[:])", globals=globals(), number=100))
    print(timeit("median(mass_3[:])", globals=globals(), number=100))
