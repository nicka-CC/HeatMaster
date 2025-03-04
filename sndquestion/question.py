while True:
    try:
        a = int(input("Введите длину первого катета (см): "))
        if a > 0:
            break
        else:
            print("Ошибка: Длина катета должна быть положительным числом.")
    except ValueError:
        print("Ошибка: Пожалуйста, введите целое число.")

while True:
    try:
        b = int(input("Введите длину второго катета      (см): ")) > 0
        if b > 0:
            break
        else:
            print("Ошибка: Длина катета должна быть положительным числом.")
    except ValueError:
        print("Ошибка: Пожалуйста, введите целое число.")
# a = int(input("Введите длину первого катета (см): "))
# b = int(input("Введите длину второго катета (см): "))

c = (a * a + b * b) ** 0.5
perimetr = c + a + b
ploshad = a * b / 2

print(f"Гипотенуза = {c:.0f}")
print(f"Периметр = {perimetr:.0f}")
print(f"Площадь = {ploshad:.0f}" )