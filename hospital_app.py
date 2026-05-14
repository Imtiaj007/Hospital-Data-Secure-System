import sqlite3, os, datetime
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

# --- Encryption Key Setup ---
KEY_FILE = "secret.key"
if not os.path.exists(KEY_FILE):
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f: f.write(key)
cipher = Fernet(open(KEY_FILE, "rb").read())

# --- Database & Logic ---
def init_db():
    conn = sqlite3.connect('hospital.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS patients 
                    (id INTEGER PRIMARY KEY, name BLOB, mob BLOB, pid BLOB, diag BLOB, date BLOB)''')
    conn.close()

def get_next_id():
    try:
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(id) FROM patients")
        last_id = cursor.fetchone()[0]
        conn.close()
        return f"{last_id + 1:02d}" if last_id is not None else "01"
    except:
        return "01"

def save():
    data = [ent_name.get(), ent_mob.get(), ent_pid.get(), ent_diag.get(), ent_date.get()]
    if all(data):
        enc_data = [cipher.encrypt(d.encode()) for d in data]
        conn = sqlite3.connect('hospital.db')
        conn.execute("INSERT INTO patients (name, mob, pid, diag, date) VALUES (?,?,?,?,?)", enc_data)
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Data Saved Successfully!")
        
        ent_name.delete(0, 'end')
        ent_mob.delete(0, 'end')
        ent_diag.delete(0, 'end')
        
        ent_pid.config(state='normal')
        ent_pid.delete(0, 'end')
        ent_pid.insert(0, get_next_id())
        ent_pid.config(state='readonly')
    else:
        messagebox.showwarning("Error", "All fields are required!")

# --- UI Setup ---
root = tk.Tk()
root.title("Hospital Secure Entry System")
root.geometry("400x520")
init_db()

labels_text = ["Patient Name", "Mobile Number", "Patient ID (Auto)", "Diagnosis", "Date (Auto)"]
entries = []

for text in labels_text:
    tk.Label(root, text=text, font=("Arial", 10, "bold")).pack(pady=5)
    e = tk.Entry(root, width=40)
    e.pack()
    entries.append(e)

ent_name, ent_mob, ent_pid, ent_diag, ent_date = entries

ent_pid.insert(0, get_next_id())
ent_pid.config(state='readonly')

ent_date.insert(0, datetime.datetime.now().strftime("%d/%m/%Y"))
ent_date.config(state='readonly')

tk.Button(root, text="Save", command=save, bg="#2ecc71", fg="white", font=("Arial", 10, "bold")).pack(pady=25)

root.mainloop()
