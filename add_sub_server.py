# Import socket module
import socket

# Here we use localhost ip address
# and port number
LOCALHOST = socket.gethostbyname(socket.gethostname())
ADD_SUB_SERVER_PORT = 5051
MUL_DIV_SERVER_PORT = 5052
MAIN_SERVER_PORT = 5050
FORMAT = 'utf-8'

# calling server socket method
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, ADD_SUB_SERVER_PORT))

server.listen()
print("ADD_SUB_Server started")
print("Waiting for client request..")
# Here server socket is ready for
# get input from the user
clientConnection, clientAddress = server.accept()
print("Connected client :", clientAddress)
msg = ''

def calculate(exp):
    result = 0
    operation_list = exp.split()
    
    print(operation_list)
    oprnd1 = operation_list[0]
    operation = operation_list[1]
    oprnd2 = operation_list[2]

    # here we change str to int converstion
    num1 = int(oprnd1)
    num2 = int(oprnd2)
    # Here we are perform basic arithmetic operation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    return result

def handle_client(client):
    connected = True
    while connected:
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
    # Here we change int to string and
    # after encode send the output to client

clientConnection.close()
