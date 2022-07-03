#let's scrape data into a CSV!
#Goal:Grab all links from Rithm School blog
#Data:store URL, anchor tag text, and date

#URL-https://www.rithmschool.com/blog

from re import A
import requests
from bs4 import BeautifulSoup
from csv import writer

response=requests.get("https://www.rithmschool.com/blog")
soup=BeautifulSoup(response.text,"html.parser")
articles=soup.find_all("article")
with open("blog_data.csv","w") as csv_file:
    csv_writer=writer(csv_file)
    csv_writer.writerow(["title","link","date"])
    for article in articles:
        a_tag=article.find("a")
        title=a_tag.get_text()
        url=a_tag['href']
        date=article.find("time")
        csv_writer.writerow([title,url,date])
        