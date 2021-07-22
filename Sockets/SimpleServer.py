import socket

s = socket.socket()
print("Socket successfully created")

port = 12345

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests 
# coming from other computers on the network
s.bind(('', port))
print("Socket binded to %s" %(port))

s.listen(5)
print("Socket is listening")

while True:
	c, addr = s.accept()
	print("Got connection from", addr)

	c.send("Thank you for connecting".encode())
	c.close()