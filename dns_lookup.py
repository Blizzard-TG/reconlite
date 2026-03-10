import socket

def lookup(domain):

    print("\n[DNS LOOKUP]")

    try:
        ip = socket.gethostbyname(domain)
        print("Domain:", domain)
        print("IP:", ip)

    except:
        print("DNS resolution failed")
