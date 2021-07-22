import requests

# r = requests.get("https://imgs.xkcd.com/comics/python.png")

# print(r)
# print(r.text)
# print(r.content)

# with open("comic.png", "wb") as f:
# 		f.write(r.content)

# print(r.status_code)
# print(r.ok)
# print(r.headers)

# payload = {"page": 2, "count": 25}
# r = requests.get("https://httpbin.org/get", params=payload)

# print(r.text)
# print(r.url)

r = requests.post("https://httpbin.org/post", data={"username": "ariban900", "password": "123456"})

print(r.text)