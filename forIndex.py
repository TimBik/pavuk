import requests


def getHTML(site):
    response = requests.get(site)
    return response.text


if __name__ == '__main__':
    sites = open("sites.txt", "r").readlines()
    index_file = open("index.txt", "w")
    id = 1


    for site in sites:
        if("\n" in site):
            site = site[:-1]
        print(site)
        try:
            html = getHTML(site)
            index_file.write(str(id) + " " + site + "\n")
            id += 1
        except:
            print("notWork")
    index_file.close()


