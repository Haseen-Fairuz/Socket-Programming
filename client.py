import socket
c=socket.socket()
addr=input("Enter IP address:")
c.connect((addr,5055))
print("\n OPERATIONS")
print("\n1-->create a file(create)")
print("\n2-->read a file(cat)")
print("\n3-->write a file(edit)")
print("\n4-->delete a file(delete)")
print("\n5.exit\n")
while True:
    i=input("Enter operation:")
    c.send(bytes(i,"utf-8"))
    if(i.startswith("edit")):
        req=input("Enter the string to be added:")
        c.send(bytes(req,"utf-8"))
    elif(i=='exit'):
        quit()
        c.close()
    file1=c.recv(1024).decode()
    print(file1)
         
        
                     
