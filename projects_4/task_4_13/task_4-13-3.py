print("Вычисление факториала N!")
print("-" * 40)


n = int(input("Введите целое неотрицательное число N: "))


if n < 0:
    print("Ошибка: факториал определён только для неотрицательных чисел!")
else:
    
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    
   
    print("-" * 40)
    print(f"{n}! = {factorial}")