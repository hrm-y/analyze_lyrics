import requests
from bs4 import BeautifulSoup
import settings


def get_kashi_urls():
    searched_result_artists = []
    res = requests.get(settings.SEARCH_RESULT_IN_TARGET_ARTIST)
    soup = BeautifulSoup(res.text, "html.parser")
    target_artists = soup.find_all("a", attrs={"class": "d-block"})
    searched_result_artists = [
        settings.BASE_URL + target_artist.attrs["href"]
        for target_artist in target_artists
    ]
    """
    for target_artist in target_artists:
        # print(settings.BASE_URL + target_artist.attrs["href"])
        searched_result_artists.append(settings.BASE_URL + target_artist.attrs["href"])
    """

    kashi_urls = []
    for artist_url in searched_result_artists:
        res = requests.get(artist_url)
        soup = BeautifulSoup(res.text, "html.parser")
        a_tags = soup.find_all("a", attrs={"class": "py-2 py-lg-0"})
        for a_tag in a_tags:
            kashi_urls.append(settings.BASE_URL + a_tag.attrs["href"])

    return kashi_urls
