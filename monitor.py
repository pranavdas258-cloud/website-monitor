import requests
import hashlib
import time

URL = "https://upsconline.gov.in/marksheet/exam/marksheet_system/archives.php"

BOT_TOKEN = "8698742988:AAEYQcCvfd5zHdCBbWArWBOLEIQJMbo4op0"
CHAT_ID = "6236141105"

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    try:
        requests.post(url, data=data)
    except:
        print("Failed to send Telegram message")

def get_hash():
    try:
        r = requests.get(URL, timeout=10)
        return hashlib.md5(r.text.encode()).hexdigest()
    except:
        print("Error fetching website")
        return None


print("Starting website monitor...")
send_message("✅ Website monitor started")

old_hash = get_hash()

while True:
    print("Checking website...")
    time.sleep(300)   # check every 5 minutes
    
    new_hash = get_hash()

    if new_hash and new_hash != old_hash:
        print("Website changed!")
        send_message("⚠ Website Updated: " + URL)
        old_hash = new_hash