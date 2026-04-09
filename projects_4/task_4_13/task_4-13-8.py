print("Количество положительных чисел в массиве")
print("-" * 50)

array = list(map(float, input("Введите элементы массива через пробел: ").split()))

positive_count = 0
for num in array:
    if num > 0:
        positive_count += 1


print("-" * 50)
print(f"Массив: {array}")
print(f"Количество положительных чисел: {positive_count}")