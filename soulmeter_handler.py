#Code by AkinoAlice@Tyrant_Rex

import requests, os, shutil, ctypes, re, json

from webbrowser import open_new
from bs4 import BeautifulSoup

def config() -> str:
    global setting
    try:
        setting = json.read("config.json")
    except:
        setting = {
            "KeepHistoryVision": False,
            "KeepArchive": False,
            "StartSoulWorker": True,
            "RepoOwner": "neonr-0",
        }
        with open("config.json", "w") as setting_file:
            setting_file.write(json.dumps(setting,indent=4))

    return setting

def remove_file(vision: str) -> None:
    for history_file in os.listdir():
        if history_file.endswith(".exe") and not setting["KeepHistoryVision"]:
            if vision in history_file:
                continue
            elif "soulmeter_handler" in history_file :
                continue
            os.remove(history_file)

        if history_file.endswith(".zip") and not setting["KeepArchive"]:
            if vision in history_file:
                continue
            os.remove(history_file)

def check_vision(repo_owner: str) -> str:
    soup = BeautifulSoup(requests.get(f"https://github.com/{repo_owner}/SoulMeter").text, "lxml")
    soup = soup.find(href=re.compile(f"/{repo_owner}/SoulMeter/releases/tag/*"))
    return soup["href"].replace(f"/{repo_owner}/SoulMeter/releases/tag/","")

def update(vision: str, repo_owner: str) -> None:
    open(f"./{vision}.zip", "wb").write(requests.get(f"https://github.com/{repo_owner}/SoulMeter/releases/download/{vision}/SoulMeter-v{vision}.zip").content)
    shutil.unpack_archive(f"./{vision}.zip", ".")

def main():
    setting = config()
    repo_owner = setting["RepoOwner"]

    if not ctypes.windll.shell32.IsUserAnAdmin():
        raise BaseException("Run as Admin/以管理員身份運行")

    vision = check_vision(repo_owner)

    if not f"SoulMeter {vision}.exe" in os.listdir():
        update(vision,repo_owner)

    remove_file(vision)

    os.popen(f"./SoulMeter {vision}.exe")

    if setting["StartSoulWorker"]:
        open_new("steam://rungameid/1377580")

if __name__ == "__main__":
    try:
        main()
    except:
        raise BaseException("Run as Admin/以管理員身份運行")