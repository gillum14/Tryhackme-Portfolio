# Extending Your Network

## Learning Objectives:
~ Understand port forwarding and its purpose.
~ Learn the role of firewalls in network security.
~ Understand VPNs and their benefits.
~ Differentiate between routers and switches.
~ Learn how VLANs improve network segmentation.

---

## Notes:

### Port Forwarding
Port forwarding allows devices outside of a local network to access internal services (such as a web server).
- Configured on a **router**
- Maps incoming traffic from a public IP address to a private device
- Commonly used to host websites, game servers, or remote services

> **Port Forwarding vs Firewall**
> - **Port Forwarding** opens a path to a device.
> - **Firewalls** decide whether traffic is allowed through that path.

---

### Firewalls
A firewall monitors and filters network traffic entering and leaving a network.

Firewalls can filter traffic based on:
- Source or destination IP address
- Port number
- Protocol (TCP/UDP)

#### Firewall Types
| **Stateful** | Monitors the entire connection and makes dynamic decisions. More secure but uses more resources. |
| **Stateless** | Evaluates each packet independently using predefined rules. Faster but less intelligent. |

---

### Virtual Private Network (VPN)
A **VPN (Virtual Private Network)** creates an encrypted tunnel between devices over the Internet.

Benefits include:
- Secure communication between remote networks
- Encrypts network traffic
- Improves privacy and anonymity
- Protects data on public Wi-Fi

#### Common VPN Technologies

| Technology | Description |
|------------|-------------|
| **PPP** | Provides authentication and encryption. |
| **PPTP** | Easy to configure but offers weaker encryption. |
| **IPSec** | Strong encryption but more complex to configure. |

---

### Routers

Routers connect different networks and forward packets between them.
They operate at **Layer 3 (Network Layer)** of the OSI model.

Routers determine the best path based on factors such as:
- Shortest route
- Most reliable route
- Fastest connection

Routers commonly manage:
- Routing
- Port forwarding
- Firewall rules

---

### Switches

Switches connect multiple devices within the same network.
- **Layer 2 Switches** forward frames using **MAC addresses**.
- **Layer 3 Switches** can also route packets using **IP addresses**, providing some router functionality.

---

### VLANs (Virtual Local Area Networks)
A **VLAN** logically separates devices on the same physical network.

Benefits include:
- Improved security
- Reduced unnecessary network traffic
- Better organization of network resources

Example:
Different departments (Sales, Accounting, HR) can share the same switch while remaining isolated from one another.

---

## Lab

### Firewall Challenge
Configured a firewall to block malicious traffic on **port 80** while allowing legitimate traffic to reach the web server.

**Skills practiced:**
- Firewall rule configuration
- Traffic filtering
- Port-based security

---

### Network Simulator
Used the network simulator to observe how packets travel between devices and completed the TCP packet routing challenge.

**Skills practiced:**
- Packet routing
- Router and switch behavior
- TCP communication

---

## Conclusion -  Learned port forwarding, firewalls, VPNs, routers, switches, and VLANs all play important roles in building secure and efficient networks. Understanding how these technologies work together provides a strong foundation for network administration, troubleshooting, and cybersecurity.
