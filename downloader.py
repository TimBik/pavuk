import requests


def getHTML(site):
    response = requests.get(site)
    return response.text


if __name__ == '__main__':
    sites = open("sites.txt", "r").readlines()
    id = 0
    # site = sites[0][:-5]
    # print(site)
    # for i in range(19):
    #     print(site + str(i + 1) + ".php")
    for site in sites:
        if("\n" in site):
            site = site[:-1]
        print(site)
        try:
            html = getHTML(site)
            file_download = open("vikachka/html_" + str(id) + ".txt", 'w')
            file_download.write(html)
            file_download.close()
            print(id)
            id += 1
        except:
            print("notWork")



