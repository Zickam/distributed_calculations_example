import socket

import config
from cpu_bound_functions import getPrime


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(config.UNIT_ADDRESS)

    while 1:
        sock.listen()
        accepted_sock, addr = sock.accept()

        while 1:
            data = accepted_sock.recv(config.BUFF_SIZE)
            if data:
                break

        num = int(data.decode("utf-8").strip())

        calculated_prime = getPrime(num)

        accepted_sock.send(str(calculated_prime).encode("utf-8"))
        print(f"Calculated prime (n: {num}):", calculated_prime)

    sock.close()


if __name__ == "__main__":
    main()