for i in range(19):
    file = open("vikachka/html_" + str(i) + ".txt", "r").readlines()

    param = "https://"
    param2 = "http://"
    all_sites = set()
    for j in range(20):
        if("<a target=" in file[j]):
            break
        words = file[j].split(" ")
        for word in words:
            if("povezlo.su/" in word):
                continue
            if (param in word and "passport.webmoney" not in word):
                start = word.find(param)
                all_sites.add(word[start:len(word) - 1])
            if (param2 in word):
                start = word.find(param2)
                all_sites.add(word[start:len(word) - 1])

    for site in all_sites:
        print(site)
