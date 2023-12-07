# data = (("Sergey", 20), ("Maxim", 22), ("Alex", 26))
# data_1 = {"Sergey": 20, "Maxim": 22, "Alex": 26}
# data_2 = [{"name": "Sergey", "age": 20}, {"name": "Maxim", "age": 22}, {"name": "Alex", "age": 26}]

def count_people_above_age(people, age):
    count = 0
    for person in people:
        if person['age'] > age:
            count += 1
    return count


def count_people_above_age1(people, age):
    return len(list(filter(lambda person: person['age'] > age, people)))


def count_older_than(people, age):
    is_older = map(lambda person: person['age'] > age, people)
    return sum(is_older)


# Пример использования скрипта
people_data = [
    {'name': "Sergey", 'age': 25},
    {'name': 'Maxim', 'age': 35},
    {'name': 'Anna', 'age': 42},
    {'name': 'Sophie', 'age': 18},
    {'name': 'Den', 'age': 29}
]

age_limit = 30
print(f"Количество людей старше {age_limit} лет: {count_people_above_age(people_data, age_limit)}")


count_people_above_age1(people_data, age_limit)
print(f"Количество людей старше {age_limit} лет: {count_people_above_age1(people_data, age_limit)}")

age_limit = 30
count = count_older_than(people_data, age_limit)
print(f"Количество людей старше {age_limit} лет: {count}")

"----------------------------------"
name_and_age = {
    "Rust": 35,
    "Python": 30,
    "Class": 21,
    "Struct": 19,
    "List": 39,
    "Vector": 36
}

age = 30


def filter_min_age(arr: dict, min_age: int) -> int:
    return len(list(filter(lambda name: min_age < arr[name], arr)))


def map_min_age(arr: dict, min_age: int) -> int:
    return sum(map(lambda name: arr[name] > min_age, arr))


fil = filter_min_age(name_and_age, age)

map_ = map_min_age(name_and_age, age)

print(fil, map_, sep="\n")


"----------------------------"
def get_count(data,age_filter):
    count = 0
    for age in data.values():
        if age > age_filter:
            count += 1
    return count


data = {"Pavel": 20, "Maxim": 42, "Sergey": 75, "Andrey": 18, "gena": 31}
print(get_count(data, 30))


