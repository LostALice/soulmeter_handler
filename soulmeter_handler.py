#Code by AkinoAlice@Tyrant_Rex

import requests, os, shutil, ctypes, re

from bs4 import BeautifulSoup

def check_vision(repo_owner: str) -> str:
    soup = BeautifulSoup(requests.get(f"https://github.com/{repo_owner}/SoulMeter").text, "lxml")
    soup = soup.find(href=re.compile(f"/{repo_owner}/SoulMeter/releases/tag/*"))
    return soup["href"].replace(f"/{repo_owner}/SoulMeter/releases/tag/","")


def update(vision: str, repo_owner: str) -> None:
    open(f"./{vision}.zip", "wb").write(requests.get(f"https://github.com/{repo_owner}/SoulMeter/releases/download/{vision}/SoulMeter-v{vision}.zip").content)
    shutil.unpack_archive(f"./{vision}.zip", ".")


def main():
    repo_owner = "neonr-0"
    if not ctypes.windll.shell32.IsUserAnAdmin():
        raise BaseException("Run as Admin/以管理員身份運行")

    vision = check_vision(repo_owner)

    if not f"SoulMeter {vision}.exe" in os.listdir():
        update(vision,repo_owner)

    os.popen(f"./SoulMeter {vision}.exe")


if __name__ == "__main__":
    main()