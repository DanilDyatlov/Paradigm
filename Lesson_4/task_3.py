lst = [1, 1, 5, 3, 5, 8, 9, 8]
count_item = filter(lambda x: lst.count(x) > 1, lst)

count_item = list(set(count_item))
print(count_item)



from random import randint

lst: list = [randint(1, 4) for i in range(10)]


def get_dub(arr: lst) -> list:
    pattern = set()
    res_list = []

    for i in arr:
        if i in pattern:
            res_list.append(i)
        else:
            pattern.add(i)

    return res_list


print(lst)
print(get_dub(lst))


('------')

lst = list (range (1, 6))
print (lst)

tmp = map(lambda x: x * x, lst)
print(tmp)


def my_map(func, array):
    for item in array:
        yield func(item)


def my_filter(func, array):
    for item in array:
        if func(item):
            yield item


def frange(begin, end, step):
    while begin < end:
        yield begin
        begin += step


a = frange(1, 2, 0.3)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))