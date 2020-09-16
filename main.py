#import socket module
from socket import *
import sys # In order to terminate the program

''' AF_INET is the Internet address family for IPv4. 
SOCK_STREAM is the socket type for TCP, the protocol 
that will be used to transport our messages in the network '''
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
#Fill in start
HOST = '127.0.0.1' #set up the IP address
PORT = 6789        #Set up the port
serverSocket.bind((HOST, PORT)) #associate the socket with the host and port
serverSocket.listen()

print(f'the web server is up on port: {HOST}:{PORT}')
#Fill in end
while True:
 #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()#Fill in start #Fill in end
    try:
        message = connectionSocket.recv(1024) #Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()#Fill in start #Fill in end

         #Send one HTTP header line into socket
         #Fill in start
        connectionSocket.send(bytes('HTTP/1.1 200 OK', 'UTF-8'))
        # connectionSocket.send(bytes(outputdata,'UTF-8'))
         #Fill in end
         #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
         #Send response message for file not found

         #Fill in start
         connectionSocket.send(bytes('HTTP/1.1 404 Not Found', 'UTF-8'))
         # Fill in end

         # Close client socket

         # Fill in start
         connectionSocket.close()
         # Fill in end

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data