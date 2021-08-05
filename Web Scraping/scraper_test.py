from requests_html import HTMLSession

session = HTMLSession()
r = session.get("http://testphp.vulnweb.com/artists.php")

# for link in r.html.absolute_links:
#   print(link if "?artist=" in link else "")
r.html.render()

content = r.html.find("#content")[0]
artists = content.find(".story")
for artist in artists:
  print(artist.find("a", first=True).find("h3", first=True).text)


# print(r.html.find("#content", first=True).find(
#     ".story", first=True).find("p", first=True).text)


# print(r.html.text)
