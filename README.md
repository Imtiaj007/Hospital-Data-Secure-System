# 🏥 Hospital Secure System with Auto-Cloud Backup

A professional Hospital Management System built with Python. It features field-level encryption and automated cloud backups to Google Drive.

## 🚀 Features
- **AES-128 Encryption:** Protects patient data.
- **Auto-Backup:** Encrypts and syncs DB to Google Drive.
- **Telegram Alerts:** Real-time notifications on backup status.
- **Dynamic UI:** Real-time date and auto-ID generation.

## 🛠️ Setup
1. Install dependencies: `pip install cryptography requests`
2. Configure Rclone with Google Drive.
3. Run: `./Hospital_App.sh`

## How to Run:
Follow these steps to set up the application on your Linux system:

​Step 1: Clone the Repository
​Open your terminal and run: `git clone https://github.com/imtiaj007/Hospital-Secure-System.git
cd Hospital-Secure-System`

Step 2: Install Required Libraries
​This app requires cryptography and requests. Install them using: `pip install cryptography requests`

Step 3: System Dependencies
​Make sure you have the following tools installed on your system:
​GPG: For database encryption.
​Rclone: For cloud backup (Google Drive).
​Python 3: To run the scripts.

​Step 4: Configure Backup (Optional but Recommended)
​Open auto_backup.py and replace the BOT_TOKEN and CHAT_ID with your own Telegram bot credentials.
​Setup Rclone with Google Drive and name the remote as mydrive.

​Step 5: Run the Application
​First, give execution permission to the launcher script, then run it:
`chmod +x Hospital_App.sh
./Hospital_App.sh`
