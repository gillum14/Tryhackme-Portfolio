OSI Model

Learning Objectives:
~ Understand the purpose and importance of the OSI (Open Systems Interconnection) model.
~ Learn the function of each of the seven OSI layers.
~ Understand how data moves through the OSI model using encapsulation.
~ Identify common protocols and devices associated with each layer.
~ Understand the differences between TCP and UDP at the Transport Layer.

---

Notes:
- The **OSI (Open Systems Interconnection) Model** is a networking framework that defines how devices communicate across a network.
- The model provides a standardized method for network communication, allowing devices with different hardware, operating systems, and designs to exchange information successfully.
- One of the main benefits of the OSI model is that it breaks networking communication into smaller, manageable layers. Each layer has specific responsibilities and works together to ensure data is properly transmitted, received, and interpreted.
- The OSI model consists of **seven layers**, organized from **Layer 7 (Application)** to **Layer 1 (Physical).**
Layer 7 - Application
Layer 6 - Presentation
Layer 5 - Session
Layer 4 - Transport
Layer 3 - Network
Layer 2 - Data Link
Layer 1 - Physical

---

Encapsulation:
As data moves through each layer of the OSI model, additional information is added to help with transmission.
This process is called **encapsulation**.
Each layer adds its own header or information before passing the data to the next layer.

---

Layer 1: Physical Layer

The Physical Layer is the lowest layer of the OSI model.

It focuses on the physical components involved in networking, including:
- Cables
- Electrical signals
- Hardware devices
- Wireless signals

Data is transmitted using binary values:
1s and 0s

This layer is responsible for physically moving bits between devices.

---

Layer 2: Data Link Layer

The Data Link Layer focuses on physical addressing and preparing data for transmission.

Responsibilities include:
- Adding MAC addresses
- Error detection
- Formatting data for transmission

Every network-enabled device contains a **Network Interface Card (NIC)** with a unique:
MAC addresses are assigned by manufacturers and are permanently stored on the network card.
Although MAC addresses cannot normally be changed, they can be spoofed.
The Data Link Layer uses MAC addresses to determine the physical destination of data.

---

Layer 3: Network Layer

The Network Layer is responsible for:
- Routing data
- Determining the best path for packets
- Reassembling data

This layer uses:
IP Addresses

Example:
192.168.1.100

Devices such as routers operate at this layer because they can forward packets using IP addresses.

These are known as:

Layer 3 Devices

## Routing Decisions

Routers consider factors such as:
- Shortest path
- Most reliable path
- Fastest connection type

Common routing protocols include:
- OSPF (Open Shortest Path First)
- RIP (Routing Information Protocol)

---

# Layer 4: Transport Layer
The Transport Layer is responsible for transmitting data between devices.

The two main protocols used at this layer are:
- TCP (Transmission Control Protocol)
- UDP (User Datagram Protocol)

---

# TCP (Transmission Control Protocol)

TCP is designed for:
- Reliability
- Accuracy
- Guaranteed delivery

TCP creates a stable connection between two devices and verifies that data arrives correctly and in the proper order.

## Advantages of TCP
- Guarantees accurate data transmission
- Performs error checking
- Synchronizes communication between devices

## Disadvantages of TCP
- Slower than UDP
- Requires a continuous connection
- Can be affected by slow connections

## Common Uses:

TCP is used when accuracy is critical:
- File transfers
- Email
- Web browsing

Example:
Downloading a file requires every piece of data to arrive correctly.

---

# UDP (User Datagram Protocol)
UDP focuses on speed rather than reliability.

Unlike TCP, UDP:
- Does not verify delivery
- Does not establish a continuous connection
- Sends data without confirming receipt

## Advantages of UDP
- Faster than TCP
- Requires less overhead
- Allows applications to control transmission speed

## Disadvantages of UDP
- Data may be lost
- No error checking
- Poor performance over unstable connections

## Common Uses:

UDP is useful when speed is more important than perfect accuracy:
- Video streaming
- Device discovery
- DHCP
- ARP

Example:
During video streaming, losing a few packets may only cause temporary pixelation.

---

# TCP vs UDP Comparison

| TCP | UDP |
|---|---|
| Reliable delivery | No delivery guarantee |
| Connection-based | Connectionless |
| Slower | Faster |
| Error checking | No error checking |
| Used for files, email, websites | Used for streaming and real-time communication |

---

# Layer 5: Session Layer
The Session Layer creates and maintains communication sessions between devices.

Responsibilities include:
- Establishing connections
- Maintaining sessions
- Closing inactive connections
- Creating checkpoints for recovery

If data is lost during transmission, checkpoints allow only the missing information to be resent.
Each session is unique, meaning data cannot move between different sessions.

---

# Layer 6: Presentation Layer
The Presentation Layer acts as a translator between applications.

Responsibilities include:
- Data formatting
- Data translation
- Encryption and decryption

This layer ensures that data sent from one application can be understood by another.

Security functions such as:
HTTPS encryption


occur at this layer.

---

# Layer 7: Application Layer
The Application Layer is the layer users interact with most directly.
It defines how applications communicate with network services.

Examples include:
- Web browsers
- Email clients
- File transfer applications

Common protocols include:
- DNS (Domain Name System)
- HTTP/HTTPS
- FTP

Example:
DNS translates website names into IP addresses.
google.com → IP Address

---

# Key Takeaways

- The OSI model provides a standardized framework for network communication.
- Data moves through seven layers, each with specific responsibilities.
- Encapsulation occurs as information is added at each layer.
- TCP provides reliable communication, while UDP prioritizes speed.
- Understanding the OSI model is essential for troubleshooting networks and analyzing security issues.

---

# Completed lab to identify and correctly order the seven layers of the OSI model to escape the dungeon and retrieve the flag.
- Used knowledge of the OSI model layers.
- Applied understanding of layer order and responsibilities.

---

Conclusion:
The OSI model is a foundational concept in networking and cybersecurity. Understanding how each layer functions helps security professionals troubleshoot network issues, analyze traffic, and understand where attacks may occur.
Learning the OSI model provides the foundation needed for understanding protocols, network devices, and security tools such as Wireshark.

