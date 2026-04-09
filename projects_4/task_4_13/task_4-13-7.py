
print("Среднее арифметическое всех элементов массива")
print("-" * 50)

array = list(map(float, input("Введите элементы массива через пробел: ").split()))

if len(array) == 0:
    print("Ошибка: массив не должен быть пустым!")
else:

    total = 0
    for num in array:
        total += num
    

    average = total / len(array)
    
    print("-" * 50)
    print(f"Массив: {array}")
    print(f"Сумма элементов: {total}")
    print(f"Количество элементов: {len(array)}")
    print(f"Среднее арифметическое: {average}")