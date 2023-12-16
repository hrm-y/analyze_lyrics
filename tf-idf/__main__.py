from get_title_kashi_dic import get_title_kashi_dic
from cal_tf_idf import cal_tf_idf


def main():
    title_kashi_dic = get_title_kashi_dic()
    cal_tf_idf(title_kashi_dic)


if __name__ == "__main__":
    main()
