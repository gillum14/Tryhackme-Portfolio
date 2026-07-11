"""
Network Basics Tool

This script supports my What is Networking notes by demonstrating basic
networking concepts such as IP addresses, private vs public networks,
IPv4, IPv6, MAC addresses, and ping.
"""

import ipaddress
import platform
import subprocess


def inspect_ip_address(ip_input):
    try:
        ip = ipaddress.ip_address(ip_input)

        print(f"\nIP Address: {ip}")
        print(f"IP Version: IPv{ip.version}")
        print(f"Private Address: {ip.is_private}")
        print(f"Public Address: {not ip.is_private}")
        print(f"Loopback Address: {ip.is_loopback}")
        print(f"Multicast Address: {ip.is_multicast}")

    except ValueError:
        print("\nInvalid IP address format.")


def explain_mac_address():
    print("\nMAC Address")
    print("-" * 40)
    print("A MAC address is a unique hardware address assigned to a network interface.")
    print("MAC spoofing occurs when a device pretends to use another device's MAC address.")


def ping_host(host):
    print(f"\nPinging {host}")
    print("-" * 40)

    system_name = platform.system().lower()

    if system_name == "windows":
        command = ["ping", "-n", "4", host]
    else:
        command = ["ping", "-c", "4", host]

    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=10)
        print(result.stdout)

        if result.returncode == 0:
            print("Ping result: Host responded.")
        else:
            print("Ping result: Host did not respond successfully.")
    except subprocess.TimeoutExpired:
        print("Ping timed out.")
    except FileNotFoundError:
        print("Ping command was not found on this system.")


if __name__ == "__main__":
    print("Network Basics Tool")
    print("=" * 40)

    ip_input = input("Enter an IP address to inspect, such as 192.168.1.1: ").strip()
    inspect_ip_address(ip_input)

    explain_mac_address()

    host_input = input("\nEnter a host to ping, such as example.com, or press Enter to skip: ").strip()

    if host_input:
        ping_host(host_input)
    else:
        print("Ping skipped.")
