from requests_html import HTML, HTMLSession
import csv

with open("simple.html") as html_file:
	source = html_file.read()
	html = HTML(html=source)
	html.render()

print(html.text)

match = html.find("title", first=True)
print(match[0].html)
print(match.text)

match = html.find("#footer", first=True)
print(match.text)

article = html.find("div.article", first=True)
# print(article.text)
headline = article.find("h2", first=True)
summary = article.find("p", first=True)
print(headline.text + "\n" + summary.text)

articles = html.find("div.article")
for article in articles:
	headline = article.find("h2", first=True)
	summary = article.find("p", first=True)
	print(headline.text + "\n" + summary.text + "\n")

match = html.find("#footer", first=True)
print(match.html)

csv_file = open("cms_scrape.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["headline", "summary", "video"])

session = HTMLSession()
r = session.get("https://coreyms.com/")

for link in r.html.absolute_links:
	print(link)

print(r.html)

articles = r.html.find("article")

for article in articles:	
	headline = article.find(".entry-title-link", first=True).text
	print(headline)

	summary = article.find(".entry-content p", first=True).text
	print(summary)

	try:
		vid_src = article.find("iframe", first=True).attrs["src"]
		vid_id = vid_src.split("/")[4].split("?")[0]
		yt_link = f'https://youtube.com/watch?v={vid_id}'
	except Exception as e:
		yt_link = None	
	
	print(yt_link)
	print()

	csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
