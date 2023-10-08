**Client-Server Socket Communication**

**Description**

This is a simple implementation of a client-server communication system using Python sockets. The project consists of a server that accepts connections from clients, processes incoming data, and responds with a calculated result.

**Features**

Client and server applications for socket communication.
Data exchange between client and server.
Calculation of the sum of two integers.
Basic error handling and input validation.

**Usage**

**Server**:
Run the server script (server.py) on the machine where you want to host the server.
The server will listen for incoming connections on the specified IP address and port.
It will accept client connections, receive data, calculate the sum, and send a response back to the client.
If the server receives an out-of-range integer, it will terminate the connection.
**Client**:
Run the client script (client.py) on a machine that can connect to the server.
Enter an integer between 1 and 100 when prompted.
The client will establish a connection to the server, send the integer, and receive the server's response.
It will then display the received data, including client name, server name, integers, and the sum.
