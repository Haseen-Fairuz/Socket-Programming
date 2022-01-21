import socket
import os
s=socket.socket()
print('Socket Created')
s.bind(('',5055))
s.listen(1)
print('Waiting for connections')
c,addr=s.accept()
print("Connected with",addr)
while True:
    a=c.recv(1024).decode().strip()
    if(a.startswith('create')):
        loc=a[7:].strip()
        try:
            f=open(loc,"x")
            content='File Created'
        except:
            content='File Not Created'
        f.write("hello")
        f.close()
    elif(a.startswith('cat')):
        loc=a[4:].strip()
        try:
            f=open(loc,"r")
            content=f.read()
        except:
            content='File cannot be Found'
        f.close()
    elif(a.startswith('edit')):
        loc=a[5:].strip()
        try:
            f=open(loc,"a")
            req=c.recv(1024).decode()
            f.write(req)
            content='File Edited with :'+req
        except:
            content='File cannot be Found'
        f.close()
    elif(a.startswith('delete')):
        loc=a[7:].strip()
        if os.path.exists(loc):
            os.remove(loc)
            content='File Deleted'
        else:
            content='File Cannot be Found'
    elif(a.startswith('exit')):
        c.close()
        s.close()
        quit()
    else:
        content='Invalid Command'
    c.send(bytes(content,"utf-8"))
    print(content)
