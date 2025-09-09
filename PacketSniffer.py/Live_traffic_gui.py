import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import sqlite3

class LiveTrafficApp:
    def __init__(self, master):
        self.master = master
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master)
        self.canvas.get_tk_widget().pack()
        self.update_chart()

    def update_chart(self):
        # Query database for protocol counts
        conn = sqlite3.connect("packets.db")
        cur = conn.cursor()
        cur.execute("SELECT protocol, COUNT(*) FROM packets GROUP BY protocol")
        results = cur.fetchall()
        conn.close()
        protocols, counts = zip(*results) if results else ([], [])
        self.ax.clear()
        self.ax.bar(protocols, counts)
        self.ax.set_title("Live Protocol Breakdown")
        self.canvas.draw()
        self.master.after(1000, self.update_chart)  # Update every second

root = tk.Tk()
app = LiveTrafficApp(root)
root.mainloop()
