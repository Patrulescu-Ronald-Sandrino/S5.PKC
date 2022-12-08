from typing import Tuple


def is_prime(n: int) -> bool:  # TODO: optimize
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    return all(n % i != 0 for i in range(3, int(n ** 0.5) + 1, 2))


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def generate_two_primes() -> Tuple[int, int]:  # TODO: optimize
    p = 17
    q = 11
    return p, q
