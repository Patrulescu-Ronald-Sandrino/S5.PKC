from RSA import RSA

p = 31
q = 59
k = 2
l = 3
mode = RSA.Mode.decrypt
text = '_CI_SW_IX'


rsa = RSA(p, q)

print(f"p={p}, q={q}")
print()
print(f"values:")
print(f"n={rsa.n}, φ={rsa.φ}, e={rsa.e}", end='')
print(f", d={rsa.d}" if mode == RSA.Mode.decrypt else '')
print()
print()


def encrypt(plaintext):
    ciphertext = rsa.encrypt(plaintext, k, l)
    print(f"ciphertext: {ciphertext}")
    print()
    print()
    print(f"plaintext: {rsa.decrypt(ciphertext, k, l)}")


def decrypt(ciphertext):
    plaintext = rsa.decrypt(ciphertext, k, l)
    print(f"plaintext: {plaintext}")
    print()
    print()
    print(f"ciphertext: {rsa.encrypt(plaintext, k, l)}")


switcher = {
    RSA.Mode.encrypt: encrypt,
    RSA.Mode.decrypt: decrypt
}

switcher[mode](text)
