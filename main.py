# main.py

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import threading
import sniffer
import db_connect

class IDSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unified Intrusion Detection System (IDS)")
        self.root.geometry("950x550")
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        tk.Label(self.root, text="Intrusion Detection System Dashboard", font=("Arial", 18, "bold")).pack(pady=10)

        # Buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        self.start_btn = tk.Button(btn_frame, text="Start Sniffing", command=self.start_sniffing, bg="green", fg="white", width=15)
        self.start_btn.grid(row=0, column=0, padx=10)

        self.stop_btn = tk.Button(btn_frame, text="Stop Sniffing", command=self.stop_sniffing, bg="red", fg="white", width=15)
        self.stop_btn.grid(row=0, column=1, padx=10)

        self.refresh_btn = tk.Button(btn_frame, text="Refresh Alerts", command=self.load_alerts, width=15)
        self.refresh_btn.grid(row=0, column=2, padx=10)

        # Treeview Table for Alerts
        columns = ("ID", "Timestamp", "Source IP", "Destination IP", "Message")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=180 if col == "Message" else 120)

        self.tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    def start_sniffing(self):
        self.sniffing_thread = threading.Thread(target=sniffer.start_sniffing)
        self.sniffing_thread.daemon = True
        self.sniffing_thread.start()
        messagebox.showinfo("Started", "Packet sniffing has started.")

    def stop_sniffing(self):
        sniffer.stop_sniffing()
        messagebox.showinfo("Stopped", "Packet sniffing has stopped.")

    def load_alerts(self):
        alerts = db_connect.get_alerts()
        for i in self.tree.get_children():
            self.tree.delete(i)
        for alert in alerts:
            self.tree.insert("", "end", values=alert)

if __name__ == "__main__":
    root = tk.Tk()
    app = IDSApp(root)
    root.mainloop()
