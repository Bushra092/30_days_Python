import socket

s = socket.socket()
print("Socket Created")

s.bind(('localhost', 9999))

s.listen(3)

print("Waiting for Connections")

while True:
    c, add  = s.accept()
    
    name = c.recv(1024).decode()
    print("Connected with", add,name)
    c.send(bytes("Welcome To ......", "utf-8"))
    c.close()
