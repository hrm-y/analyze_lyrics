from analyze_kashi import analyze_kashi
from make_word_cloud import make_word_cloud


def main():
    title_hinshi_dic = analyze_kashi()
    make_word_cloud(title_hinshi_dic)


if __name__ == "__main__":
    main()
