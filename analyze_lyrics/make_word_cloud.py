import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import settings


def make_word_cloud(title_hinshi_dic):
    wordcloud = WordCloud(
        font_path="/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc",
        background_color="white",
        width=450,
        height=300,
        prefer_horizontal=1.0,
    )

    for title, hinshi_dic in title_hinshi_dic.items():
        wordcloud.generate(" ".join(hinshi_dic["meishi_list"]))
        plt.imshow(wordcloud)
        plt.axis("off")
        # plt.show()

        WORD_CLOUD_SAVE_PATH = os.path.join(
            settings.WORD_CLOUD_SAVE_DIR, f"{title}.png"
        )
        os.makedirs(settings.WORD_CLOUD_SAVE_DIR, exist_ok=True)
        plt.savefig(WORD_CLOUD_SAVE_PATH)
