import unicodedata


def output_tf_idf(title_list, values, feature_names):
    print()
    for i, vec in enumerate(values):
        cnt = 0
        print(f"【{title_list[i]}】")
        for w_id, tfidf in sorted(enumerate(vec), key=lambda x: x[1], reverse=True):
            if cnt >= 5:
                break
            lemma = feature_names[w_id]
            tfidf = format(tfidf, ".8f")

            count = 0
            for c in lemma:
                if unicodedata.east_asian_width(c) in "FWA":
                    count += 1

            col = 14 - count
            print(f"{lemma:{col}}:{tfidf:10}")
            cnt += 1
        print()
