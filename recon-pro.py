import os
import time
import json
import requests
import whois
import socket
import nmap
from bs4 import BeautifulSoup
import subprocess
import base64
import platform
import ssl

def print_ascii_art():
    print("""
██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗    ██████╗ ██████╗  ██████╗ 
██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║    ██╔══██╗██╔══██╗██╔═══██╗
██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║    ██████╔╝██████╔╝██║   ██║
██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║    ██╔═══╝ ██╔══██╗██║   ██║
██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║    ██║     ██║  ██║╚██████╔╝
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ 
    """)

def check_requirements():
    print("[+] Checking requirements...")
    time.sleep(2)

def subdomain_bruteforce(domain):
    print(f"[+] Brute forcing subdomains for {domain} using Sublist3r...")
    wordlist = '/usr/share/wordlists/dirb/common.txt'
    if os.path.exists(wordlist):
        try:
            subprocess.run(["sublist3r", "-d", domain, "-o", "subdomains.txt"])
        except Exception as e:
            print(f"Error during subdomain brute forcing: {e}")
    else:
        print("[+] Error: Wordlist not found!")
    return "subdomains.txt"

def fetch_robots_txt(domain):
    print(f"[+] Fetching robots.txt for {domain}...")
    try:
        robots_url = f"http://{domain}/robots.txt"
        response = requests.get(robots_url)
        if response.status_code == 200:
            return response.text
        else:
            return "robots.txt not found"
    except requests.exceptions.RequestException:
        return "robots.txt not found"

def fetch_sitemap(domain):
    print(f"[+] Fetching sitemap.xml for {domain}...")
    try:
        sitemap_url = f"http://{domain}/sitemap.xml"
        response = requests.get(sitemap_url)
        if response.status_code == 200:
            return response.text
        else:
            return "sitemap.xml not found"
    except requests.exceptions.RequestException:
        return "sitemap.xml not found"

def ssl_certificate_info(domain):
    print(f"[+] Getting SSL/TLS Certificate Information for {domain}...")
    try:
        # Connect to the domain using SSL/TLS and retrieve the certificate
        conn = ssl.create_connection((domain, 443))
        context = ssl.create_default_context()
        ssl_sock = context.wrap_socket(conn, server_hostname=domain)
        ssl_info = ssl_sock.getpeercert()
        
        return ssl_info
    except Exception as e:
        return f"Error fetching SSL certificate: {e}"

def port_scan(domain):
    print(f"[+] Scanning ports for {domain}...")
    scanner = nmap.PortScanner()
    try:
        scanner.scan(domain, '1-1024')
        return scanner[domain]['tcp']
    except Exception as e:
        return f"Error during port scanning: {e}"

def fetch_http_headers(domain):
    print(f"[+] Fetching HTTP Headers for {domain}...")
    try:
        response = requests.get(f'http://{domain}')
        return dict(response.headers)
    except requests.exceptions.RequestException as e:
        return f"Error fetching HTTP headers: {e}"

def whois_info(domain):
    print(f"[+] Fetching Whois Information for {domain}...")
    try:
        domain_info = whois.whois(domain)
        return domain_info
    except Exception as e:
        return f"Error fetching WHOIS information: {e}"

def check_http_methods(domain):
    print(f"[+] Checking HTTP Methods for {domain}...")
    try:
        response = requests.options(f'http://{domain}')
        return response.headers.get('allow', 'No methods found')
    except requests.exceptions.RequestException as e:
        return f"Error checking HTTP methods: {e}"

def dns_lookup(domain):
    print(f"[+] Performing DNS Lookup for {domain}...")
    try:
        result = socket.gethostbyname(domain)
        return result
    except socket.gaierror:
        return "DNS lookup failed"

def extract_page_title(domain):
    print(f"[+] Extracting page title for {domain}...")
    try:
        response = requests.get(f'http://{domain}')
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No title found"
        return title
    except requests.exceptions.RequestException as e:
        return f"Error extracting page title: {e}"

def server_fingerprinting(domain):
    print(f"[+] Performing server fingerprinting for {domain}...")
    try:
        response = requests.get(f'http://{domain}')
        return response.headers.get('server', 'No server info found')
    except requests.exceptions.RequestException as e:
        return f"Error performing server fingerprinting: {e}"

def ping_test(domain):
    print(f"[+] Performing Ping Test for {domain}...")
    response = os.system(f"ping -c 1 {domain}")
    if response == 0:
        return f"{domain} is reachable"
    else:
        return f"{domain} is not reachable"

def generate_report(domain, report_data):
    print("[+] Generating report...")
    try:
        with open(f"{domain}_pentest_report.json", 'w') as json_file:
            json.dump(report_data, json_file, indent=4)
        print(f"[+] Report saved as {domain}_pentest_report.json")
    except Exception as e:
        print(f"Error generating report: {e}")

def main():
    print_ascii_art()
    check_requirements()
    domain = input("[+] Enter the domain to test: ")

    report_data = {}

    report_data['domain'] = domain

    report_data['subdomain_bruteforce'] = subdomain_bruteforce(domain)
    report_data['robots_txt'] = fetch_robots_txt(domain)
    report_data['sitemap'] = fetch_sitemap(domain)
    report_data['ssl_certificate_info'] = ssl_certificate_info(domain)
    report_data['open_ports'] = port_scan(domain)
    report_data['http_headers'] = fetch_http_headers(domain)
    report_data['whois_info'] = whois_info(domain)
    report_data['http_methods'] = check_http_methods(domain)
    report_data['dns_lookup'] = dns_lookup(domain)
    report_data['page_title'] = extract_page_title(domain)
    report_data['server_fingerprinting'] = server_fingerprinting(domain)
    report_data['ping_test'] = ping_test(domain)

    generate_report(domain, report_data)

if __name__ == "__main__":
    main()
