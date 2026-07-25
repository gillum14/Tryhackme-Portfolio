# Cryptography Concepts

## Learning Objectives:
- Understand the purpose of cryptography in protecting **Confidentiality** and **Integrity**.
- Explain the difference between **plaintext**, **ciphertext**, **keys**, and **algorithms**.
- Compare **symmetric** and **asymmetric** encryption.
- Understand how encryption is used in **HTTPS** to secure web communications.

## Notes:
- **Cryptography** protects data by converting readable information (**plaintext**) into unreadable data (**ciphertext**) using an **algorithm** and a **key**.
- **Algorithm:** Public method used for encryption/decryption.
- **Key:** Secret value that controls the encryption process; security depends on keeping the key private.

### Symmetric Encryption
- Uses **one shared key** for both encryption and decryption.
- **Advantages:**
  - Fast and efficient.
  - Ideal for encrypting large amounts of data.
- **Disadvantage:**
  - Requires a secure method to share the key (**key distribution problem**).
- **Example:** Caesar Cipher (educational only; not secure for real-world use).

### Asymmetric Encryption
- Uses **two mathematically linked keys**:
  - **Public Key** – Shared with anyone.
  - **Private Key** – Kept secret by the owner.
- Solves the key distribution problem because only the private key can decrypt data encrypted with the public key.
- Commonly used to establish secure communications over the internet.

### HTTPS & Certificates
- HTTPS combines both encryption methods:
  1. **Asymmetric encryption** securely exchanges a shared key.
  2. **Symmetric encryption** encrypts the rest of the session for speed.
- **Digital certificates** verify a website's identity and are signed by trusted **Certificate Authorities (CAs)**.

### Symmetric vs. Asymmetric Encryption

| Symmetric | Asymmetric |
|-----------|------------|
| One shared key | Public & private key pair |
| Very fast | Slower |
| Best for encrypting data | Best for securely exchanging keys |
| Requires secure key sharing | Public key can be shared openly |

## Lab:
- Completed the **Secret Message Rescue** game by encrypting and decrypting messages using the Caesar Cipher.
- Explored how symmetric and asymmetric encryption work together to secure HTTPS connections.

## Conclusion:
Cryptography is a fundamental component of cybersecurity, protecting sensitive information through encryption. Modern systems use a **hybrid approach**, combining asymmetric encryption for secure key exchange with symmetric encryption for efficient data transfer. This combination secures technologies such as HTTPS, VPNs, online banking, and encrypted messaging.
