import requests
from bs4 import BeautifulSoup

URL = "https://upsconline.gov.in/marksheet/exam/marksheet_system/archives.php"

BOT_TOKEN = "8698742988:AAEYQcCvfd5zHdCBbWArWBOLEIQJMbo4op0"
CHAT_ID = "6236141105"

def send_message(text):
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(telegram_url, data=data)

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

links = []
for a in soup.find_all("a"):
    href = a.get("href")
    if href and "marksheet" in href:
        if href.startswith("http"):
            links.append(href)
        else:
            links.append("https://upsconline.gov.in" + href)

links = list(set(links))

try:
    with open("last_links.txt","r") as f:
        old_links = f.read().splitlines()
except:
    old_links = []

new_links = [l for l in links if l not in old_links]

if new_links:
    for link in new_links:
        send_message("🆕 UPSC marksheet update detected:\n" + link)

with open("last_links.txt","w") as f:
    for link in links:
        f.write(link + "\n")
