import socket
import threading
import time

import config


class Client(socket.socket):
    def __init__(self):
        super().__init__()
        self.connect((config.UNIT_IP, config.UNIT_PORT))

    def sendPrimeToCalculate(self, n: int, primes: list[int]):
        self.send(str(n).encode(encoding="utf-8"))
        threading.Thread(target=self.receive, args=(primes, )).start()

    def receive(self, primes: list[int]):
        while 1:
            data = self.recv(config.BUFF_SIZE)
            if data:
                num = int(data.decode("utf-8").strip())
                primes.append(num)
                return

            time.sleep(0.001)



