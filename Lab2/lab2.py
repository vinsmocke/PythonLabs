from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def least_common_multiple(numbers):
    lcm_result = numbers[0]
    for num in numbers[1:]:
        lcm_result = lcm(lcm_result, num)
    return lcm_result

n = int(input())
numbers = list(map(int, input().split()))

result = least_common_multiple(numbers)
print(f"Result: {result}")
