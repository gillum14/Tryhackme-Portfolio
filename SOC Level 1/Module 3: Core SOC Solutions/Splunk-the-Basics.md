# Splunk: The Basics

## Learning Objectives

- Understand Splunk's core architecture
- Learn the purpose of Forwarders, Indexers, and Search Heads
- Explore the Splunk interface
- Understand how Splunk ingests log data
- Perform basic log ingestion and searches using SPL

---

## Notes

### What is Splunk?

- **Splunk** is a leading Security Information and Event Management (**SIEM**) platform.
- Collects, indexes, searches, and analyzes machine and network data in real time.
- Enables security analysts to detect threats, investigate incidents, and visualize security events.

---

### Splunk Architecture

#### Splunk Forwarder

A lightweight agent installed on monitored systems.

Responsibilities:
- Collects logs from endpoints
- Sends data to the Splunk Indexer
- Minimal impact on system performance

Common log sources:
- Windows Event Logs
- PowerShell logs
- Sysmon
- Linux system logs
- Web server logs
- Database logs

---

#### Splunk Indexer

The core processing component of Splunk.

Responsibilities:
- Receives logs from Forwarders
- Parses incoming data
- Normalizes logs into **field-value pairs**
- Indexes and stores events
- Makes data searchable

---

#### Splunk Search Head

The analyst's primary workspace.

Responsibilities:
- Executes searches using **SPL (Search Processing Language)**
- Retrieves indexed events
- Creates dashboards, reports, and visualizations
- Supports tables, pie charts, bar charts, and other visual analytics

---

### Splunk Interface

#### Splunk Bar

Provides quick access to:
- Messages
- Settings
- Activity
- Help
- Global Search
- Installed Apps

---

#### Apps Panel

- Displays installed Splunk applications
- Default application:
  - **Search & Reporting**

---

#### Explore Splunk

Quick access to:
- Add Data
- Install Apps
- Documentation

---

#### Home Dashboard

- Displays available dashboards
- Supports custom dashboards
- Visualizes indexed security data

---

### Log Ingestion

Splunk can ingest many types of machine data, including:

- Windows Event Logs
- Linux logs
- Firewall logs
- VPN logs
- Web server logs
- Application logs
- Database logs
- JSON logs

#### Upload Process

1. Select Source
2. Select Source Type
3. Configure Input Settings
4. Review Configuration
5. Complete Upload

---

### JSON Log Parsing

When uploading newline-delimited JSON:

- Use the detected **JSON** source type
- Create or select the destination index
- If fields are not extracted automatically, use:

```spl
| spath
```

`spath` parses JSON fields into searchable field-value pairs.

---

### Basic SPL Searches

Count all events:

```spl
index=VPN_Logs
| stats count
```

Search for a specific user:

```spl
index=VPN_Logs
| spath
| search UserName="Maleena"
| stats count
```

Find activity from a specific IP:

```spl
index=VPN_Logs
| spath
| search Source_ip="107.14.182.38"
| stats values(UserName) as UserName count
```

Exclude a country:

```spl
index=VPN_Logs
| spath
| search Source_Country!="France"
| stats count
```

Count events from an IP address:

```spl
index=VPN_Logs
| spath
| search Source_ip="107.3.206.58"
| stats count
```

---

### Key Concepts

- **Forwarder:** Collects and forwards logs
- **Indexer:** Parses, normalizes, indexes, and stores logs
- **Search Head:** Searches and visualizes indexed data
- **SPL (Search Processing Language):** Splunk's query language
- **Field-Value Pair:** Structured representation of parsed log data
- **Index:** Storage location for searchable events
- **spath:** Extracts fields from JSON data

---

## Lab

- Explored the Splunk interface
- Reviewed Splunk architecture
- Uploaded VPN JSON logs
- Created a new index (`VPN_Logs`)
- Parsed JSON events using `spath`
- Performed basic SPL searches to validate data ingestion
- Queried logs by username, IP address, and country

---

## Conclusion

Splunk is one of the most widely used SIEM platforms for collecting, indexing, searching, and visualizing security data. Understanding its architecture—Forwarders, Indexers, and Search Heads—along with basic log ingestion and SPL searching, provides the foundation for threat hunting, incident response, and day-to-day SOC operations.