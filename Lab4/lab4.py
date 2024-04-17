def кількість_дільників(n):
    кількість = 0
    for m in range(1, n):
        if n % m == n // m:
            кількість += 1
    return кількість

n = int(input("Введіть натуральне число n: "))
if 1 < n < 150:
    print("Кількість рівних дільників числа", n, ":", кількість_дільників(n))
else:
    print("Введіть число n в межах від 1 до 150.")
