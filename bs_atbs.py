# Let's get all the chapters from Automate the Boring Stuff
import requests, bs4, webbrowser, sys

url = r'https://automatetheboringstuff.com'
home_page = requests.get(url, verify=False)
home_page.raise_for_status()

atbs = bs4.BeautifulSoup(home_page.text)

# The chapters are all links within an unordered list
links = atbs.select('ul li a')

# Furthermore, all the chapters have "Chapter" in the text of the tag
chapter_links = []
for link in links:
    if "Chapter" in link.string:
        chapter_links.append(link.get('href'))

print(chapter_links)

try:
    if sys.argv[1] == "--open":
        for link in chapter_links:
            webbrowser.open_new_tab(url + link)
except IndexError:
    print("extra arguments not included")