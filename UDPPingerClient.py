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

    #Start ping timer
    start_time = time.time()

    #Create ping message and format time
    message = "Ping " + str(ping) + " {}".format(time.strftime("%H:%M:%S", time.localtime(start_time)))

    #Attach message and send to server socket
    clientSocket.sendto(message.encode(), (serverName, serverPort))


    #Try to measure RTT for ping
    try:
        
        #Listen for response from server
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        
        #Pause timer to calculate round-trip time (in seconds)
        return_time = time.time()
        rtt = round(return_time - start_time, 6)
    
        #Output PING results
        print(modifiedMessage.decode() + ": RTT={} s".format(rtt))


    #If timeout error, print 'Request timed out'
    except timeout as err:

        print('Request timed out')
