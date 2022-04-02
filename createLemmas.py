import pymorphy2

morph = pymorphy2.MorphAnalyzer()

name_file = "tokens/word_text_"
for i in range(1, 150):
    try:
        tokens = open(name_file + str(i) + ".txt", "r").readlines()
        lems = {}
        for token in tokens:
            if (token[-1] == "\n"):
                token = token[0:-1]
            normal = morph.parse(token)[0].normal_form
            if (normal not in lems):
                lems[normal] = set()
            lems[normal].add(token)
        lem_file = open("lems/lem_" + str(i) + ".txt", "w")
        for lem in lems:
            lem_file.write(lem + ":  ")
            for token in lem:
                lem_file.write(token)
            lem_file.write("\n")
        print(str(i) + " done")
    except FileNotFoundError:
        print('Файл не существует!')
