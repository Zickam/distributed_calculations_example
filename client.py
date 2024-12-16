import threading

import config

import requests

url = f"http://{config.UNIT_IP}:{config.UNIT_PORT}"

class Client:
    def _send(self, n: int, primes: list[int]):
        resp = requests.get(url, params={"num": n})
        primes.append(int(resp.json()["prime"]))

    def sendPrimeToCalculate(self, n: int, primes: list[int]):
        thread = threading.Thread(target=self._send, args=(n, primes, ))
        thread.start()
        return thread
