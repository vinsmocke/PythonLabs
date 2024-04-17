MOD = 12345

def count_sequences(n):
    a_prev, b_prev = 1, 1
    for i in range(2, n + 1):
        a_curr = (a_prev + b_prev) % MOD
        b_curr = a_prev
        a_prev, b_prev = a_curr, b_curr
    return (a_prev + b_prev) % MOD

n = int(input("Введіть довжину послідовності n: "))
result = count_sequences(n)
print("Кількість шуканих послідовностей:", result)
