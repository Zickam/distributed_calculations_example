def isPrime(num: int) -> bool:
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for _i in range(3, int(num ** 0.5) + 1, 2):
        if num % _i == 0:
            return False
    return True

def getPrime(n: int) -> list[int]:
    primes_count = 0
    i = 3
    last_prime = 2
    while primes_count < n:
        if isPrime(i):
            primes_count += 1
            last_prime = i
        i += 1
    return last_prime

def getPrimes(n: int) -> list[int]:
    primes = []
    i = 2
    while len(primes) < n:
        if isPrime(i):
            primes.append(i)
        i += 1
    return primes


if __name__ == "__main__":
    # for i in range(200):
    #     print(getPrime(i))
    print(getPrime(200000))