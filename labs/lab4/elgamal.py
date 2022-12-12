import random
import string
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

ALPHABET = "_" + string.ascii_uppercase
K = 300


class ElGamal:

    def __init__(self):
        self.__p = 0
        self.__g = 0
        self.__x = 0  # private key
        self.__y = 0  # public key

    def generate(self, bits):
        # Generate a safe prime p
        self.__p = getPrime(bits)

        # Generate generator g
        while 1:
            # Choose a square residue; it will generate a cyclic group of order q.
            self.__g = pow(random.randrange(2, self.__p), 2, self.__p)

            if self.__g in (1, 2):
                continue

            if (self.__p - 1) % self.__g == 0:
                continue

            ginv = pow(self.__g, -1, self.__p)
            if (self.__p - 1) % ginv == 0:
                continue

            # Found
            break

        # Generate private key x
        self.__x = random.randrange(2, self.__p - 1)
        # Generate public key y
        self.__y = pow(self.__g, self.__x, self.__p)

    def encrypt(self, message: bytes, K):
        for l in message.decode():
            if l not in ALPHABET:
                print("Letter not found in alphabet!")
                exit(1)
        a = pow(self.__g, K, self.__p)
        b = (pow(self.__y, K, self.__p) * bytes_to_long(message)) % self.__p
        return [int(a), int(b)]

    def decrypt(self, message):
        if len(message) != 2:
            print("Wrong message provided!")
            exit(1)
        message = (pow(message[0], -self.__x, self.__p) * message[1]) % self.__p
        for l in long_to_bytes(message).decode():
            if l not in ALPHABET:
                print("Letter not found in alphabet!")
                exit(1)
        return int(message)

    def get_private_key(self):
        return self.__x

    def get_public_key(self):
        return self.__y


bits_amount = int(input("Amount bits of security: "))
message_to_encode = input("Message: ").encode()

elGamal = ElGamal()
elGamal.generate(256)

print(f"Private key: {elGamal.get_private_key()}")
print(f"Public key: {elGamal.get_public_key()}")

encrypted = elGamal.encrypt(message_to_encode, K)
decrypted = elGamal.decrypt(encrypted)
print(f"{encrypted=}")
print(f"{decrypted=}")
print(f"decrypted message: {long_to_bytes(decrypted)}")
assert message_to_encode == long_to_bytes(decrypted)

print("All tests ran successfully")
