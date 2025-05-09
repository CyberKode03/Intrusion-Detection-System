import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from datetime import datetime

# Connect to MySQL database
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Replace with your MySQL password if you set one
        database="idsdb",  # Ensure this database exists
        port=3377          # ✅ This is critical if you changed the port in XAMPP
    )
except mysql.connector.Error as err:
    messagebox.showerror("Database Connection Error", f"Error: {err}")
    exit()

# Fetch alerts from the database
def fetch_alerts():
    try:
        cursor = db.cursor()
        cursor.execute("SELECT timestamp, src_ip, dest_ip, message FROM alerts ORDER BY timestamp DESC")
        results = cursor.fetchall()
        return results
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return []

# Refresh table contents
def refresh_table():
    for row in tree.get_children():
        tree.delete(row)

    for alert in fetch_alerts():
        tree.insert("", "end", values=alert)

# Schedule automatic refresh every 10 seconds
def schedule_refresh():
    refresh_table()
    root.after(10000, schedule_refresh)

# Clear all alerts
def clear_alerts():
    try:
        cursor = db.cursor()
        cursor.execute("TRUNCATE TABLE alerts")
        db.commit()
        refresh_table()
    except mysql.connector.Error as err:
        messagebox.showerror("Clear Alerts Error", f"Error: {err}")

# Create the GUI window
root = tk.Tk()
root.title("Intrusion Detection System - Alert Viewer")
root.geometry("800x400")
root.configure(bg="#f5f5f5")

# Heading
heading = tk.Label(root, text="🚨 IDS Alert Viewer", font=("Arial", 18, "bold"), bg="#f5f5f5")
heading.pack(pady=10)

# Create a Treeview widget for table
columns = ("Timestamp", "Source IP", "Destination IP", "Message")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=180 if col == "Message" else 120)

tree.pack(expand=True, fill="both", padx=20)

# Clear Alerts Button
clear_button = tk.Button(root, text="Clear Alerts", command=clear_alerts, bg="red", fg="white", font=("Arial", 10, "bold"))
clear_button.pack(pady=10)

# Initial table load and schedule auto-refresh
refresh_table()
schedule_refresh()

# Start the GUI loop
root.mainloop()
