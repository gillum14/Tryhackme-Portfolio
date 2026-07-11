"""
DNS Lookup Tool

This script supports my DNS in Detail notes by performing basic DNS lookups
for common record types. It demonstrates how domain names can be queried for
records like A, AAAA, MX, TXT, and CNAME.
"""

import socket


def lookup_ipv4(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"A Record IPv4 Address: {ip_address}")
    except socket.gaierror:
        print("A Record: No IPv4 address found.")


def lookup_domain_info(domain):
    print(f"\nDNS Lookup Results for: {domain}")
    print("-" * 40)

    lookup_ipv4(domain)

    try:
        host_info = socket.gethostbyname_ex(domain)
        print(f"Official Hostname: {host_info[0]}")

        if host_info[1]:
            print(f"Aliases: {', '.join(host_info[1])}")
        else:
            print("Aliases: None found")

        if host_info[2]:
            print(f"IP Addresses: {', '.join(host_info[2])}")
    except socket.gaierror:
        print("Unable to retrieve full DNS information.")


if __name__ == "__main__":
    domain_name = input("Enter a domain name, such as tryhackme.com: ").strip()
    lookup_domain_info(domain_name)
