#Name: Ali H. Iqbal                                              
#Course: CSC 138                                           
#Due Date: June 20, 2016                                  
#Socket Programming Assignment 1                                           
#Professor: Jun Dai                                      

#include socket library

from socket import *

#create an INET, STREAMing socket

serverPort = 12340

#create UDP socket

serverSocket = socket(AF_INET, SOCK_DGRAM)

# now connect to the web, server on port #80 
# bind socket to local port number 12340

serverSocket.bind(('', serverPort))

#printout message

print 'The server is ready to receive'

#loop
while 1:

    #read from UDP socket into message, getting client's address (client IP and port)

    message, clientAddress = serverSocket.recvfrom(2048)
    
    modifiedMessage = message.upper()
    
    #send upder case string back to this client
  
    serverSocket.sendto(modifiedMessage, clientAddress)
