WHOIS Lookup

Install dependency:

pip install python-whois


Run the Tool
python reconlite.py -t example.com --dns --ports --whois

Output:

[DNS LOOKUP]
Domain: example.com
IP: 93.184.216.34

[PORT SCAN]
Port 80 OPEN
Port 443 OPEN


Once this works, the next evolution would be turning it into a single executable CLI tool so someone could simply type:

reconlite example.com --full

and the tool performs every reconnaissance step automatically.
