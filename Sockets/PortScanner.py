import pyfiglet
import sys
import socket
import time

ps_banner = pyfiglet.figlet_format("Port Scanner", font="slant")
print(ps_banner)
startTime = time.time()

print("-" * len(ps_banner.split("\n")[2]))

print("Options for scanning:")
print("1. Single port")
print("2. Range of ports")
print("3. All ports")

option = int(input("Enter option: "))


def singlePort(host, port):
  print("-" * len(ps_banner.split("\n")[2]))
  print("Conducting single PORT Scan on {}:{}".format(host, port))
  print("Scan started at: {}".format(time.strftime("%H:%M:%S")))
  print("-" * len(ps_banner.split("\n")[2]))

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  result = s.connect_ex((host, port))
  print("PORT {}, Result: {}".format(port, result))
  if result == 0:
    print("Port {}: Open".format(port))

  s.close()


def rangeOfPorts(host, start_port, end_port):
  print("-" * len(ps_banner.split("\n")[2]))
  print("Conducting range scan on {} from PORT {} to {}".format(
      host, start_port, end_port))
  print("Scan started at: {}".format(time.strftime("%H:%M:%S")))
  print("-" * len(ps_banner.split("\n")[2]))

  for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((host, port))
    if result == 0:
      print("Port {}: Open".format(port))
    s.close()


# Match exists only in Py 3.10 so using if else instead

if option == 1:
  host = input("Enter host website address: ")
  port = int(input("Enter port: "))
  singlePort(host, port)
elif option == 2:
  host = input("Enter host website address: ")
  start_port = int(input("Enter start port: "))
  end_port = int(input("Enter end port: "))
  rangeOfPorts(host, start_port, end_port)
elif option == 3:
  host = input("Enter host website address: ")
  rangeOfPorts(host, 1, 65535)
else:
  print("Invalid option")
  sys.exit()

print('Time taken:', time.time() - startTime)
