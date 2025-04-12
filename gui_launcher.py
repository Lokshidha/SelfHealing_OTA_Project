
import tkinter as tk
from tkinter import messagebox, scrolledtext
import shutil
from ecu_simulator import run_ecu


def backup_version1():
    try:
        shutil.copy("updates/version1.py", "backup/version_backup.py")
        log_output("🗂️ Backup of Version 1 created.\n")
        update_status("✔ Backup Complete", "green")
    except Exception as e:
        log_output(f"❌ Backup Failed: {e}\n")
        update_status("✖ Backup Failed", "red")

def apply_update():
    log_output("\n🚀 Starting OTA Update...\n")
    update_status("⏳ Updating ECU...", "orange")
    try:
        run_ecu("updates/version2.py")
        log_output("✅ OTA Update Applied Successfully!\n")
        shutil.copy("updates/version2.py", "backup/version_backup.py")
        update_status("✔ OTA Update Success", "green")
    except Exception:
        log_output("❌ Update Failed! Rolling back to last stable version...\n")
        try:
            run_ecu("backup/version_backup.py")
            log_output("🔁 Rollback successful. ECU is now running the stable version.\n")
            update_status("✔ Rolled Back to Stable", "green")
        except Exception as e:
            log_output(f"❌ Rollback also failed: {e}\n")
            update_status("✖ Rollback Failed", "red")

def log_output(message):
    output_box.insert(tk.END, message)
    output_box.see(tk.END)

def update_status(message, color):
    status_label.config(text=message, fg=color)

# ---------- UI Setup ----------
window = tk.Tk()
window.title("KPIT - Self-Healing OTA ECU System")
window.geometry("700x500")
window.configure(bg="#e8f0fe")

# ---------- Styles ----------
BUTTON_STYLE = {"padx": 15, "pady": 10, "font": ("Segoe UI", 11, "bold"), "relief": "raised", "bd": 2}
HEADING_FONT = ("Segoe UI", 18, "bold")

# ---------- UI Elements ----------
title = tk.Label(window, text="🚗 KPIT | Self-Healing OTA ECU Demo", font=HEADING_FONT, bg="#e8f0fe", fg="#003366")
title.pack(pady=20)

button_frame = tk.Frame(window, bg="#e8f0fe")
button_frame.pack(pady=10)

backup_btn = tk.Button(button_frame, text="🗂️ Backup Stable ECU", bg="#00a65a", fg="white", command=backup_version1, **BUTTON_STYLE)
backup_btn.grid(row=0, column=0, padx=10)

update_btn = tk.Button(button_frame, text="🚀 Apply OTA Update", bg="#007bff", fg="white", command=apply_update, **BUTTON_STYLE)
update_btn.grid(row=0, column=1, padx=10)

output_box = scrolledtext.ScrolledText(window, width=80, height=15, font=("Consolas", 10), bg="#f4f6f9")
output_box.pack(pady=20)

status_label = tk.Label(window, text="System Idle", font=("Segoe UI", 12, "italic"), fg="gray", bg="#e8f0fe")
status_label.pack(pady=5)

# ---------- Run Window ----------
window.mainloop()
