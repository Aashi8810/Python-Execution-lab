def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_primes(start: int, end: int) -> int:
    count = 0
    for n in range(start, end):
        if is_prime(n):
            count += 1
    return count
