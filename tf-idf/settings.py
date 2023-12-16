import os
import nltk
from sklearn.feature_extraction import _stop_words

# ARTIST_NAME = "=LOVE"
# ARTIST_NAME = "≠ME"
ARTIST_NAME = "≒JOY"
# ARTIST_NAME = "日向坂46"

CHASEN_ARGS = r" -F '%m\t%f[7]\t%f[6]\t%F-[0,1,2,3]\t%f[4]\t%f[5]\n'"
CHASEN_ARGS += r" -U '%m\t%m\t%m\t%F-[0,1,2,3]\t\t\n'"

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
KASHI_DIR = os.path.join(PARENT_DIR, "kashi", ARTIST_NAME)

HINSHI_LIST = ["名詞", "動詞", "形容詞"]
# HINSHI_LIST = ["名詞"]

# STOP_WORDSの設定
stop_words_sklearn = _stop_words.ENGLISH_STOP_WORDS
nltk.download("stopwords")
stop_words_nltk = nltk.corpus.stopwords.words("english")
stop_words_japanese = ["ここ", "これ", "あと", "ある", "たち", "てる", "する", "ちゃう", "いい"]
stop_words_nltk.extend(stop_words_sklearn)
stop_words_nltk.extend(stop_words_japanese)
stop_words_all = stop_words_nltk

# TF-IDF計算後のワードクラウドを作成するかの設定
MAKE_WORD_CLOUD = True
# MAKE_WORD_CLOUD = False

WORD_CLOUD_DIR = "word_cloud"
WORD_CLOUD_SAVE_DIR = os.path.join(WORD_CLOUD_DIR, ARTIST_NAME, "tf-idf")


# ターミナルに各曲のTF-IDF上位を出力する設定
OUTPUT_TFIDF = True
# OUTPUT_TFIDF = False
