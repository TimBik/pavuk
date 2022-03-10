from bs4 import BeautifulSoup
import pymorphy2

morph = pymorphy2.MorphAnalyzer()

file_name_p = "vikachka/html_"
for i in range(1, 149):
    html = open(file_name_p + str(i) + ".txt", "r")
    soup = BeautifulSoup(html, 'html.parser')
    # текст из HTML-документа
    text = soup.get_text()
    text = text.replace('\n', ' ')
    # text = text.replace('  ', ' ')
    words = text.split(" ")
    save = open("tokens/word_text_" + str(i) + ".txt", 'w')
    unikum = set()
    for word in words:
        if (word != '' and not "же" in word ):
            res = morph.parse(word)[0]
            if (res.is_known and res.tag.POS != "ADJF" and res.tag.POS != "PREP" and res.tag.POS != "CONJ"):
                unikum.add(word)

    for word in unikum:
        save.write(word + "\n")
    print(str(i) + " done")
