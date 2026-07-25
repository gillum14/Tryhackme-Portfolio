# Become a Hacker

## Learning Objectives:
- Understand the purpose of **Offensive Security** and ethical hacking.
- Learn common offensive security terminology.
- Practice identifying and exploiting vulnerabilities in a safe environment.
- Become familiar with basic offensive security tools and methodologies.

## Notes:
- **Offensive Security** focuses on proactively finding and exploiting vulnerabilities before malicious attackers do.
- Ethical hacking is **authorized, legal, and performed within a defined scope** to improve security.

### Key Terminology
- **Red Teaming:** Simulates real-world attacks to evaluate an organization's defenses.
- **Penetration Test:** Authorized assessment to identify and validate security vulnerabilities.
- **Vulnerability:** A weakness that could be exploited.
- **Exploit:** A technique used to take advantage of a vulnerability.
- **Scope:** Defines what systems and actions are authorized during testing.
- **Enumeration:** Gathering information about a target to identify potential attack vectors.
- **Authentication:** Verifying a user's identity before granting access.
- **Dictionary Attack:** Attempts logins using a predefined list of passwords.

### Offensive Security Mindset
- Question assumptions and look for unexpected behavior.
- Test inputs developers may not have anticipated.
- Chain multiple small weaknesses together to increase impact.
- Always operate within authorized boundaries.

### Common Offensive Security Tools
- **Gobuster:** Discovers hidden directories and web pages through directory enumeration.
- **Hydra:** Automates password guessing using dictionary attacks against login forms.

### Importance of Credentials
- Attackers often target usernames and passwords because successful authentication can provide access to:
  - Sensitive data
  - Administrative functions
  - Additional attack opportunities

## Lab:
- Used **Gobuster** to enumerate hidden web directories and identify a login page.
- Performed manual password testing followed by an automated **Hydra** dictionary attack to discover valid login credentials.
- Successfully authenticated to the web application and completed the ethical hacking exercise.

## Conclusion:
This room introduced the fundamentals of offensive security and ethical hacking. By combining enumeration, password attacks, and automation, I learned how attackers identify and chain vulnerabilities together while operating within an authorized scope. It also provided a foundation for future penetration testing and red team concepts.
