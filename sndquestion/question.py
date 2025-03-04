a = int(input("Введите длину первого катета (см): "))
b = int(input("Введите длину второго катета (см): "))
c = (a * a + b * b) ** 0.5
perimetr = c + a + b
ploshad = a * b / 2
print(f"Гипотенуза = {c:.0f}")
print(f"Периметр = {perimetr:.0f}")
print(f"Площадь = {ploshad:.0f}" )