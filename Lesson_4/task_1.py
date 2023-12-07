# def normalization(arr):
#     x_max = max(arr)
#     x_min = min(arr)
#
#     def normalize(x):
#         x_norm = (x - x_min) / (x_max - x_min)
#         return x_norm
#
#     normalized_arr = list(map(normalize, arr))
#     return normalized_arr
#
#
# # Пример использования функции normalization
# array = [1, 2, 3, 4, 5]
# normalized_array = normalization(array)
# print(normalized_array)


# from random import shuffle
#
#
# def normalize(vec: list) -> list:
#     x_min = min(vec)
#     x_max = max(vec)
#     return list(map(lambda x: (x - x_min) / (x_max - x_min), vec))
#
#
# vector = list(range(10))
# shuffle(vector)
# norm = normalize(vector)
# print(*vector)
# print(*map(lambda x: round(x, 5), norm))
