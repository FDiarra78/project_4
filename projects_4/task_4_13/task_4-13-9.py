print("Сумма всех нечётных элементов массива")
print("-" * 50)


array = list(map(int, input("Введите целые числа массива через пробел: ").split()))

sum_odd = 0
odd_elements = []

for num in array:
    if num % 2 != 0:  # Проверка на нечётность
        sum_odd += num
        odd_elements.append(num)

print("-" * 50)
print(f"Массив: {array}")
print(f"Нечётные элементы: {odd_elements}")
print(f"Сумма нечётных элементов: {sum_odd}")