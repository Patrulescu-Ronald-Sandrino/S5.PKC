from enum import Enum
from functools import reduce

from Language import Language
from MultipleMeta import MultipleMeta
from utils import gcd, generate_two_primes, is_prime


# NOTICE!: in the lecture, e is found randomly
def find_e(φ: int) -> int:  # how to do this in a functional/stream manner?
    e = 1
    while True:
        e += 2
        if gcd(e, φ) == 1 and is_prime(e):
            return e


class LowercaseEnglishWithBlank(Language):
    def __init__(self):
        filler = '_'
        super().__init__(filler, [filler] + [chr(i) for i in range(ord('A'), ord('Z') + 1)])

    def _code(self, letter: str) -> int:
        try:
            return self._alphabet.index(letter)
        except ValueError:
            raise ValueError(f"letter '{letter}' is not in the alphabet {self._alphabet}")


class RSA(metaclass=MultipleMeta):
    # region constructors
    class Mode(Enum):
        encrypt = 1
        decrypt = 2

    def __init__(self, p: int, q: int):
        self.__p = p
        self.__q = q
        self.__n = p * q
        self.__φ = self.__n + 1 - (p + q)
        self.__e = find_e(self.__φ)
        self.__d = pow(self.__e, -1, self.__φ)

        self.__language: Language = LowercaseEnglishWithBlank()

    def __init__(self):
        self.__init__(*generate_two_primes())

    # endregion

    # region properties
    @property
    def n(self) -> int:
        return self.__n

    @property
    def e(self) -> int:
        return self.__e

    @property
    def d(self) -> int:
        return self.__d

    @property
    def φ(self):
        return self.__φ
    # endregion

    def __encrypt(self, m: int) -> int:
        return pow(m, self.e, self.n)

    def __decrypt(self, c: int) -> int:
        return pow(c, self.__d, self.n)

    def encrypt(self, plaintext: str, k: int, l: int) -> str:
        if not (27 ** k < self.n < 27 ** l):
            raise ValueError(f'k={k} and l={l} are invalid for n={self.n}')

        print(f"plaintext: {plaintext}")
        blocks = self.__language.split_plaintext(plaintext, k)
        print(f"blocks of {k} letters: {blocks}")
        converted_blocks = [self.__language.block_to_number(block) for block in blocks]
        print(f"numerical equivalents: {converted_blocks}")
        encrypted_blocks = [self.__encrypt(number) for number in converted_blocks]
        print()

        print(f"encryption:")
        print(f"values: {encrypted_blocks}")
        cipher_blocks = [self.__language.number_to_block(block, l) for block in encrypted_blocks]
        print(f"blocks of {l} letters: {cipher_blocks}")
        ciphertext = reduce(lambda x, y: x + y, cipher_blocks)
        print()

        return ciphertext

    def decrypt(self, ciphertext: str, k: int, l: int) -> str:
        if not (27 ** k < self.n < 27 ** l):
            raise ValueError(f'k={k} and l={l} are invalid for n={self.n}')

        print(f"ciphertext: {ciphertext}")
        blocks = self.__language.split_plaintext(ciphertext, l)
        print(f"blocks of {l} letters: {blocks}")
        converted_blocks = [self.__language.block_to_number(block) for block in blocks]
        print(f"numerical equivalents: {converted_blocks}")
        decrypted_blocks = [self.__decrypt(number) for number in converted_blocks]
        print()

        print(f"decryption:")
        print(f"values: {decrypted_blocks}")
        plain_blocks = [self.__language.number_to_block(block, k) for block in decrypted_blocks]
        print(f"blocks of {k} letters: {plain_blocks}")
        plaintext = reduce(lambda x, y: x + y, plain_blocks)
        print()

        return plaintext
