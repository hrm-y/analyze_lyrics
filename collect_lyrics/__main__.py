from get_kashi_urls import get_kashi_urls
from make_kashi_txt import make_kashi_txt


def main():
    kashi_urls = get_kashi_urls()
    make_kashi_txt(kashi_urls)


if __name__ == "__main__":
    main()
