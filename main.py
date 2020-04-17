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


def sent(text):
    ru_blob = TextBlob(text.lower())
    lang = ru_blob.detect_language()
    en_blob = ru_blob.translate(from_lang=lang, to='en')
    sub = en_blob.sentiment.subjectivity * 100
    pol = en_blob.sentiment.polarity
    print('Объективность: ', 100 - sub, '%', sep='')
    if pol <= -0.5:
        print('Тональность текста: негативный')
    elif pol <= 0.5:
        print('Тональность текста: нейтральный')
    else:
        print('Тональность текста: позитивный')


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
    fl = 206.835 - (1.3 * cnt_w / cnt_s) - (cnt_sy / cnt_w * 60.1)
    print('индекс удобочитаемости Флеша:', fl)
    if fl > 80:
        print('Текст очень легко читается')
    elif fl > 50:
        print('Простой текст')
    elif fl > 25:
        print('Текст немного трудно читать')
    else:
        print('Текст трудно читается')
    sent(text)


if __name__ == '__main__':
    main()
