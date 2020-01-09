import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())
port = 1234

server_socket.bind((host,port))
server_socket.listen()
print("Server is ready to listen")


client_socket,client_addr = server_socket.accept()
#print(client_socket)
print("Client ip is {} and client port is {}".format(client_addr[0],client_addr[1]))

while True:
    smsg = input("Server --> ")
    client_socket.send(smsg.encode())
    if smsg.strip().lower() == "bye":
        print("Server is saying bye to you")
        server_socket.close()
        client_socket.close()
        break

    cmsg = client_socket.recv(1024)
    print("Client --> ",cmsg.decode())
    if cmsg.decode().strip().lower() == "bye":
        print("Client is saying bye to you")
        server_socket.close()
        client_socket.close()
        break
