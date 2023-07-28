import threading
import requests
import os
import random
from pystyle import Write, Colors, Colorate
from datetime import datetime

session = requests.Session()

# Webhook URL
web = Write.Input("[CLOWN] Webhook: ", Colors.rainbow, interval=0.0025)

# Message personnalisé
spam = Write.Input("[CLOWN] Message: ", Colors.rainbow, interval=0.0025)

# Liste des avatars
avatars = [
    "https://th.bing.com/th/id/OIP.u9OOTcnEi5ULfNvUKIawxgHaHa?pid=ImgDet&rs=1",
    "https://cdn.discordapp.com/attachments/1121565947216539789/1121566100858085527/image.png",
    "https://cdn.discordapp.com/attachments/1121565947216539789/1121566059938451526/image.png"
]

# Proxies
proxies = open('proxies.txt').read().splitlines()

def ehook(webhook):
    while True:
        now = datetime.now()
        s = now.strftime("%S")
        x = f'[{datetime.now().strftime("%H:%M:%S")}] Sent Webhook: {spam}'
        yes = f'[{datetime.now().strftime("%H:%M:%S")}]'
        proxy = random.choice(proxies)
        
        einfo = {
            'content': spam,
            "avatar_url": random.choice(avatars)
        }
        try:
            r = session.post(webhook, json=einfo, proxies={"http": 'http://' + proxy})
            if "retry_after" in r.text:
                print(f"{yes} ratelimited sleeping for {r.json()['retry_after']} secs.")
            elif r.status_code == 204:
                print(Colorate.Horizontal(Colors.rainbow, x))
        except requests.exceptions.RequestException as e:
            print(f"Failed to send Webhook: {str(e)}")

if __name__ == "__main__":
    os.system('cls & title Ecstacy Webhook Spammer - SNOXI#0001')
    logo = """
   ______   __       ____     _       __   _   __
  / ____/  / /      / __ \   | |     / /  / | / /
 / /      / /      / / / /   | | /| / /  /  |/ / 
/ /___   / /___   / /_/ /    | |/ |/ /  / /|  /  
\____/  /_____/   \____/     |__/|__/  /_/ |_/
               DEV BY SNOXI
      """
    print(Colorate.Horizontal(Colors.rainbow, logo, 3))
    while True:
        threading.Thread(target=ehook, args=(web,)).start()
