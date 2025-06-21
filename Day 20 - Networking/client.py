import socket


c = socket.socket() 
c.connect(('localhost', 9999))

print(c.recv(1024).decode())
name = input('Enter a name')
c.send(bytes(name,"utf-8"))

print("Connected to server")