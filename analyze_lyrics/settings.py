import os

# ARTIST_NAME = "=LOVE"
# ARTIST_NAME = "≠ME"
ARTIST_NAME = "≒JOY"
# ARTIST_NAME = "日向坂46"

CHASEN_ARGS = r" -F '%m\t%f[7]\t%f[6]\t%F-[0,1,2,3]\t%f[4]\t%f[5]\n'"
CHASEN_ARGS += r" -U '%m\t%m\t%m\t%F-[0,1,2,3]\t\t\n'"

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
KASHI_DIR = os.path.join(PARENT_DIR, "kashi", ARTIST_NAME)

WORD_CLOUD_DIR = "word_cloud"
WORD_CLOUD_SAVE_DIR = os.path.join(WORD_CLOUD_DIR, ARTIST_NAME, "tf-idf-no")
