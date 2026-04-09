print("Поиск минимального из четырёх чисел")
print("-" * 40)

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
d = float(input("Введите четвёртое число: "))

min_num = a

if b < min_num:
    min_num = b
if c < min_num:
    min_num = c
if d < min_num:
    min_num = d

print("-" * 40)
print(f"Минимальное число: {min_num}")