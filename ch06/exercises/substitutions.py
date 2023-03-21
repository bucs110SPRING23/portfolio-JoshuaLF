import json

def main():
    subs_file = json.load(open("subs.json", "r"))
    subs_test = json.dumps(subs_file)

    news_file = json.load(open("news.txt", "r"))


    betterNews = open("betternews.txt", "w")

    while news_file.:
        print(str)
        for str in news_file.read():
            if str.