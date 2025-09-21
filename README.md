# Dell Laser Printer - Unauthenticated Access Scanner

**Author:** Farish  
**Language:** Python 3  
**Purpose:** Scan Dell Laser Printers for unauthenticated access and exposed security pages.

---

## Usage

```bash
# Run against an IP or URL
python3 dell_laser_printer.py 192.168.1.100
python3 dell_laser_printer.py https://192.168.1.4

#Output 
[+] Dell Laser Printer detected at http://152.1.72.46
    Printer version: B2360dn
    [+] Application is vulnerable for authentication bypass!


