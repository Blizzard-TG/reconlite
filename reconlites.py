import argparse
import dns_lookup
import port_scan
import whois_lookup

parser = argparse.ArgumentParser(description="ReconLite Security Recon Tool")

parser.add_argument("-t", "--target", help="Target domain or IP")
parser.add_argument("--dns", action="store_true", help="DNS lookup")
parser.add_argument("--ports", action="store_true", help="Port scan")
parser.add_argument("--whois", action="store_true", help="WHOIS lookup")

args = parser.parse_args()

if args.dns:
    dns_lookup.lookup(args.target)

if args.ports:
    port_scan.scan(args.target)

if args.whois:
    whois_lookup.lookup(args.target)
