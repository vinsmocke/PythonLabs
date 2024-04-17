from itertools import product

def generate_numbers(length):
    numbers = [''.join(num) for num in product('59', repeat=length)]
    return numbers

def main():
    length = int(input("Введіть довжину чисел (розрядів) (<30): "))
    if length > 0 and length < 30:
        numbers = generate_numbers(length)
        counter = 0
        for num in numbers:
            if num.find("999") != -1 or num.find("555") != -1:
                counter += 1
        print(f"кількість чисел із р розрядів {len(numbers)-counter}")
    else:
        print("Введіть додатне число або число менше 30.")


if __name__ == "__main__":
    main()