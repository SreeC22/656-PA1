import socket
import random

# Define server name and port
server_name = "Server of John Q. Smith"
server_port = 6789

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind(('', server_port))

# Listen for incoming connections
server_socket.listen(1)
print(f"{server_name} is ready to receive on port {server_port}")

while True:
    # Accept a connection from a client
    connection_socket, addr = server_socket.accept()
    
    # Receive the message from the client
    client_message = connection_socket.recv(1024).decode()
    client_name, client_number = client_message.split(',')
    client_number = int(client_number)
    
    # Check if the received number is out of range
    if client_number < 1 or client_number > 100:
        print("Received out-of-range number. Server will terminate.")
        connection_socket.close()
        break
    
    # Generate a random number between 1 and 100
    server_number = random.randint(1, 100)
    
    # Display the client's number, server's number, and their sum
    print(f"{client_name} connected")
    print(f"Client's number: {client_number}, Server's number: {server_number}, Sum: {client_number + server_number}")
    
    # Send the server's name and number back to the client
    server_message = f"{server_name},{server_number}"
    connection_socket.send(server_message.encode())
    
    # Close the connection socket
    connection_socket.close()

# Close the server socket
server_socket.close()
