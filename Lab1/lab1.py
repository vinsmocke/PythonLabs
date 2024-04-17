def time_to_eat_cake(t1, t2, t3):
    total_time = 1 / t1 + 1 / t2 + 1 / t3
    return round(1 / total_time, 2)

# Зчитуємо значення t1, t2, t3 з вхідного рядка
t1, t2, t3 = map(int, input().split())

# Обчислюємо час, за який гості зможуть з'їсти пиріг
result = time_to_eat_cake(t1, t2, t3)

# Виводимо результат
print(f"Час, небхідний для з’їдання пирога: {result} годин")
