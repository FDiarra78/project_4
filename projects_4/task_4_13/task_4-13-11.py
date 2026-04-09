print("Среднее арифметическое элементов массива с чётными индексами")
print("-" * 50)


array = list(map(float, input("Введите элементы массива через пробел: ").split()))

if len(array) == 0:
    print("Ошибка: массив не должен быть пустым!")
else:
    
    sum_even_index = 0
    count_even_index = 0
    even_index_elements = []
    
    for i in range(len(array)):
        if i % 2 == 0: 
            sum_even_index += array[i]
            count_even_index += 1
            even_index_elements.append(array[i])
    
    average = sum_even_index / count_even_index
   
    print("-" * 50)
    print(f"Массив: {array}")
    print(f"Индексы: {list(range(len(array)))}")
    print(f"Элементы с чётными индексами: {even_index_elements}")
    print(f"Сумма: {sum_even_index}")
    print(f"Количество: {count_even_index}")
    print(f"Среднее арифметическое: {average}")