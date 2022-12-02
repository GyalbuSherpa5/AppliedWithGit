uin = "The quick brown fox jumps over the lazy dog"
uin = uin.lower()

vowel = "aeiou"

count = 0

for i in uin:
    if i in vowel:
        count += 1

print(count)


def isPrime(val):
    if val < 2:
        return False

    temp = 2

    while temp * temp <= val:
        if val % temp == 0:
            return False
        temp += 1

    return True


print(isPrime(count))

