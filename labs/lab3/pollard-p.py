from typing import Callable


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def is_prime(n: int):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# https://moodle.cs.ubbcluj.ro/pluginfile.php/46228/mod_resource/content/1/pkc-c04.pdf#page=12&zoom=150
def pollard_p(n: int, x0: int, f: Callable[[int], int] = lambda x: x ** 2 + 1):
    if is_prime(n):
        print(f"{n} is prime")
        return

    j = 1
    x_sequence = {0: x0}

    while True:
        x_sequence[j] = f(x_sequence[j - 1]) % n
        j += 1
        x_sequence[j] = f(x_sequence[j - 1]) % n

        # j is even
        d = gcd(abs(x_sequence[j] - x_sequence[j // 2]), n)

        print(f"x{j - 1} = {x_sequence[j - 1]}, x{j} = {x_sequence[j]}, (|x{j} - x{j // 2}|, n) = {d}")

        if 1 < d < n:
            return d

        j += 1


if __name__ == '__main__':
    n = 2
    x0 = 2
    f1 = pollard_p(n, x0, lambda x: x ** 2 + 1)
    if f1 is not None:
        print(f"{n} = {f1} * {n // f1}")
