```console

                ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗    ██████╗ ██████╗  ██████╗ 
                ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║    ██╔══██╗██╔══██╗██╔═══██╗
                ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║    ██████╔╝██████╔╝██║   ██║
                ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║    ██╔═══╝ ██╔══██╗██║   ██║
                ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║    ██║     ██║  ██║╚██████╔╝
                ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝
                
                                                                        BY: n0tabdu11ah

```

# Pentest Automation Tool

## Overview
The Pentest Automation Tool is a Python-based utility designed to automate various penetration testing tasks for a given domain. It gathers a comprehensive set of information to help you understand the security posture of a target domain, including subdomain enumeration, SSL/TLS certificate details, port scanning, HTTP headers, and more.

---

## Features
- **Subdomain Bruteforce:** Uses Sublist3r to find subdomains.
- **Fetch Robots.txt:** Retrieves and displays the `robots.txt` file.
- **Fetch Sitemap.xml:** Retrieves and displays the `sitemap.xml` file.
- **SSL/TLS Certificate Info:** Fetches SSL/TLS certificate details for the domain.
- **Port Scanning:** Scans ports 1-1024 using Nmap.
- **HTTP Headers:** Fetches HTTP headers for the domain.
- **WHOIS Info:** Retrieves WHOIS information.
- **HTTP Methods:** Checks allowed HTTP methods.
- **DNS Lookup:** Resolves the domain to its IP address.
- **Page Title Extraction:** Extracts the page title of the domain's main page.
- **Server Fingerprinting:** Identifies the server type.
- **Ping Test:** Checks domain reachability.
- **Report Generation:** Saves all gathered data into a JSON report.

---

## Requirements
- Python 3.x
- Required Python modules: `requests`, `nmap`, `BeautifulSoup`, `whois`
- Tools: Sublist3r (installed and configured), Nmap

---

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/pentest-tool.git
cd pentest-tool
```
2. Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```

  - Ensure Sublist3r is installed and accessible in your PATH:
  
  ```bash
  git clone https://github.com/aboul3la/Sublist3r.git
  cd Sublist3r
  pip install -r requirements.txt
  ```

## Usage

1. Run the script:

```bash
python pentest_tool.py
```

2. Enter the domain to test when prompted.
3. The tool will perform a series of tests and generate a report.

## Output

The tool generates a JSON report containing all gathered information. The report is saved as `<domain>_pentest_report.json` in the working directory.

## Example

```console
██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗    ██████╗ ██████╗  ██████╗ 
██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║    ██╔══██╗██╔══██╗██╔═══██╗
██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║    ██████╔╝██████╔╝██║   ██║
██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║    ██╔═══╝ ██╔══██╗██║   ██║
██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║    ██║     ██║  ██║╚██████╔╝
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ 

[+] Enter the domain to test: example.com
[+] Brute forcing subdomains for example.com using Sublist3r...
[+] Fetching robots.txt for example.com...
[+] Fetching sitemap.xml for example.com...
[+] Getting SSL/TLS Certificate Information for example.com...
[+] Scanning ports for example.com...
...
[+] Report saved as example.com_pentest_report.json
```

## Dependencies

Python Modules:
- requests
- nmap
- BeautifulSoup
- whois
## Tools:
- Sublist3r
- Nmap

## Disclaimer

This tool is for educational purposes only. Ensure you have proper authorization before testing any domain.
