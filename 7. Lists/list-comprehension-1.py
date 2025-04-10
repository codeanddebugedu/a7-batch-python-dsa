def check_prime(num: int) -> bool:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


result = [i for i in range(1, 101) if check_prime(i)]
print(result)
