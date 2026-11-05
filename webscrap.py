# pip install beautifulsoup4
# pip install requests
# ip install pandas

import requests
from bs4 import BeautifulSoup

# #Fetch the web pages

url="https://edunetfoundation.org/"
response=requests.get(url)

#check if the request is successfull
# if response.status_code == 200:
#     print("Successfully fetched the web page")
# else:
#     print("Failed")

# prase the HTML Content
soup=BeautifulSoup(response.text,"html.parser")

# extract Data

title=soup.title.string
print(f"Page Title:{title}")

# extract hyperlink

links=soup.find_all("a")
for link in links:
    href =link.get("href")
    text= link.get_text
    print(f"Link text: {text},URL:{href}")

import csv

links = soup.find_all("a", href=True)

with open("website_links.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow(["Link Text", "URL"])

    for link in links:
        href = link.get("href", "").strip()
        text = link.get_text(" ", strip=True)

        if not text:
            text = link.get("title") or link.get("aria-label") or "No Link Text"

        if href and href != "#":
            writer.writerow([text, href])

print("Links saved successfully!")