import os
import csv
import getpass
import socket
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import subprocess
import sys
import threading

# Save response to CSV
def save_response(choice, response):
    file_exists = os.path.isfile("responses.csv")
    hostname = socket.gethostname()
    username = getpass.getuser()
    identity = f"{hostname}\\{username}"

    with open("responses.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "Computer/User", "Choice", "Response"])
        writer.writerow([datetime.now().isoformat(), identity, choice, response])

# Handlers
def submit_response():
    choice = var.get()
    text = response_entry.get("1.0", tk.END).strip()

    if not text:
        messagebox.showerror("Required", "Please enter a response.")
        return

    save_response(choice, text)
    messagebox.showinfo("Thank You", "Your response has been saved.")
    root.destroy()

def relaunch_script_after_delay(delay_seconds=600):
    """ Relaunches this script after a delay """
    python_executable = sys.executable
    script_path = os.path.abspath(__file__)
    threading.Timer(delay_seconds, lambda: subprocess.Popen([python_executable, script_path])).start()

def snooze():
    relaunch_script_after_delay(600)  # 10 minutes
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("Windows 11 Upgrade Required!")
root.geometry("600x450")
root.resizable(False, False)
root.overrideredirect(True)  # disable drag and close

# Center window
root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (600 // 2)
y = (screen_height // 2) - (450 // 2)
root.geometry(f"+{x}+{y}")

# Frame for content
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill="both", expand=True)

# Title and Description
tk.Label(frame, text="Windows 11 Upgrade Required!", font=("Segoe UI", 16, "bold")).pack(pady=10)

tk.Label(frame, text=(
    "Your computer must be upgraded to Windows 11 due to the end of Windows 10 support.\n\n"
    "If you still rely on Windows 10, explain why. Otherwise, confirm when you will upgrade."
), font=("Segoe UI", 11), justify="left", wraplength=560).pack()

# Radio buttons
var = tk.StringVar(value="Yes")
tk.Radiobutton(frame, text="Yes, I can upgrade (Date is mandatory)", variable=var, value="Yes", font=("Segoe UI", 10)).pack(anchor="w", pady=4)
tk.Radiobutton(frame, text="No, I have a dependency (Application name is mandatory)", variable=var, value="No", font=("Segoe UI", 10)).pack(anchor="w")

# Response field
tk.Label(frame, text="Your response (required):", font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(10, 0))
response_entry = tk.Text(frame, height=4, width=70, font=("Segoe UI", 10))
response_entry.pack(pady=5)

# Submit Button
submit_btn = tk.Button(frame, text="Submit", command=submit_response, font=("Segoe UI", 11, "bold"), width=20)
submit_btn.pack(pady=(10, 0), anchor="center")

# Snooze Button (outside main frame)
snooze_btn = tk.Button(root, text="Snooze", command=snooze)
snooze_btn.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

root.mainloop()
