import socket

valid_users = {"Mahmood Yousaf":"hi123","Abdullah Tahir":"by123","Qazi Asalan Shah":"no123"}

Address = "localhost"

port = 5050

s = socket.socket()

s.bind((Address,port))

s.listen(5)
print("Listening for client")
while True:
    c,addr = s.accept()
    print("Client connected ",addr)
    userName = c.recv(1024)
    print("Username received from client ",userName.decode("utf-8"))
    password = c.recv(1024)
    print("Password received from client ",password.decode("utf-8"))
    userName = userName.decode("utf-8")
    password = password.decode("utf-8")
    if userName in valid_users:
        print("User Name is successfully validated")
        check = valid_users[userName]
        if check == password:
            print(("Password is successfully validated"))
            print("Client is authurized ")
            c.send("1".encode("utf-8"))
        else:
            print("Password is incorrect")
            c.send("0".encode("utf-8"))
    else:
        print("Username is invalid")
        c.send("0".encode("utf-8"))