import json

def main():    
    text = open("ch06/exercises/news.txt", "r").read().lower()

    subs_file = open("ch06/exercises/subs.json", "r")
    subs = json.load(subs_file)
    print(subs)

    for k, v in subs.items():
        text = text.replace(k, v)
        print(text)

    betterNews = open("ch06/exercises/betternews.txt", "w")
    betterNews.write(text)
    betterNews.close()

main()