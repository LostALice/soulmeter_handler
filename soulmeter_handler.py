#Code by AkinoAlice@Tyrant_Rex

import requests, os, shutil, ctypes, re, json

from webbrowser import open_new
from bs4 import BeautifulSoup

class PermissionError(Exception):
    """
    Please follow the following instructions:
    1. Right click the program
    2. Select "Properties" -> "Compatibility".
    3. Verify if the checkbox for "Run this program as an Administrator" has been selected.

    請按照以下說明操作:
    1.右鍵單擊程序
    2.選擇屬性 -> 兼容性
    3.檢查是否選中“以管理員身份運行此程序”的複選框
    """


class handler:
    def __init__(self) -> None:
        try:
            setting = json.load("setting.json")
        except FileNotFoundError:
            setting = {
                "KeepHistoryVision": False,
                "KeepArchive": False,
                "StartSoulWorker": True,
                "RepoOwner": "neonr-0",
            }
        with open("config.json", "w") as setting_file:
            setting_file.write(json.dumps(setting,indent=4))

        setting = json.load("setting.json")
        self.KeepHistoryVision = setting["KeepHistoryVision"]
        self.StartSoulWorker = setting["StartSoulWorker"]
        self.KeepArchive = setting["KeepArchive"]
        self.RepoOwner = setting["RepoOwner"]

    #remove old vision
    def remove_file(self,vision: str) -> None:
        for history_file in os.listdir():
            if history_file.endswith(".exe") and not self.KeepHistoryVision:
                if vision in history_file:
                    continue
                elif "soulmeter_handler" in history_file :
                    continue
                os.remove(history_file)

            if history_file.endswith(".zip") and not self.KeepArchive:
                if vision in history_file:
                    continue
                os.remove(history_file)

    #check update
    def check_vision(self,repo_owner: str) -> str:
        soup = BeautifulSoup(requests.get(f"https://github.com/{repo_owner}/SoulMeter").text, "lxml")
        soup = soup.find(href=re.compile(f"/{repo_owner}/SoulMeter/releases/tag/*"))
        return soup["href"].replace(f"/{repo_owner}/SoulMeter/releases/tag/","")

    #update soulmeter
    def update(self,vision: str, repo_owner: str) -> None:
        open(f"./{vision}.zip", "wb").write(requests.get(f"https://github.com/{repo_owner}/SoulMeter/releases/download/{vision}/SoulMeter-v{vision}.zip").content)
        shutil.unpack_archive(f"./{vision}.zip", ".")

    #startup
    def startup(self):
        if not ctypes.windll.shell32.IsUserAnAdmin():
            raise BaseException("Run as Admin/以管理員身份運行")

        if not os.path.exists("./soulmeter"):
            os.mkdir("./soulmeter")
        if not os.path.exists("./archive"):
            os.mkdir("./archive")


# def main():
#     setting = setup()
#     repo_owner = setting["RepoOwner"]

#     if not ctypes.windll.shell32.IsUserAnAdmin():
#         raise BaseException("Run as Admin/以管理員身份運行")
#     vision = check_vision(repo_owner)

#     if not f"SoulMeter {vision}.exe" in os.listdir():
#         update(vision,repo_owner)

#     remove_file(vision)

#     os.popen(f"./SoulMeter {vision}.exe")

#     if setting["StartSoulWorker"]:
#         open_new("steam://rungameid/1377580")

if __name__ == "__main__":
    try:
        handler().startup()
    except:
        raise BaseException("Run as Admin/以管理員身份運行")