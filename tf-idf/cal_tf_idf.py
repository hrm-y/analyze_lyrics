import settings
from make_word_cloud import make_word_cloud
from output_tf_idf import output_tf_idf

from sklearn.feature_extraction.text import TfidfVectorizer


def cal_tf_idf(title_kashi_dic):
    title_list = list(title_kashi_dic.keys())
    kashi_list = list(title_kashi_dic.values())

    vectorizer = TfidfVectorizer(max_df=0.9)
    values = vectorizer.fit_transform(kashi_list).toarray()
    feature_names = vectorizer.get_feature_names_out()

    if settings.MAKE_WORD_CLOUD:
        make_word_cloud(title_list, values, feature_names)

    if settings.OUTPUT_TFIDF:
        output_tf_idf(title_list, values, feature_names)
