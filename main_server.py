import socket

# use localhost ip address with port number
LOCALHOST = socket.gethostbyname(socket.gethostname())
ADD_SUB_SERVER_PORT = 5051
MUL_DIV_SERVER_PORT = 5052
MAIN_SERVER_PORT = 5050
FORMAT = 'utf-8'

#create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, MAIN_SERVER_PORT))

def handle_client(client):
    connected = True
    while connected:
        exp = client.recv(1024).decode(FORMAT)
        result_msg = send(exp)
        client.send(result_msg.encode(FORMAT))
    client.close()

def send(exp):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if '+' in exp or '-' in exp:
        client_socket.connect((LOCALHOST, ADD_SUB_SERVER_PORT))
    elif '*' in exp or '/' in exp:
        client_socket.connect((LOCALHOST, MUL_DIV_SERVER_PORT))

    client_socket.send(exp.encode(FORMAT))

    return_msg = client_socket.recv(1024).decode(FORMAT)
    print(return_msg)
    return return_msg

# server bigins listening for incoming TCP requests
server.listen()
print(f"Main server is listening")

while True:
    client, addr = server.accept()
    handle_client(client)