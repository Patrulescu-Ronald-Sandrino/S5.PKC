from abc import ABCMeta, abstractmethod
from typing import List


class Language(metaclass=ABCMeta):
    def __init__(self, filler: str, alphabet: List[str]):
        self._filler: str = filler
        self._alphabet: List[str] = alphabet

    def __len__(self) -> int:
        return len(self._alphabet)

    @abstractmethod
    def _code(self, letter) -> int:
        pass

    def split_plaintext(self, message, k):
        blocks = [message[i:i + k] for i in range(0, len(message), k)]
        blocks[-1] += self._filler * (k - len(blocks[-1]))

        return blocks

    def block_to_number(self, block: str) -> int:
        return sum(self._code(c) * pow(len(self), len(block) - i - 1) for i, c in enumerate(block))

    def number_to_block(self, block: int, l: int) -> str:
        codes = []

        while block > 0:
            codes.append(block % len(self))
            block //= len(self)

        padding = self._filler * (l - len(codes))

        return padding + ''.join(self._alphabet[code] for code in reversed(codes))
