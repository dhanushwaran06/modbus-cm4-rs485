\# Modbus RTU Data Logger - Raspberry Pi CM4 & RS-485

\## Project Overview

This project sets up a Modbus RTU data logging system using a Raspberry
Pi CM4, RS-485, and SQLite. It reads electrical parameters (Voltage,
Current, and Active Power) from an energy meter and displays real-time
data via a Flask web dashboard.

\-\--

\## Hardware Requirements

\- Raspberry Pi Compute Module 4 (CM4) - Waveshare CM4 IO Base Board
(RS-485 supported) - RS-485 Energy Meter (Supports Modbus RTU
communication) - RS-485 to USB adapter (optional) - Power supply (5V, 3A
recommended)

\-\--

\## Wiring Connections (RS-485 to CM4)

\| RS-485 Meter \| CM4 RS-485 Port \|
\|\-\-\-\-\-\-\-\-\-\-\-\-\--\|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\| \| A
(Data+) \| RS485-A (A+) \| \| B (Data-) \| RS485-B (B-) \| \| GND \| GND
\|

\-\--

\## Software Setup (Raspberry Pi OS)

\### 1. Install Required Packages

sudo apt update && sudo apt install -y python3 python3-pip sqlite3 pip
install flask minimalmodbus pytz

\### 2. Clone This Repository

git clone https://github.com/YOUR_USERNAME/modbus-cm4-rs485.git cd
modbus-cm4-rs485

\### 3. Run the Modbus Data Logger

python read_modbus.py

\### 4. Start the Web Dashboard

python app.py

Now visit http://\<Raspberry-Pi-IP\>:5000 in your browser.

\-\--

\## Modbus Data Mapping (Registers)

\| Parameter \| Modbus Address (HEX) \| Decimals \| Registers \| Unit \|
\|\-\-\-\-\-\-\-\-\-\-\-\-\--\|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\|\-\-\-\-\-\-\-\-\--\|\-\-\-\-\-\-\-\-\-\--\|\-\-\-\-\--\|
\| Voltage \| 0x0131 \| 1 \| 1 \| V \| \| Current \| 0x0139 \| 3 \| 2 \|
A \| \| Active Power \| 0x0141 \| 1 \| 2 \| W \|

\-\--

\## Features

\- Reads Modbus RTU data using MinimalModbus - Stores data in SQLite
database - Displays real-time data via a Flask web UI - Fully compatible
with Raspberry Pi CM4 RS-485

\-\--

\## License

This project is open-source under the MIT License.

\-\--

\## Want more features?

Open an issue or contribute! 🚀
