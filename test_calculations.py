import time

from client import Client
from cpu_bound_functions import getPrime

primes_to_calculate = [
    2 * 10 ** 5,
    3 * 10 ** 5
]

def testSynchronousCalc():
    primes = []

    start_time = time.time()

    for prime_to_calculate in primes_to_calculate:
        primes.append(getPrime(prime_to_calculate))

    end_time = time.time()
    time_spent = end_time - start_time

    print("Synchronous time:", time_spent)
    print("Synchronous output:", primes)

    return time_spent


def testDistributedCalc():
    primes = []

    client = Client()

    primes_for_distributed = primes_to_calculate[:len(primes_to_calculate) // 2]
    primes_for_local = primes_to_calculate[len(primes_to_calculate) // 2:]

    start_time = time.time()

    for prime_for_distributed in primes_for_distributed:
        client.sendPrimeToCalculate(prime_for_distributed, primes)

    for prime_for_local in primes_for_local:
        primes.append(getPrime(prime_for_local))

    end_time = time.time()
    time_spent = end_time - start_time

    print("Distributed time:", time_spent)
    print("Distributed output:", primes)

    return time_spent


def main():
    # time_spent = testSynchronousCalc()
    time_spent = testDistributedCalc()


if __name__ == "__main__":
    main()


