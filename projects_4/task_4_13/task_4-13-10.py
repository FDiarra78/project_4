print("Сумма элементов массива с нечётными индексами")
print("-" * 50)


array = list(map(float, input("Введите элементы массива через пробел: ").split()))

sum_odd_index = 0
odd_index_elements = []

for i in range(len(array)):
    if i % 2 != 0:  # Индекс нечётный
        sum_odd_index += array[i]
        odd_index_elements.append(array[i])

print("-" * 50)
print(f"Массив: {array}")
print(f"Индексы: {list(range(len(array)))}")
print(f"Элементы с нечётными индексами: {odd_index_elements}")
print(f"Сумма элементов с нечётными индексами: {sum_odd_index}")