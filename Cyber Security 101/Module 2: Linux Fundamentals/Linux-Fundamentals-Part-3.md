# Linux Fundamentals Part 3

## Learning Objectives
- Edit files using terminal-based text editors.
- Transfer files between local and remote systems.
- Understand Linux processes and service management.
- Learn task automation, package management, and log locations.

## Notes
- **Nano** is a beginner-friendly terminal text editor; **Vim** is a more advanced alternative.
- **wget** downloads files from web servers over HTTP.
- **scp** securely transfers files between systems using SSH.
- Python's built-in HTTP server (`python3 -m http.server`) can quickly share files over a network.
- View running processes with `ps` and monitor them in real time with `top`.
- Manage processes using `kill` with signals like `SIGTERM`, `SIGKILL`, and `SIGSTOP`.
- **systemctl** manages services (`start`, `stop`, `enable`, `disable`, `status`).
- Run commands in the background using `&`, suspend with `Ctrl + Z`, and restore with `fg`.
- **cron** automates scheduled tasks using `crontab -e`.
- **apt** installs, updates, and removes software from trusted repositories.
- System logs are stored in **`/var/log`** and are useful for troubleshooting and security investigations.

## Lab
- Edited files using **Nano**.
- Downloaded files with **wget**.
- Transferred files securely using **scp**.
- Hosted files using Python's **HTTP server**.
- Viewed and managed running processes.
- Explored service management with **systemctl**.
- Reviewed task scheduling with **cron** and software management with **apt**.

## Conclusion
This room expanded my Linux skills by introducing text editors, secure file transfers, process management, service control, task automation, package management, and system logging. These are core administrative skills that are widely used in cybersecurity and system administration.
