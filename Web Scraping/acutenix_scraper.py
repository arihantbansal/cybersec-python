import sys
from requests_html import HTMLSession

from pyfiglet import figlet_format
from colorama import init
from termcolor import cprint

ps_banner = figlet_format("Acutenix Scraper", font="cybermedium")
cprint(ps_banner, 'blue')

print("-" * len(ps_banner.split("\n")[2]))

print("Options for scraping:")
print("1. HREF Links")
print("2. Names of Artists")
print("3. All Categories")
print("-" * len(ps_banner.split("\n")[2]))

option = int(input("Enter option: "))

session = HTMLSession()


def scrape_href(all=True):
  r = session.get("http://testphp.vulnweb.com/")
  links = list(r.html.absolute_links)
  if not all:
    links = [link for link in links if "testphp.vulnweb.com" not in link]
  print("\nLinks: \n")
  for index, link in enumerate(links):
    print(index + 1, link)


def scrape_artists():
  r = session.get("http://testphp.vulnweb.com/artists.php")
  r.html.render()
  content = r.html.find("#content")[0]
  artists = content.find(".story")
  print("\nArtists: \n")
  for artist in artists:
    print(artist.find("a", first=True).find("h3", first=True).text)


def scrape_categories():
  r = session.get("http://testphp.vulnweb.com/categories.php")
  r.html.render()
  content = r.html.find("#content")[0]
  categories = content.find(".story")
  print("\nCategories: \n")
  for category in categories:
    print(category.find("a", first=True).find("h3", first=True).text)


# Match exists only in Py 3.10 so using if else instead
if option == 1:
  print("Do you want to scrape only external links? (y/n)")
  choice = input("")
  if choice.lower() == "y":
    scrape_href(all=False)
  elif choice.lower() == "n":
    scrape_href()
  else:
    print("Invalid choice")
    sys.exit()
elif option == 2:
  scrape_artists()
elif option == 3:
  scrape_categories()
else:
  print("Invalid option")
  sys.exit()
