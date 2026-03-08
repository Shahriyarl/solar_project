import sqlite3

def save_data(voltage, current, power):

    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO solar_data (voltage, current, power) VALUES (?, ?, ?)",
        (voltage, current, power)
    )

    conn.commit()
    conn.close()
