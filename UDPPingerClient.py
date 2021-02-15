# UDPPingerClient.py
from socket import *
import time

#Set server address to vars
serverName = 'localhost'
serverPort = 12000


#Build for loop to ping the server 10 times
for ping in range(1, 11):

    # Create a UDP socket and set 1 second timeout
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(1)

    #Create ping message
    message = "Ping " + str(ping)

    #Start ping timer
    start_time = time.time()

    #Attach message and send to server socket
    clientSocket.sendto(message.encode(), (serverName, serverPort))


    #Try to measure RTT for ping
    try:
        
        #Listen for response from server
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        
        #Pause timer to calculate round-trip time (in seconds)
        return_time = time.time()
        rtt = return_time - start_time
    
        #Output PING results
        print(modifiedMessage.decode() + " {}".format(rtt))


    #If timeout error, print 'Request timed out'
    except timeout as err:

        print('Request timed out')
