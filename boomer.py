# Created by krytyYT
# github.com/krytyYT/WebhookBoomer
import os
import sys
import string
import pyfiglet
import random
from discord_webhook import DiscordWebhook

proxy_file = open("proxy.txt", "r")
proxy_text = proxy_file.readlines()

def proxies():
    line = random.choice(proxy_text)
    ip = line.replace('\n', '')
    if str(ip).startswith('http'):
        pass
    else:
        https = "https://"+ip
        http = "http://"+ip
    proxy = {
        "https":https,
        "http":http
    }
    return proxy
os.system("cls")
result = pyfiglet.figlet_format("Webhook Boomer", font = "slant") 
print(result)
print("\n         github.com/krytyYT/WebhookBoomer\n\n")
prox = str(input("    [?] Use proxies (Yes/No): "))
option = str(input("    [?] Your message: "))
option2 = str(input("    [?] Your webhook url: "))
print("\n\n     If you want to stop close program this is easy xD")
while True:
    if prox == "yes":
        webhook = DiscordWebhook(url=option2, content=option, username="Spamming with: github.com/krytyYT/WebhookBoomer", avatar_url="https://i.imgur.com/4dMqhCc.jpg", proxies=proxies())
        response = webhook.execute()
        print(response)
    else:
        webhook = DiscordWebhook(url=option2, content=option, username="Spamming with: github.com/krytyYT/WebhookBoomer", avatar_url="https://i.imgur.com/4dMqhCc.jpg")
        response = webhook.execute()
        print(response)
