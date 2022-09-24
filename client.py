# Import socket module
import socket

# In this Line we define our local host
# address with port number
LOCALHOST = socket.gethostbyname(socket.gethostname())
MAIN_SERVER_PORT = 5050
# Making a socket instance
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# connect to the server
client.connect((LOCALHOST, MAIN_SERVER_PORT))
# Running a infinite loop
while True:
	print("Example : 4 + 5")
	# here we get the input from the user
	inp = input("Enter the operation in \
the form opreand operator oprenad: ")
	# If user wants to terminate
	# the server connection he can type Over
	if inp == "Over":
		break
	# Here we send the user input
	# to server socket by send Method
	client.send(inp.encode())

	# Here we received output from the server socket
	answer = client.recv(1024)
	print("Answer is "+answer.decode())
	print("Type 'Over' to terminate")

client.close()
