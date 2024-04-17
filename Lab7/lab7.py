import math

def intersection_points():
    x1, y1, r1 = map(float, input("Введіть координати та радіус першого кола (x1, y1, r1): ").split())
    x2, y2, r2 = map(float, input("Введіть координати та радіус другого кола (x2, y2, r2): ").split())

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    sum_of_radii = r1 + r2
    diff_of_radii = abs(r1 - r2)

    if distance == 0 and r1 == r2:
        return -1
    elif distance > sum_of_radii:
        return 0
    elif distance == sum_of_radii:
        return 1
    elif distance < sum_of_radii and distance > diff_of_radii:
        return 2
    elif distance == diff_of_radii:
        return 1
    elif distance < diff_of_radii:
        return 0

result = intersection_points()
print("Кількість точок перетину:", result)
