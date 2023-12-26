# Code by AkinoAlice@Tyrant_Rex

import requests
import os
import re
import json

from bs4 import BeautifulSoup
from webbrowser import open_new
from zipfile import ZipFile


class PermissionError(Exception):
    pass


class handler:
    def __init__(self) -> None:
        self.StartSoulWorker: bool
        self.KeepArchive: bool
        self.RepoOwner: str
        self.vision: str

        if not os.path.exists(f"./config.json"):
            setting = {
                "StartSoulWorker": True,
                "KeepArchive": False,
                "KeepFonts": False,
                "RepoOwner": "neonr-0",
            }
            with open("./config.json", "w") as setting_file:
                setting_file.write(json.dumps(setting, indent=4))

        with open("./config.json", "r", encoding="utf-8") as f:
            setting = json.load(f)

        self.StartSoulWorker = setting["StartSoulWorker"]
        self.KeepArchive = setting["KeepArchive"]
        self.KeepFont = setting["KeepFonts"]
        self.RepoOwner = setting["RepoOwner"]
        self.vision = ""

    # check update
    def check_vision(self) -> None:
        soup = BeautifulSoup(requests.get(
            f"https://github.com/{self.RepoOwner}/SoulMeter").text, "lxml")
        soup = soup.find(href=re.compile(
            f"/{self.RepoOwner}/SoulMeter/releases/tag/*"))
        self.vision = soup["href"].replace(
            f"/{self.RepoOwner}/SoulMeter/releases/tag/", "")

    # update soulmeter
    def update(self) -> None:
        for soulmeter_file in os.listdir("./soulmeter"):
            if soulmeter_file.endswith(".exe"):
                if f"./soulmeter/{soulmeter_file}" == f"./soulmeter/SoulMeter {self.vision}.exe":
                    return
                os.remove(f"./soulmeter/{soulmeter_file}")

        with open(f"./archive/{self.vision}.zip", "wb") as f:
            f.write(requests.get(
                f"https://github.com/{self.RepoOwner}/SoulMeter/releases/download/{self.vision}/SoulMeter-v{self.vision}.zip").content)

        with ZipFile(f"./archive/{self.vision}.zip", "r") as zip_file:
            for file_name in zip_file.namelist():
                if file_name in ["WinDivert.dll", "WinDivert64.sys"]:
                    continue

                if ".ttf" in file_name and self.KeepFont and os.path.exists("./soulmeter/Font"):
                    continue

                zip_file.extract(file_name, r"./soulmeter")

        os.rename("./soulmeter/SoulMeter.exe",
                  f"./soulmeter/SoulMeter {self.vision}.exe")

        if not self.KeepArchive:
            os.remove(f"./archive/{self.vision}.zip")

    # startup
    def startup(self) -> None:
        if not os.path.exists("./soulmeter"):
            os.mkdir("./soulmeter")
        if not os.path.exists("./archive"):
            os.mkdir("./archive")

    def start_soulworker(self) -> None:
        os.chdir("./soulmeter")
        os.popen(f"./SoulMeter {self.vision}.exe")

        if self.StartSoulWorker:
            open_new("steam://rungameid/1377580")

    def main(self) -> None:
        self.startup()
        self.check_vision()
        self.update()
        self.start_soulworker()


if __name__ == "__main__":
    try:
        sw = handler()
        sw.main()
    except Exception as e:
        raise PermissionError(f"""
                Please follow the following instructions:
                1. Right click the program
                2. Select "Properties" -> "Compatibility".
                3. Verify if the checkbox for "Run this program as an Administrator" has been selected.

                請按照以下說明操作:
                1.右鍵單擊程序
                2.選擇屬性 -> 兼容性
                3.檢查是否選中“以管理員身份運行此程序”的複選框
                ----------------------------------------------------------------
                {e}
        """)
