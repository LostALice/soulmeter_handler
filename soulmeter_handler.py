#Code by AkinoAlice@Tyrant_Rex

import requests, os, shutil, ctypes, re

from bs4 import BeautifulSoup

def check_vision() -> str:
    soup = BeautifulSoup(requests.get("https://github.com/ga0321/SoulMeter").text, "lxml")
    soup = soup.find(href=re.compile("/ga0321/SoulMeter/releases/tag/*"))
    return soup["href"].replace("/ga0321/SoulMeter/releases/tag/","")

def update(vision):
    open(f"./{vision}.zip", "wb").write(requests.get(f"https://github.com/ga0321/SoulMeter/releases/download/{vision}/SoulMeter-v{vision}.zip").content)
    shutil.unpack_archive(f"./{vision}.zip", ".")

if not ctypes.windll.shell32.IsUserAnAdmin():
    raise BaseException("Run as Admin/以管理員身份運行")

vision = check_vision()

if not f"SoulMeter {vision}.exe" in os.listdir():
    update(vision)

os.popen(f"./SoulMeter {vision}.exe")
