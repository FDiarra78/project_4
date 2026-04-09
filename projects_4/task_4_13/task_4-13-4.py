# S = 1 + 2 + 3 + ... + N

print("Сумма первых N натуральных чисел")
print("-" * 40)

n = int(input("Введите целое положительное число N: "))

if n < 1:
    print("Ошибка: N должно быть больше 0!")
else:
    total = 0
    for i in range(1, n + 1):
        total += i
    
    print("-" * 40)
    print(f"Сумма чисел от 1 до {n}: {total}")