import whois

def lookup(domain):

    print("\n[WHOIS INFO]")

    w = whois.whois(domain)

    print("Registrar:", w.registrar)
    print("Creation Date:", w.creation_date)
    print("Expiration Date:", w.expiration_date)
