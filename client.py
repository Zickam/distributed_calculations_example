import threading

import config

import requests

url = f"http://{config.UNIT_IP}:{config.UNIT_PORT}"
url_primes = f"http://{config.UNIT_IP}:{config.UNIT_PORT}/primes"

class Client:
    def _send(self, n: int, primes: list[int]):
        resp = requests.get(url, params={"num": n})
        primes.append(int(resp.json()["prime"]))

    def sendPrimeToCalculate(self, n: int, primes: list[int]):
        thread = threading.Thread(target=self._send, args=(n, primes, ))
        thread.start()
        return thread

    def _sendPrimes(self, n: int, primes: list[int]):
        resp = requests.get(url_primes, params={"num": n})
        for prime in resp.json()["primes"]:
            primes.append(prime)

    def sendPrimesToCalculate(self, n: int, primes: list[int]):
        thread = threading.Thread(target=self._sendPrimes, args=(n, primes,))
        thread.start()
        return thread
