import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import csv
import os
from datetime import datetime

import os
import csv
import getpass
import socket
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog

def submit_response():
    choice = upgrade_var.get()
    response = response_entry.get().strip()
    


    if choice == "" or response == "":
        messagebox.showerror("Input Error", "Please select an option and fill in the required field.")
        return

    save_response(choice, response)
    messagebox.showinfo("Submitted", "Your response has been saved. Thank you!")
    root.destroy()

def save_response(choice, response):
    file_exists = os.path.isfile("responses.csv")
    hostname = socket.gethostname()  # e.g., OZL4041W
    username = getpass.getuser()     # e.g., jdoe
    computer_identity = f"{hostname}\\{username}"  # e.g., OZL4041W\jdoe

    with open("responses.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "Computer/User", "Choice", "Response"])
        writer.writerow([datetime.now().isoformat(), computer_identity, choice, response])

def snooze():
    messagebox.showinfo("Snoozed", "You chose to snooze. The prompt will return later.")
    root.destroy()

# Main GUI window
root = tk.Tk()
root.title("Windows 11 Upgrade Required!")
root.geometry("500x400")
root.resizable(False, False)

# Heading
tk.Label(root, text="Windows 11 Upgrade Required!", font=("Arial", 14, "bold")).pack(pady=10)

# Message
message = (
    "Hello User,\n\n"
    "Your computer (OZL4041W) must be upgraded to Windows 11 due to the end of\n"
    "Windows 10 support by Microsoft and company compliance.\n"
    "If you had a dependency on Windows 10, please confirm if it still applies. If not,\n"
    "proceed with the upgrade as soon as possible.\n"
    "If you still need Windows 10, please provide the reason or dependent application\n"
    "below. Otherwise, please confirm the date you plan to upgrade to Windows 11."
)
tk.Label(root, text=message, justify="left", wraplength=480).pack(padx=10)

# Radio buttons
upgrade_var = tk.StringVar()

tk.Radiobutton(root, text="Yes, I can upgrade (Date is mandatory)", variable=upgrade_var, value="Yes").pack(anchor="w", padx=20, pady=5)
tk.Radiobutton(root, text="No, I have a dependency (Application name is mandatory)", variable=upgrade_var, value="No").pack(anchor="w", padx=20)

# Response box
tk.Label(root, text="Your response (required):").pack(anchor="w", padx=20, pady=(10, 0))
response_entry = tk.Entry(root, width=60)
response_entry.pack(padx=20, pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

submit_button = ttk.Button(button_frame, text="Submit", command=submit_response)
submit_button.grid(row=0, column=0, padx=10)

snooze_button = ttk.Button(button_frame, text="Snooze", command=snooze)
snooze_button.grid(row=0, column=1, padx=10)

# Run
root.mainloop()