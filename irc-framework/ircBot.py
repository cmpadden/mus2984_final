import socket
from time import sleep

"""
TESTED with irc.oftc.net
"""


def ping():
    '''
    responds to server pings
    '''
    try:
        ircsock.send("PONG :Pong\n")
    except myError as e:
        print "ircsock.send error: " + e

def sendmsg(chan, msg):
    '''
    sends a message to a specified channel
    '''
    try:
        ircsock.send("PRIVMSG " + chan + " :" + msg + "\n")
    except myError as ee:
        print "ircsock.send error: " + ee

def connectToIRC(server, port, channel, botnick):
    """
    Goes through the handshake of connecting to an IRC server and channel
    """
    try:
        ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ircsock.connect((server, port)) 
        ircsock.send("USER " + botnick + " " + botnick + " " + botnick + " :MUS2984 Bot!\n")
        ircsock.send("NICK " + botnick + "\n")
        ircsock.send("JOIN " + channel + "\n")

        # print connection stats (-: left aligned, s: string)
        print 
        print "%-50s" %("Connected to IRC")
        print "%-25s%-25s" % ("Server", str(server)+":"+str(port))
        print "%-25s%-25s" % ("Channel", str(channel))
        print "%-25s%-25s" % ("Nick", str(botnick))
        print

        # return the socket
        return ircsock

    except myError as connectError:
        print "Error: " + connectError

def monitorIRC(ircsock):
    """
    Receive data from the server
    """
    while 1:
        ircmsg = ircsock.recv(256)   # receive data from the server
        ircmsg = ircmsg.strip('\n\r') # remove unneeded linebreaks
 
        # if the server pings, respond
        if ircmsg.find("PING :") != -1:
            ping()
        
        # monitor for request using !musbot
        #TODO add threading

        if ircmsg.find(":!musbot") != -1:
            requestNick = ircmsg[1:ircmsg.find('!')] 
            requestMessage = ircmsg[ircmsg.find(":!musbot"):][8:].strip()
           
            # print the nick and request to console
            print "%-25s%-25s%-25s" % ("REQUEST", str(requestNick), str(requestMessage))

# -------------------------------------------------------------- end modules

server = "irc.oftc.net"    # server
port = 6667                # port
channel = "#mus2984"       # channel
botnick = "musBot"         # nick

# connect to the irc
ircsock = connectToIRC(server, port, channel, botnick)

# sleep before monitoring
sleep(5)

# monitor the IRC connection
monitorIRC(ircsock)
