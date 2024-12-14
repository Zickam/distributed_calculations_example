import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind("0.0.0.0:9899")
    while 1:
        

if __name__ == "__main__":
    main()