import socket

import config
from config import UNIT_PORT
from cpu_bound_functions import getPrime


def main():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("0.0.0.0", UNIT_PORT))

        print("Listening for new clients...")

        while 1:
            sock.listen()
            accepted_sock, addr = sock.accept()

            numbers = []

            while 1:
                data = accepted_sock.recv(config.BUFF_SIZE)
                if data:
                    num = int(data.decode("utf-8").strip())
                    if num == config.END_SYMBOL:
                        break
                    numbers.append(num)

            for num in numbers:
                calculated_prime = getPrime(num)
                accepted_sock.send(str(calculated_prime).encode("utf-8"))
                print(f"Calculated prime (n: {num}):", calculated_prime)

            accepted_sock.close()

    except Exception as ex:
        raise ex
    finally:
        sock.close()


if __name__ == "__main__":
    main()