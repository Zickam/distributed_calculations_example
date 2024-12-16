import asyncio
import time

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
                      ] * 3

def testSynchronousCalc():
    primes = []

    start_time = time.time()

    for prime_to_calculate in primes_to_calculate:
        primes.append(getPrime(prime_to_calculate))

    end_time = time.time()
    time_spent = end_time - start_time

    print("Synchronous time:", time_spent, "seconds")
    print("Synchronous output:", primes, "amount:", len(primes))


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

    # other unit was calculating the stuff behind the scenes while our machine was calculating its part so now we just
    # have to wait the other unit to finish its work
    for thread in threads:
        thread.join()

    end_time = time.time()
    time_spent = end_time - start_time

    print("Distributed time:", time_spent, "seconds")
    print("Distributed output:", primes, "amount:", len(primes))


def main():
    testSynchronousCalc()
    asyncio.run(testDistributedCalc())


if __name__ == "__main__":
    main()


