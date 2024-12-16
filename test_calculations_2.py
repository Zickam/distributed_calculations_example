import os
import asyncio
import time

from client import Client
from cpu_bound_functions import getPrime, factorial

factorials_to_calc = [
                          10 ** 5,
    2 * 10 ** 5,
    # 3 * 10 ** 5,
    # 4 * 10 ** 5
                      ]

def testSynchronousCalc():
    factorials = []

    start_time = time.time()

    with open("tmp_sync/fact_1.txt", "w") as file:
        for fact in factorials_to_calc:
            num = factorial(fact)
            factorials.append(num)
            file.write(str(num))
            file.write("\n")

    end_time = time.time()
    time_spent = end_time - start_time

    print("Synchronous time:", time_spent, "seconds")
    print("Synchronous output amount:", len(factorials))


async def testDistributedCalc():
    factorials = []

    client = Client()

    factorials_for_distributed = factorials_to_calc[:len(factorials_to_calc) // 2]
    factorials_for_local = factorials_to_calc[len(factorials_to_calc) // 2:]

    start_time = time.time()

    threads = []
    for prime_for_distributed in factorials_for_distributed:
        threads.append(client.sendFactorialToCalculate(prime_for_distributed, factorials))

    with open("tmp_distributed/fact_1.txt", "w") as file:
        for fact in factorials_for_local:
            num = factorial(fact)
            factorials.append(num)
            file.write(str(num))
            file.write("\n")


    # other unit was calculating the stuff behind the scenes while our machine was calculating its part so now we just
    # have to wait the other unit to finish its work
    for thread in threads:
        thread.join()

    end_time = time.time()
    time_spent = end_time - start_time

    print("Distributed time:", time_spent, "seconds")
    print("Distributed output amount:", len(factorials))


def main():
    os.system("rm -rf tmp_distributed")
    os.mkdir("tmp_distributed")
    os.system("rm -rf tmp_sync")
    os.mkdir("tmp_sync")
    testSynchronousCalc()
    asyncio.run(testDistributedCalc())


if __name__ == "__main__":
    main()


