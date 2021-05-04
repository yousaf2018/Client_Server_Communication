import socket
import time 
address = "www.google.com"

port = 80

c = socket.socket()

c.connect((address,port))

request = "Hi google how are you i am not rebot"
print("Connected with server")
c.send(request.encode("ascii"))
print("Hi")
data = c.recv(1024)
print(data)
