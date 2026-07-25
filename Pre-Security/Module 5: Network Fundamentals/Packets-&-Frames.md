Learning Objectives:
~ Understand the difference between packets and frames.
~ Understand how encapsulation works in network communication.
~ Learn the differences between TCP and UDP.
~ Understand the purpose of ports and common protocols.

---

Notes:
Packets vs Frames
Packets and frames are pieces of data used during network communication. They operate at different layers of the OSI model.
| Frame | Layer 2 - Data Link | Uses MAC addresses for local network communication |
| Packet | Layer 3 - Network | Uses IP addresses for routing data between networks |

**Encapsulation** is the process of adding information to data as it moves through the OSI model.

---

TCP (Transmission Control Protocol)

TCP is a **connection-based protocol** that prioritizes reliable communication.

TCP provides:
- Guaranteed delivery
- Error checking
- Packet ordering
- Data integrity

Common uses:
- Web browsing
- Email
- File transfers

### TCP Three-Way Handshake

TCP establishes communication using:
1. **SYN** - Client requests a connection.
2. **SYN/ACK** - Server acknowledges the request.
3. **ACK** - Client confirms the connection.

After the handshake, data transmission begins.
TCP connections are closed using a **FIN packet** to properly terminate communication.

---

# UDP (User Datagram Protocol)

UDP is a **connectionless protocol** that prioritizes speed over reliability.

UDP:
- Does not require a handshake.
- Does not guarantee delivery.
- Does not perform error checking.

Common uses:
- Video streaming
- Voice communication
- Device discovery

---

# TCP vs UDP

| TCP | UDP |
|---|---|
| Connection-based | Connectionless |
| Reliable delivery | No delivery guarantee |
| Slower | Faster |
| Error checking | No error checking |
| Used when accuracy matters | Used when speed matters |

---

# Ports
Ports are communication endpoints that allow devices to direct traffic to specific applications.

Port range:
0 - 65535


Common ports:
| Protocol | Port | Purpose |
|---|---|---|
| FTP | 21 | File transfer |
| SSH | 22 | Secure remote access |
| HTTP | 80 | Web traffic |
| HTTPS | 443 | Encrypted web traffic |
| SMB | 445 | File sharing |
| RDP | 3389 | Remote desktop |

---

** Completed lab to reassemble the TCP handshake sequence to understand how TCP establishes communication.

Skills practiced:
- TCP connection process
- SYN, SYN/ACK, and ACK packets

---

** Practical Challenge
Connected to:
IP Address: 8.8.8.8
Port: 1234
Retrieved the flag successfully.

---

Conclusion - Reviewed packets, frames, TCP, UDP, and ports are foundational networking concepts in cybersecurity. Obtained a better understanding how data is structured and transmitted helps security professionals analyze network traffic, troubleshoot communication issues, and investigate potential threats.
