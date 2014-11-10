import socket

server = "irc.oftc.net"    # server
channel = "#vtcsec"         # channel
botnick = "ayybot"         # nick


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

def joinchan(chan):
    '''
    joins a channel
    '''
    try:
        ircsock.send("JOIN " + chan + "\n")
    except myError as eee:
        print "ircsock.send error: " + eee

def respond_ayy():
    '''
    responds to a user that inputs "Hello mybot"
    '''
    try:
        ircsock.send("PRIVMSG " + channel + " :ayy lmao was detected.\n")
    except myError as eeee:
        print "ircsock.send error: " + eeee


# connect and join the configured channel
try:
    print " ** connecting to the server ** "
    ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ircsock.connect((server, 6667)) # connect to the server using port 6667
    ircsock.send("USER " + botnick + " " + botnick + " " + botnick + " :This is a fun bot!\n")
    ircsock.send("NICK " + botnick + "\n") # assign the nick to the bot
    ircsock.send("JOIN " + channel + "\n")

except myError as connectError:
    print "Error: " + connectError


# receive data from the server
while 1:
    ircmsg = ircsock.recv(2048)   # receive data from the server
    ircmsg = ircmsg.strip('\n\r') # remove unneeded linebreaks
    print ircmsg
   
    if ircmsg.find("PING :") != -1: # if the server pings, respond
        ping()

    if ircmsg.find(":ayy lmao") != -1:
        respond_ayy()

    
