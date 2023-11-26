# Task_1

# def found_target():
#     array = [1, 2, 8, 9, 6]
#     if 8 in array:
#         print("true")
#     else:
#         print("false")


# lis = list(range(10, 20))
# target = 55
# for i in range(len(lis)):
#     if target == lis[i]:
#         print(True)
#         break
# else:
#     print(False)

# def declared():
#     numbers = list(range(10, 20))
#
#     target = 5
#     print(target in numbers)
#
#     target = 15
#     print(target in numbers)

#
# declared()
# found_target()

# Task_2

array = [3, 7, 15, -10, 0, -3, 0, 2, 7, 1, 10]
count_positive = 0
count_negative = 0
count_zero = 0
length = len(array)
for i in array:
    if i > 0:
        count_positive += 1
        result_pos = count_positive / length
    elif i < 0:
        count_negative += 1
        result_neg = count_negative / length
    elif i == 0:
        count_zero += 1
        result_zero = count_zero / length

print("-----------------")
print(result_pos)
print(result_neg)
print(result_zero)
print("-----------------")
print(count_positive)
print(count_negative)
print(count_zero)
print(length)



# def metod(set_):
#     total = len(set_)
#
#     pos = len(list(i for i in set_ if i > 0)) / total
#     neg = len(list(i for i in set_ if i < 0)) / total
#     zeros = len(list(i for i in set_ if i == 0)) / total
#
#     return pos, neg, zeros
#
#
# def metod2(set_):
#     total = len(set_)
#
#     pos = len(list(filter(lambda x: x > 0, set_))) / total
#     neg = len(list(filter(lambda x: x < 0, set_))) / total
#     zeros = len(list(filter(lambda x: x == 0, set_))) / total
#
#     return pos, neg, zeros
#
#
# stt_ = set(range(-10, 10))
#
# m = metod(stt_)
# m2 = metod2(stt_)
#
# print(*m)
#
# print(*m2)
