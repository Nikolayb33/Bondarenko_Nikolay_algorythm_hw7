"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
import random
from timeit import timeit


def median_2(a):
    m = len(a)
    n = len(a) // 2
    while m > n:
        a.remove(max(a))
        m -= 1
    return max(a)


if __name__ == "__main__":
    mass_1 = [2 * m + 1 for m in range(10)]
    random.shuffle(mass_1)
    mass_2 = [2 * m + 1 for m in range(100)]
    random.shuffle(mass_2)
    mass_3 = [2 * m + 1 for m in range(1000)]
    random.shuffle(mass_3)
    print(timeit("median_2(mass_1[:])", globals=globals(), number=100))
    print(timeit("median_2(mass_2[:])", globals=globals(), number=100))
    print(timeit("median_2(mass_3[:])", globals=globals(), number=100))

