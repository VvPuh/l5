import os
import re


def find_unic_words(text_adr):
    text = os.path.join('data', text_adr)
    if not os.path.isfile(text):
        print("Файл text1 не существует")
        exit()
    text = open(text, "r", encoding="utf-8")
    text_unic_words = set(re.split(r"[ ,.?!'\"()\[\]{}\n;:]", text.read()))
    text_unic_words -= {''}
    text.close()
    return len(text_unic_words)


first_text_unic_words = find_unic_words("text1.txt")
print("Уникальные слов в первом тексте: ", first_text_unic_words)
second_text_unic_words = find_unic_words("text2.txt")
print("Уникальные слов во втором тексте: ", second_text_unic_words)
