# Introduction to EDR

## Learning Objectives

- Understand the purpose and core functions of Endpoint Detection and Response.
- Differentiate EDR from traditional antivirus solutions.
- Explain the architecture of an EDR platform.
- Identify common endpoint telemetry collected by EDR agents.
- Understand EDR detection and response capabilities.
- Practice investigating alerts in a simulated EDR console.

## Notes

### Endpoint Detection and Response

**Endpoint Detection and Response (EDR)** is a security solution that continuously monitors endpoints, detects suspicious activity, and allows analysts to respond to threats from a centralized console.

EDR is especially important in remote and hybrid environments because endpoints may operate outside an organization's traditional network perimeter.

Common EDR platforms include:

- CrowdStrike Falcon
- SentinelOne ActiveEDR
- Microsoft Defender for Endpoint
- OpenEDR
- Symantec EDR

Although products differ in features, most use a similar architecture based on endpoint agents and a centralized management console.

---

### Core Pillars of EDR

EDR platforms are built around three primary capabilities:

1. **Visibility**
2. **Detection**
3. **Response**

#### Visibility

EDR provides detailed insight into activity occurring on endpoints.

Common activity captured includes:

- Process creation and termination
- Parent-child process relationships
- Command-line activity
- Registry modifications
- File and folder changes
- Network connections
- User activity

This information is often displayed as a process tree and timeline, allowing analysts to reconstruct the sequence of events surrounding an alert.

Historical endpoint data can also support threat hunting and incident investigations.

#### Detection

EDR combines multiple detection methods, including:

- Signature-based detection
- Behavioral detection
- Anomaly detection
- Indicator of Compromise matching
- Machine learning
- MITRE ATT&CK mapping

These capabilities allow EDR to identify threats that may bypass traditional antivirus, including:

- Fileless malware
- Obfuscated PowerShell activity
- Process injection
- Suspicious parent-child process relationships
- Multi-stage attacks
- Previously unknown malware

#### Response

EDR allows analysts to respond directly from a centralized console.

Common response actions include:

- Isolating a host
- Terminating a process
- Quarantining a file
- Connecting remotely to an endpoint
- Running commands or scripts
- Collecting forensic artifacts

EDR is primarily a host-based security solution and should be used alongside network and cloud security tools.

---

### Antivirus vs. EDR

Traditional antivirus mainly relies on signatures to identify known malicious files.

EDR provides broader visibility by monitoring endpoint behavior before, during, and after execution.

| Capability | Antivirus | EDR |
|---|---|---|
| Signature-based detection | Yes | Yes |
| Behavioral detection | Limited | Yes |
| Process-tree visibility | Limited | Yes |
| Command-line monitoring | Limited | Yes |
| Memory-injection detection | Limited | Yes |
| Historical telemetry | Limited | Yes |
| Centralized investigation | Limited | Yes |
| Remote response actions | Limited | Yes |
| MITRE ATT&CK mapping | Usually no | Often yes |

Modern antivirus products may include advanced features, but EDR generally provides deeper investigation and response capabilities.

---

### Example Attack Chain

A phishing attack may progress through the following stages:

1. A user receives a malicious Word document.
2. The user opens the document.
3. A malicious macro launches PowerShell.
4. PowerShell executes an obfuscated command.
5. A second-stage payload is downloaded.
6. Malicious code is injected into `svchost.exe`.
7. The attacker establishes remote access.

A traditional antivirus may miss the activity if no known signature is present.

An EDR may detect:

- The downloaded file
- `winword.exe` execution
- An unusual `winword.exe` → `powershell.exe` relationship
- Obfuscated PowerShell commands
- Process injection into `svchost.exe`
- Unexpected outbound network connections
- The complete attack chain

---

### EDR Architecture

#### Endpoint Agents

EDR agents, also called sensors, are installed on endpoints.

Their responsibilities include:

- Monitoring endpoint activity
- Collecting telemetry
- Performing basic local detections
- Sending data to the EDR console
- Receiving response commands

The agent acts as the eyes and ears of the EDR platform.

#### EDR Console

The centralized EDR console receives and analyzes endpoint data.

It may use:

- Correlation logic
- Threat intelligence
- Behavioral analytics
- Machine learning
- Detection rules
- MITRE ATT&CK mappings

The console allows analysts to:

- Review detections
- Prioritize alerts
- Investigate endpoint activity
- Determine whether an alert is a true or false positive
- Take containment and remediation actions

---

### Alert Prioritization

EDR alerts are commonly assigned severity levels such as:

- Critical
- High
- Medium
- Low
- Informational

Analysts generally investigate the highest-severity alerts first.

During triage, analysts review:

- Files executed
- Processes created
- Command-line activity
- Network connections
- Registry changes
- User activity
- Related alerts
- Threat intelligence
- MITRE ATT&CK mappings

The analyst then determines whether the alert is a:

- **True positive**
- **False positive**
- **Benign positive**
- **Unconfirmed or requiring escalation**

---

### EDR Telemetry

Telemetry is the endpoint data collected by EDR agents.

Detailed telemetry helps analysts distinguish normal activity from malicious behavior and reconstruct the full attack timeline.

#### Process Activity

EDR records process executions and terminations.

This helps identify:

- Suspicious executables
- Unusual parent-child relationships
- Malware payloads
- Living-off-the-land activity
- Process injection

Example:

```text
winword.exe
└── powershell.exe
    └── suspicious-payload.exe
```

#### Network Connections

EDR monitors endpoint network activity.

This may reveal:

- Command-and-control communication
- Unusual ports
- Data exfiltration
- Lateral movement
- Unexpected external connections

#### Command-Line Activity

EDR captures commands executed through tools such as:

- Command Prompt
- PowerShell
- Scripting engines
- Administrative utilities

This is useful for detecting:

- Obfuscated scripts
- Encoded commands
- Suspicious administrative commands
- Living-off-the-land techniques

#### File and Folder Changes

EDR records file-system activity such as:

- File creation
- File deletion
- File modification
- Malicious payload drops
- Ransomware encryption
- Data staging

#### Registry Changes

EDR monitors Windows Registry activity.

Suspicious registry changes may indicate:

- Persistence
- Privilege escalation
- Defense evasion
- Configuration changes
- Malware execution

---

### Detection Techniques

#### Behavioral Detection

Behavioral detection evaluates what a process or user is doing rather than relying only on a known signature.

Example:

```text
winword.exe spawning powershell.exe
```

This relationship is unusual and may indicate malicious macro execution.

#### Anomaly Detection

EDR establishes a baseline of normal endpoint behavior.

Activity that deviates from the baseline may be flagged.

Example:

- A process modifies an auto-start registry key on a system where this behavior is uncommon.

Anomaly detection can generate false positives, so analyst review is still required.

#### IOC Matching

EDR compares endpoint activity with known Indicators of Compromise.

Common IOCs include:

- File hashes
- IP addresses
- Domains
- URLs
- Registry keys
- File names

Threat intelligence integrations allow EDR platforms to identify activity associated with known campaigns.

#### MITRE ATT&CK Mapping

EDR alerts may be mapped to MITRE ATT&CK tactics and techniques.

Example:

```text
Tactic: Persistence
Technique: Scheduled Task/Job
```

This helps analysts understand where the activity fits within an attack lifecycle.

#### Machine Learning

Machine learning models analyze patterns across large datasets of normal and malicious behavior.

This can help identify:

- Fileless attacks
- Multi-stage intrusions
- Previously unseen malware
- Suspicious chains of individually benign actions

---

### Response Capabilities

#### Isolate Host

Host isolation disconnects an endpoint from the network while preserving its connection to the EDR platform.

This can:

- Stop lateral movement
- Prevent command-and-control traffic
- Limit data exfiltration
- Contain active malware

Isolation should be used carefully because it may interrupt business operations.

#### Terminate Process

EDR can stop a malicious or suspicious process.

This may be preferable to full host isolation when:

- The threat is limited to one process
- The endpoint supports critical business operations
- Network isolation would cause unnecessary disruption

Analysts must confirm the process before terminating it.

#### Quarantine File

Quarantine moves a suspicious file into an isolated location where it cannot execute.

The file may later be:

- Restored
- Submitted for analysis
- Permanently removed

#### Remote Access

EDR platforms may allow analysts to remotely connect to an endpoint shell.

Remote access can be used to:

- Run commands
- Execute scripts
- Collect additional evidence
- Inspect system activity
- Perform custom remediation

#### Artifact Collection

EDR may allow analysts to remotely collect forensic artifacts, including:

- Memory dumps
- Event logs
- Registry hives
- File-system contents
- Suspicious executables
- Configuration data

These artifacts may support deeper forensic analysis or legal investigations.

---

### EDR in the Security Ecosystem

EDR does not replace every other security tool.

It commonly works alongside:

- SIEM
- Firewalls
- Email security gateways
- Data Loss Prevention
- Identity and Access Management
- Network Detection and Response
- Threat intelligence platforms

These tools may send alerts and telemetry to a SIEM, which provides analysts with a broader view across the organization.

## Lab

- Accessed a simulated EDR dashboard for a fictional organization.
- Reviewed multiple medium- and high-severity detections.
- Examined alert details and endpoint telemetry.
- Analyzed process activity, affected users, hosts, and detection context.
- Used available evidence to answer triage-related questions.
- Practiced understanding EDR visibility without performing containment or remediation actions.

## Conclusion

This room introduced the architecture and capabilities of Endpoint Detection and Response platforms.

I learned how EDR extends beyond traditional antivirus by collecting detailed endpoint telemetry, detecting behavioral and anomalous activity, and providing analysts with centralized response capabilities.

I also practiced reviewing detections in a simulated EDR console and using process, network, command-line, file, and registry data to understand suspicious activity.

EDR is a foundational SOC tool because it gives analysts the visibility and context needed to investigate advanced endpoint threats and respond effectively.