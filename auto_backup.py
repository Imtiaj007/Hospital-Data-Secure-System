import os, requests, time, subprocess

# CONFIGURATION
TOKEN = "Use Your Telegram Token Id"
CHAT_ID = "Use Your Telegram Chat Id"
GPG_PASS = "USE SECURE PASSWORD"
REMOTE = "mydrive:hospital_backup"

def delete_old():
    try:
        result = subprocess.check_output(f"rclone lsf {REMOTE}", shell=True)
        files = sorted([f for f in result.decode().strip().split('\n') if f])
        while len(files) > 3:
            os.system(f"rclone deletefile {REMOTE}/{files.pop(0)}")
    except: pass

def run_backup():
    db_file = "hospital.db"
    if not os.path.exists(db_file): return
    ts = time.strftime("%Y%m%d_%H%M%S")
    enc_f = f"backup_{ts}.db.gpg"
    os.system(f"gpg --batch --yes --pinentry-mode loopback --passphrase {GPG_PASS} -c {db_file}")
    os.rename(f"{db_file}.gpg", enc_f)
    if os.system(f"rclone copy {enc_f} {REMOTE}") == 0:
        delete_old()
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text= Backup Success: {enc_f}")
    if os.path.exists(enc_f): os.remove(enc_f)

if __name__ == "__main__":
     run_backup()
