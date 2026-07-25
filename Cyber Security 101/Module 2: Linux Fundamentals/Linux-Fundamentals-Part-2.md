# Linux Fundamentals Part 2

## Learning Objectives
- Connect to remote Linux systems using SSH.
- Use command flags, arguments, and man pages.
- Manage files, directories, and permissions.
- Understand common Linux directories and user management.

## Notes
- **SSH (Secure Shell):**
  - Securely connect to and manage remote Linux systems.
  - Syntax: `ssh username@IP_ADDRESS`

- **Command Flags & Help**
  - Flags modify a command's behavior (e.g., `ls -a`, `ls -l`).
  - `--help` displays available options.
  - `man <command>` opens the command's manual page.

- **Essential File Commands**
  - `touch` – Create a new file.
  - `mkdir` – Create a directory.
  - `cp` – Copy files/directories.
  - `mv` – Move or rename files/directories.
  - `rm` / `rm -R` – Delete files or directories.
  - `file` – Identify a file's type.

- **File Permissions**
  - Permissions consist of **Read (r), Write (w), Execute (x)**.
  - Permissions apply to:
    - Owner
    - Group
    - Others
  - Common numeric permissions:
    - `755` – Owner full access; others read/execute.
    - `644` – Owner read/write; others read only.
    - `700` – Owner only.

- **User Management**
  - `su <user>` – Switch users.
  - `su -l <user>` – Switch users with a full login shell.

- **Important Linux Directories**
  - `/etc` – System configuration files.
  - `/var` – Logs and variable application data.
  - `/root` – Home directory of the root user.
  - `/tmp` – Temporary files; writable by all users.

## Lab
- Connected to a remote Linux machine using SSH.
- Practiced using command flags and man pages.
- Created, copied, moved, renamed, and deleted files/directories.
- Explored file permissions, switched users, and reviewed important system directories.

## Conclusion
This room expanded on Linux fundamentals by introducing remote access with SSH, filesystem management, file permissions, user switching, and key system directories. These skills are foundational for Linux administration and cybersecurity.
