print("Поиск максимального из N чисел")
print("-" * 40)

n = int(input("Сколько чисел вы хотите ввести? "))

if n < 1:
    print("Ошибка: количество чисел должно быть больше 0!")
else:
    max_num = float(input("Введите число 1: "))
    
    for i in range(2, n + 1):
        num = float(input(f"Введите число {i}: "))
        if num > max_num:
            max_num = num
    
    print("-" * 40)
    print(f"Максимальное число: {max_num}")