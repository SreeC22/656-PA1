import socket

# Define client name
client_name = "Client of John Q. Smith"

# Input an integer between 1 and 100 from the user
client_number = int(input("Enter an integer between 1 and 100: "))

# Define server address and port
server_address = 'localhost'
server_port = 6789

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_address, server_port))

# Send the client's name and number to the server
client_message = f"{client_name},{client_number}"
client_socket.send(client_message.encode())

# Receive the message from the server
server_message = client_socket.recv(1024).decode()
server_name, server_number = server_message.split(',')
server_number = int(server_number)

# Display the client's name, server's name, their numbers, and compute the sum
print(f"Client's name: {client_name}, Client's number: {client_number}")
print(f"Server's name: {server_name}, Server's number: {server_number}")
print(f"Sum: {client_number + server_number}")

# Close the client socket
client_socket.close()
