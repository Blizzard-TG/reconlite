import socket

def scan(target):

    print("\n[PORT SCAN]")

    ports = [21,22,25,53,80,110,139,143,443,445,3306]

    for port in ports:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} OPEN")

        sock.close()
