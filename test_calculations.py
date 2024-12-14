import asyncio
import time

import config
from client import Client
from cpu_bound_functions import getPrime

primes_to_calculate = [
    2 * 10 ** 4,
    3 * 10 ** 4,
2 * 10 ** 4,
    3 * 10 ** 4,
2 * 10 ** 4,
    3 * 10 ** 4,
2 * 10 ** 4,
    3 * 10 ** 4,
2 * 10 ** 4,
    3 * 10 ** 4
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


async def testDistributedCalc():
    primes = []

    client = Client()

    primes_for_distributed = primes_to_calculate[:len(primes_to_calculate) // 2]
    primes_for_local = primes_to_calculate[len(primes_to_calculate) // 2:]

    start_time = time.time()

    threads = []
    for prime_for_distributed in primes_for_distributed:
        threads.append(client.sendPrimeToCalculate(prime_for_distributed, primes))

    for prime_for_local in primes_for_local:
        primes.append(getPrime(prime_for_local))

    # other unit was calculating the stuff behind the scenes while out machine was calculating its part so now just
    # have to wait till the other unit finishes its work
    for thread in threads:
        thread.join()

    end_time = time.time()
    time_spent = end_time - start_time

    print("Distributed time:", time_spent)
    print("Distributed output:", primes)

    return time_spent


def main():
    time_spent_synchronous = testSynchronousCalc()
    time_spent_distributed = asyncio.run(testDistributedCalc())
    print("Distributed calculation is", round(time_spent_synchronous / time_spent_distributed - 1, 2) * 100, "% faster than synchronous")


if __name__ == "__main__":
    main()


