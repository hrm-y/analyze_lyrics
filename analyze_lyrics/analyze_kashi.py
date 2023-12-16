import os
import MeCab
import ipadic

import settings


def analyze_kashi():
    title_hinshi_dic = {}

    kashi_txts = os.listdir(settings.KASHI_DIR)
    for kashi_txt in kashi_txts:
        KASHI_PATH = os.path.join(settings.KASHI_DIR, kashi_txt)
        with open(KASHI_PATH, mode="r") as f:
            kashi = f.read()

        tagger = MeCab.Tagger(ipadic.MECAB_ARGS + settings.CHASEN_ARGS)
        node = tagger.parseToNode(kashi)

        hinshi_dic = {}
        meishi_list = []
        doshi_list = []
        keiyoshi_list = []

        while node:
            if node.feature.split(",")[0] == "名詞":
                meishi_list.append(node.surface)
            elif node.feature.split(",")[0] == "動詞":
                doshi_list.append(node.feature.split(",")[6])
            elif node.feature.split(",")[0] == "形容詞":
                keiyoshi_list.append(node.feature.split(",")[6])

            node = node.next

        print(meishi_list)

        hinshi_dic = {
            "meishi_list": meishi_list,
            "doshi_list": doshi_list,
            "keiyoshi_list": keiyoshi_list,
        }

        title = kashi_txt.replace(".txt", "")
        title_hinshi_dic[title] = hinshi_dic

    return title_hinshi_dic
