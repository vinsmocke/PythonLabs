import math

def vector_length(x1, y1, x2, y2):
    length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(length, 6)

x1 = int(input("Введіть координату x початку вектора: "))
y1 = int(input("Введіть координату y початку вектора: "))
x2 = int(input("Введіть координату x кінця вектора: "))
y2 = int(input("Введіть координату y кінця вектора: "))

result = vector_length(x1, y1, x2, y2)
print("Довжина вектора:", result)
