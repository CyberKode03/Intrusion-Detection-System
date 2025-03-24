# 🛡️ Intrusion Detection System (IDS)

This is a GUI-based Intrusion Detection System developed using Python, Scapy, and Tkinter. It captures live packets, analyzes them, and displays suspicious activity in real-time.

---

## 🚀 Features

- 📡 **Packet Sniffing** using Scapy
- ⚠️ **Alert Monitoring** from Snort logs
- 🖥️ **User-Friendly GUI** with Tkinter
- 🗃️ **SQLite Integration** for alert storage
- 🔄 **Real-time Alert Refresh**

---

## 📂 Project Structure

```bash
IDS/
├── .gitignore
├── alert_viewer_gui.py
├── db_connect.py
├── main.py                  # Main GUI Application
├── parse_run.py            # (Optional) For testing snort parsing
├── sniffer.py              # Packet capturing
├── snort_alerts.txt        # Snort alert log (sample)
├── snort_parser.py         # Parses alerts into database
├── test_insert.py          # (Optional) Database test


