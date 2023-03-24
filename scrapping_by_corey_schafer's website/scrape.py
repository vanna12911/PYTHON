from bs4 import BeautifulSoup
import requests

with open("simple.html") as html_file:
    soup = BeautifulSoup(html_file , 'lxml')

print(soup)
# print(soup.prettify())

# match =  soup.title
match =  soup.title.text

print(match)

print(soup.div)


foot =soup.find_all("div",{"class" : "footer"})  # both works

# foot =soup.find_all("div",class_="footer")
print(foot)

here =soup.find("div",class_ = "article")
headline= here.a.text
print(headline)

summary =  here.p.text
print(summary)

print("-------------------------------")

# for iterating through all the articles
for article in soup.find_all("div", class_ = "article"):
    # print(article)
    headline =article.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()
    
