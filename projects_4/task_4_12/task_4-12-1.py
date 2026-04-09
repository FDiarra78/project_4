
print("Сортировка пузырьком по возрастанию")
print("=" * 50)

array = [7, 3, 8, 1, 4, 6, 2, 5]
print(f"Исходный массив: {array}")
print("-" * 50)

n = len(array)
iteration = 1

for i in range(n - 1):
    swapped = False
    print(f"Итерация {iteration}:")
    
    for j in range(n - 1 - i):
        if array[j] > array[j + 1]:
            # Меняем элементы местами
            array[j], array[j + 1] = array[j + 1], array[j]
            swapped = True
            print(f"  {array} ({array[j+1]} и {array[j]} поменялись)")
        else:
            print(f"  {array} ({array[j]} и {array[j+1]} не меняются)")
    
    iteration += 1
    print()

    if not swapped:
        break

print("=" * 50)
print(f"Отсортированный массив: {array}")