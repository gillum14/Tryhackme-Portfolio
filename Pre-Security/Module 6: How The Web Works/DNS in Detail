DNS in Detail

Learning Objectives:
~ Understand the purpose of the Domain Name System (DNS).
~ Learn the components of a domain name.
~ Identify common DNS record types.
~ Understand how DNS resolution works.
~ Learn the role of DNS caching.

---

Notes:

What is DNS?:
The **Domain Name System (DNS)** translates human-readable domain names (e.g., `tryhackme.com`) into IP addresses that computers use to communicate.
Without DNS, users would need to remember IP addresses instead of domain names.

---

Domain Structure

A domain name consists of several parts:

| Component | Example | Purpose |
|-----------|---------|---------|
| Top-Level Domain (TLD) | `.com`, `.org`, `.edu` | Identifies the domain category or country |
| Second-Level Domain | `tryhackme` | The registered domain name |
| Subdomain | `admin.tryhackme.com` | Organizes services within a domain |

---

Common DNS Record Types

| Record | Purpose |
|--------|---------|
| **A** | Maps a domain name to an IPv4 address |
| **AAAA** | Maps a domain name to an IPv6 address |
| **CNAME** | Points one domain name to another domain |
| **MX** | Specifies mail servers for a domain |
| **TXT** | Stores text information, commonly used for domain verification and email security (SPF, DKIM, etc.) |

---

DNS Resolution Process

When a domain is requested, DNS follows these general steps:
1. Check the local DNS cache.
2. Query the recursive DNS server (usually provided by an ISP).
3. Contact a Root DNS Server.
4. Contact the appropriate Top-Level Domain (TLD) server.
5. Contact the authoritative name server.
6. Return the requested DNS record to the client.

---

DNS Caching

DNS responses are temporarily stored to improve performance and reduce unnecessary lookups.
Each DNS record includes a **TTL (Time To Live)** value, which determines how long the record remains cached before it must be refreshed.

---

** Completed lab using the DNS query tool to perform DNS lookups and examine different DNS record types.

**Skills practiced:**
- Querying DNS records
- Identifying common DNS record types
- Observing the DNS resolution process

---

Conclusion - DNS is a core networking service that translates domain names into IP addresses, allowing users to access internet resources without memorizing numerical addresses. Understanding DNS records, the DNS resolution process, and caching is essential for troubleshooting network issues and investigating cybersecurity incidents involving domains and internet traffic.
