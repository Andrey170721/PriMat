import math
import copy
import numpy as np


kk = 5

a = np.zeros((5, 5))
xx = np.matrix(([1], [2], [3], [4], [5]))
a[0, 0] = 1.0
a[0, 1] = 1.5
a[0, 3] = 3.0
a[1, 0] = 2.0
a[1, 1] = 5.0
a[2, 2] = 4.0
a[2, 3] = 6.0
a[2, 4] = 7.0
a[3, 0] = 4.0
a[3, 2] = 2.0
a[3, 3] = 7.0
a[4, 1] = 8.5
a[4, 4] = 5.0
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        if i == j:
            a[i, j] = 0
            for s in range(a.shape[1]):
                a[i, j] += a[i, s] + 10 ** -kk
b = a * xx


# Проверка матрицы коэффициентов на корректность
def isCorrectArray(a):
    for row in range(0, len(a)):
        if (len(a[row]) != len(b)):
            print('Не соответствует размерность')
            return False

    for row in range(0, len(a)):
        if (a[row][row] == 0):
            print('Нулевые элементы на главной диагонали')
            return False
    return True


# Условие завершения программы на основе вычисления
# расстояния между соответствующими элементами соседних
# итераций в методе решения
def isNeedToComplete(x_old, x_new):
    eps = 0.0001
    sum_up = 0
    sum_low = 0
    for k in range(0, len(x_old)):
        sum_up += (x_new[k] - x_old[k]) ** 2
        sum_low += (x_new[k]) ** 2

    return math.sqrt(sum_up / sum_low) < eps


# Процедура решения
def solution(a, b):
    if not isCorrectArray(a):
        print('Ошибка в исходных данных')
    else:
        count = len(b)  # количество корней

        x = [1 for k in range(0, count)]  # начальное приближение корней

        numberOfIter = 0  # подсчет количества итераций
        MAX_ITER = 100  # максимально допустимое число итераций
        while (numberOfIter < MAX_ITER):

            x_prev = copy.deepcopy(x)

            for k in range(0, count):
                S = 0
                for j in range(0, count):
                    if (j != k): S = S + a[k][j] * x[j]
                x[k] = b[k] / a[k][k] - S / a[k][k]

            if isNeedToComplete(x_prev, x):  # проверка на выход
                break

            numberOfIter += 1

        print('Количество итераций на решение: ', numberOfIter)

        return x


if __name__ == '__main__':
    print(a)
    print(b)

    print('Решение: ', solution(a, b))  # Вызываем процедуру решение