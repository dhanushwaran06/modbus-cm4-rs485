# Save the README content to a file for user download
readme_content = """# Modbus RTU Data Logger - Raspberry Pi CM4 & RS-485

## 📌 Project Overview
This project sets up a **Modbus RTU data logging system** using a **Raspberry Pi CM4**, **RS-485**, and **SQLite**. It reads electrical parameters (Voltage, Current, and Active Power) from an **energy meter** and displays real-time data via a **Flask web dashboard**.

---

## 🛠 Hardware Requirements
- **Raspberry Pi Compute Module 4 (CM4)**
- **Waveshare CM4 IO Base Board (RS-485 supported)**
- **RS-485 Energy Meter** (Supports Modbus RTU communication)
- **RS-485 to USB adapter (optional)**
- **Power supply (5V, 3A recommended)**

---

## 🔌 Wiring Connections (RS-485 to CM4)
| **RS-485 Meter** | **CM4 RS-485 Port** |
|-----------------|-------------------|
| A (Data+)       | RS485-A (A+)       |
| B (Data-)       | RS485-B (B-)       |
| GND             | GND                |

---

## 🖥️ Software Setup (Raspberry Pi OS)
### **1️⃣ Install Required Packages**
```bash
sudo apt update && sudo apt install -y python3 python3-pip sqlite3
pip install flask minimalmodbus pytz
