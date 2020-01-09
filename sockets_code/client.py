import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())
port = 1234

server_socket.connect((host,port))


while True:
    smsg = server_socket.recv(1024)
    print("Server --> ",smsg.decode())
    if smsg.decode().strip().lower() == "bye":
        print("Server is saying bye to you")
        server_socket.close()
        break
    cmsg = input("Client --> ")
    server_socket.send(cmsg.encode())
    if cmsg.strip().lower() == "bye":
        print("Client is saying bye")
        server_socket.close()
        break

