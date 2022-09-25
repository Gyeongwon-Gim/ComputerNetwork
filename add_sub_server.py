import socket

# use localhost ip address with port number
LOCALHOST = socket.gethostbyname(socket.gethostname())
ADD_SUB_SERVER_PORT = 5051
MUL_DIV_SERVER_PORT = 5052
MAIN_SERVER_PORT = 5050
FORMAT = 'utf-8'

# create TCP welcoming socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, ADD_SUB_SERVER_PORT))

# server bigins listening for incoming TCP requests
server.listen()
print("ADD_SUB_Server started")
print("Waiting for client request..")
clientConnection, clientAddress = server.accept()
print("Connected client :", clientAddress)
msg = ''

def calculate(exp):
    result = 0
    operation_list = exp.split()
    oprnd1 = operation_list[0]
    operation = operation_list[1]
    oprnd2 = operation_list[2]

    # change str to int converstion
    num1 = int(oprnd1)
    num2 = int(oprnd2)
    
    # perform basic arithmetic operation : addition, subtraction
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    return result

def handle_client(client):
    connected = True
    while connected:
        # change int to string and
        # after encode send the output to main server
        msg = client.recv(1024).decode(FORMAT)
        result = str(calculate(msg))
        client.send(result.encode(FORMAT))

# Running infinite loop
while True:
    if msg == 'Over':
        print("Connection is Over")
        break

    print("Equation is recievied")
    handle_client(clientConnection)

    print("Send the result to client")
    
clientConnection.close()
