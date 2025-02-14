import minimalmodbus
import sqlite3
from datetime import datetime
import time
from pytz import timezone

# Configure Modbus parameters
PORT_NAME = "/dev/ttyAMA3"
SLAVE_ADDRESS = 1
BAUDRATE = 115200
IST = timezone('Asia/Kolkata')

# Initialize Modbus instrument
instrument = minimalmodbus.Instrument(PORT_NAME, SLAVE_ADDRESS)
instrument.serial.baudrate = BAUDRATE
instrument.serial.bytesize = 8
instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout = 1
instrument.mode = minimalmodbus.MODE_RTU
instrument.clear_buffers_before_each_transaction = True  

# Define Modbus register mappings
REGISTERS = {
    "Voltage (V)": {"address": 0x0131, "decimals": 1, "function_code": 3, "registers": 1},
    "Current (A)": {"address": 0x0139, "decimals": 3, "function_code": 3, "registers": 2, "bcd": True},
    "Active Power (W)": {"address": 0x0141, "decimals": 1, "function_code": 3, "registers": 2, "bcd": True},
}

# Connect to SQLite database
conn = sqlite3.connect("modbus_data.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS modbus_readings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp_IST TEXT,
    voltage REAL,
    current REAL,
    active_power REAL
)
""")
conn.commit()

# Function to decode BCD values
def decode_bcd(value, decimals):
    result = 0
    multiplier = 1
    while value > 0:
        digit = value & 0xF
        result += digit * multiplier
        multiplier *= 10
        value >>= 4
    return result / (10 ** decimals)

# Function to read a register
def read_register(name, config):
    try:
        raw_values = instrument.read_registers(
            registeraddress=config["address"],
            number_of_registers=config["registers"],
            functioncode=config["function_code"]
        )
        raw_value = int("".join(f"{x:04X}" for x in raw_values), 16)

        # Decode BCD if necessary
        if config.get("bcd", False):
            value = decode_bcd(raw_value, config["decimals"])
        else:
            value = raw_value / (10 ** config["decimals"])

        # Apply Scaling Fixes
        if name == "Current (A)":
            value *= 2.37
        elif name == "Active Power (W)":
            value *= 1.516  # Matches 14.1 W

        return value
    except Exception as e:
        print(f"⚠️ Error reading {name}: {e}")
        return None

# Main function to log data into SQLite
def main():
    READ_INTERVAL = 5  # Read every 5 seconds

    try:
        while True:
            timestamp_IST = datetime.now(IST).strftime("%Y-%m-%d %H:%M:%S")  # Convert to IST
            voltage = read_register("Voltage (V)", REGISTERS["Voltage (V)"])
            current = read_register("Current (A)", REGISTERS["Current (A)"])
            active_power = read_register("Active Power (W)", REGISTERS["Active Power (W)"])

            # Insert data into the database
            cursor.execute("INSERT INTO modbus_readings (timestamp_IST, voltage, current, active_power) VALUES (?, ?, ?, ?)",
                           (timestamp_IST, voltage, current, active_power))
            conn.commit()

            print(f"✅ Data Inserted: {timestamp_IST}, V: {voltage}, A: {current}, W: {active_power}")

            time.sleep(READ_INTERVAL)

    except KeyboardInterrupt:
        print("\n⏹️ Program stopped by user.")
    finally:
        conn.close()
        print("🔄 Database connection closed.")

if __name__ == "__main__":
    main()
