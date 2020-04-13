from textblob import *
def count_sents(text):
    simb = '.!?'
    cnt = 0
    for s in simb:
        cnt += text.count(s)
    return cnt


def count_words(text):
    return text.count(' ') + 1


def count_syll(text):
    simb = 'уеёыаоэяиюЁУЕЫАОЭЯИЮ'
    cnt = 0
    for s in simb:
        cnt += text.count(s)
    return cnt


def sent (text):
    ru_blob = TextBlob(text.lower())
    lang = ru_blob.detect_language()
    en_blob = ru_blob.translate(from_lang=lang, to='en')
    print(en_blob)
    sub = en_blob.sentiment.subjectivity * 100
    print(sub)


def main():
    text = input()
    cnt_s = count_sents(text)
    cnt_w = count_words(text)
    cnt_sy = count_syll(text)
    print('количество предложений:', cnt_s)
    print('количество слов:', cnt_w)
    print('количество слогов:', cnt_sy)
    print('средняя длина предложения в словах:', cnt_w/cnt_s)
    print('средняя длина слова в слогах:', cnt_sy/cnt_w)
    Fl = 206.835 - (1.3 * cnt_w/cnt_s) - (cnt_sy/cnt_w * 60.1)
    print('индекс удобочитаемости Флеша:', Fl)
    if Fl > 80:
        print('Текст очень легко читается')
    elif Fl > 50:
        print('Простой текст')
    elif Fl > 25:
        print('Текст немного трудно читать')
    else:
        print('Текст трудно читается')
    sent(text)
if __name__ == '__main__':
    main()
