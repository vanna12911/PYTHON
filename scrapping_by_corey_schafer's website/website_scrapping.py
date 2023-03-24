from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

source = requests.get("https://coreyms.com/").text

soup = BeautifulSoup(source , "lxml")

csv_file = open("from_corey's_website.csv", "w")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Headline" ,"Summary", "Video_link"])

# print(soup.prettify())
print()

here =soup.find_all("article")
# len(here)
# print(here.prettify())

print()

# headline = here.h2.a.text
# print(headline)

print()

# timeline=  here.header.h2.p.time.text     # prb 1
# print(timeline)
 
# summary = here.find("div", class_ = "entry-content").p.text       #both works
# summary = here.div.p.text                                    # it has gotten into the first div itself
# print(summary)

# vid_src=  here.find("iframe", class_ ="youtube-player")['src']
# print(vid_src)
print()

# vid_id = vid_src.split("/")[4]
# print(vid_id)
print()

# vid_id = vid_id.split("?")[0]
# print(vid_id)
print()

# yt_link = "https://www.youtube.com/watch?v=z0gguhEmWiY"
# print(yt_link)

for article in here:
    headline= article.h2.a.text
    print(headline)
    print()

    summary = article.find("div", class_= "entry-content").p.text
    print(summary)
    print()


     # exception handling
    try:
        vid_src= article.find("iframe", class_= "youtube-player")['src']
        vid_id = vid_src.split("/")[4]
        vid_id = vid_id.split("?")[0]
        yt_link = f"https://www.youtube.com/watch?v={vid_id}"
        print(yt_link)
        print()
    except Exception as e:
        yt_link= None

        print(yt_link)
        print()


    csv_writer.writerow([headline , summary  ,yt_link])


csv_file.close()
    
