from requests_html import HTMLSession

session = HTMLSession()
r = session.get("http://testphp.vulnweb.com/")

for link in r.html.absolute_links:
  print(link)

# print(r.html)
