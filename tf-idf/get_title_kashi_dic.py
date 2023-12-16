import MeCab
import ipadic
import os
import settings


def get_title_kashi_dic():
    title_kashi_dic = {}

    kashi_txts = os.listdir(settings.KASHI_DIR)
    for kashi_txt in kashi_txts:
        KASHI_PATH = os.path.join(settings.KASHI_DIR, kashi_txt)
        with open(KASHI_PATH, mode="r") as f:
            kashi = f.read()

        tagger = MeCab.Tagger(ipadic.MECAB_ARGS + settings.CHASEN_ARGS)
        node = tagger.parseToNode(kashi)

        split_kashi_list = []

        while node:
            kind_of_hinshi = node.feature.split(",")[0]
            if kind_of_hinshi in settings.HINSHI_LIST:
                if kind_of_hinshi == "名詞":
                    split_kashi_list.append(node.surface)
                    pass
                elif kind_of_hinshi == "動詞":
                    split_kashi_list.append(node.feature.split(",")[6])
                    pass
                elif kind_of_hinshi == "形容詞":
                    split_kashi_list.append(node.feature.split(",")[6])
                    pass
            node = node.next

        split_kashi_list = [
            word
            for word in split_kashi_list
            if not word.lower() in settings.stop_words_all
        ]

        title = kashi_txt.replace(".txt", "")
        title_kashi_dic[title] = " ".join(split_kashi_list)

    return title_kashi_dic
