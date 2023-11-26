# Задание 1
# След матрицы - это сумма чисел на её главной диагонали. След определён только для квадратных матриц
# (количество столбцов = количеству строк).

# №1
# if __name__ == '__main__':
#     matrix = [
#         [1, 2, 3],
#         [4, 5, 8],
#         [9, 10, 11]
#     ]
#     sum_ = 0
#     for i in range(len(matrix)):
#         sum_ += matrix[i][i]
#
#     print(sum_)

#№2
matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 5]]

result = 0

if len(matrix) == len(matrix[0]):
    for i in range(len(matrix)):
        result += matrix[i][i]

    print(result)

