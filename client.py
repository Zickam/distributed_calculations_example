import threading
import uuid

import config

import requests

url = f"http://{config.UNIT_IP}:{config.UNIT_PORT}"
url_factorial = f"http://{config.UNIT_IP}:{config.UNIT_PORT}/factorial"

class Client:
    def _send(self, n: int, primes: list[int]):
        resp = requests.get(url, params={"num": n})
        primes.append(int(resp.json()["prime"]))

    def sendPrimeToCalculate(self, n: int, primes: list[int]):
        thread = threading.Thread(target=self._send, args=(n, primes, ))
        thread.start()
        return thread

    def _sendFactorial(self, n: int, factorials: list[int]):
        resp = requests.get(url_factorial, params={"num": n})
        with open(f"tmp_distributed/fact_{uuid.uuid4()}.txt", "w") as file:
            fact = resp.json()["factorial"]
            factorials.append(fact)
            file.write(str(fact))
            file.write("\n")

    def sendFactorialToCalculate(self, n: int, primes: list[int]):
        thread = threading.Thread(target=self._sendFactorial, args=(n, primes,))
        thread.start()
        return thread
