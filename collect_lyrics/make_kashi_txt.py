import requests
import os
from bs4 import BeautifulSoup
import settings


def make_kashi_txt(kashi_urls):
    for kashi_url in kashi_urls:
        res = requests.get(kashi_url)
        soup = BeautifulSoup(res.text, "html.parser")
        title = soup.find("h2", attrs={"class": "ms-2 ms-md-3"}).text.replace("/", "／")
        # artist_name = soup.find("span", attrs={"itemprop": "byArtist name"}).text
        kashi = str(soup.find("div", attrs={"id": "kashi_area"}))
        kashi = (
            kashi.replace('<div id="kashi_area" itemprop="text">', "")
            .replace("</div>", "")
            .replace("<br/>", "\n")
        )

        SAVE_DIR = os.path.join(settings.KASHI_DIR, settings.TARGET_ARTIST)
        SAVE_PATH = os.path.join(SAVE_DIR, f"{title}.txt")
        print(SAVE_PATH)
        os.makedirs(SAVE_DIR, exist_ok=True)
        with open(SAVE_PATH, mode="w") as f:
            f.write(kashi)
