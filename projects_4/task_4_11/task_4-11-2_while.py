
print("Скалярное произведение двух векторов")
print("-" * 40)

vector1 = list(map(float, input("Введите первый вектор (числа через пробел): ").split()))

vector2 = list(map(float, input("Введите второй вектор (числа через пробел): ").split()))

if len(vector1) != len(vector2):
    print("Ошибка: векторы должны иметь одинаковую длину!")
else:

    scalar_product = 0
    i = 0
    n = len(vector1)
    
    print("\nВычисление:")
    while i < n:
        product = vector1[i] * vector2[i]
        scalar_product += product
        print(f"{vector1[i]} × {vector2[i]} = {product} | Текущая сумма: {scalar_product}")
        i += 1
    
    print("-" * 40)
    print(f"Скалярное произведение векторов: {scalar_product}")