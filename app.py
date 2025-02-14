from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Function to fetch the latest Modbus data from SQLite
def get_latest_data():
    conn = sqlite3.connect("modbus_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp_IST, voltage, current, active_power FROM modbus_readings ORDER BY id DESC LIMIT 1")
    data = cursor.fetchone()
    conn.close()
    
    if data:
        return {
            "timestamp": data[0],
            "voltage": data[1],
            "current": data[2],
            "active_power": data[3]
        }
    return None

@app.route("/")
def index():
    data = get_latest_data()
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
