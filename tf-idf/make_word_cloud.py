import os
import matplotlib.pyplot as plt
import settings
from wordcloud import WordCloud


def make_word_cloud(title_list, values, feature_names):
    words = feature_names
    vecs = values.tolist()
    temp_dic = {}
    vecs_dic = {}
    for vec, title in zip(vecs, title_list):
        for i in range(len(vec)):
            temp_dic[words[i]] = vec[i]
        vecs_dic[title] = temp_dic
        temp_dic = {}

    wordcloud = WordCloud(
        font_path="/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc",
        background_color="white",
        width=450,
        height=300,
        prefer_horizontal=1.0,
    )

    for title, vec_dic in vecs_dic.items():
        wordcloud.generate_from_frequencies(vec_dic)
        plt.imshow(wordcloud)
        plt.axis("off")
        # plt.show()
        WORD_CLOUD_SAVE_PATH = os.path.join(
            settings.WORD_CLOUD_SAVE_DIR, f"{title}.png"
        )
        print(WORD_CLOUD_SAVE_PATH)
        os.makedirs(settings.WORD_CLOUD_SAVE_DIR, exist_ok=True)
        plt.savefig(WORD_CLOUD_SAVE_PATH)
