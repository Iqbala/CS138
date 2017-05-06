#Name: Ali H. Iqbal                                              
#Course: CSC 138                                           
#Due Date: June 20, 2016                                  
#Socket Programming Assignment 1                                           
#Professor: Jun Dai                                      

#include Python's socket library

from socket import *

#define name and port

serverName = 'localhost'
serverPort = 12340

#create UDP socket for server

clientSocket = socket(AF_INET, SOCK_DGRAM)

#get user keyboard input

message = raw_input('Input lowercase sentence:')

#attach server name, port number to message; send into socket.

clientSocket.sendto(message,(serverName, serverPort))

#read reply characters from socket into String

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

#printout received string and close socket

print modifiedMessage

clientSocket.close()
