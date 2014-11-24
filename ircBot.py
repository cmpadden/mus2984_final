#! /usr/bin/env python

"""
    dependencies: irc
"""
global asciiArt
asciiArt = ["                      ____        _     _ ",
            "                     |  _ \      | |   | |",
            "  _ __ ___  _   _ ___| |_) | ___ | |_  | |",
            " | '_ ` _ \| | | / __|  _ < / _ \| __| | |",
            " | | | | | | |_| \__ \ |_) | (_) | |_  |_|",
            " |_| |_| |_|\__,_|___/____/ \___/ \__| (_)",
            " "]

# imports required for IRC
import irc.bot
import irc.strings
from irc.client import ip_numstr_to_quad, ip_quad_to_numstr


# imports required for OSC
import interfaceOSC


class musBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port=6667):
        """
        initialize with the channel, nick, server, and port variables
        """
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        self.channel = channel

    def on_nicknameinuse(self, c, e):
        """
        If the nick is in use, register the nick with "_" appended
        """
        print "Status: Nick was in use."
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        """
        Connect to the channel specified
        """
        print "Status: Connecting to " + str(self.channel) + "."
        c.join(self.channel)

    def on_privmsg(self, c, e):
        """
        If a private message is received, perform the command specified
        """
        print "Status: Received private message from " + str(e.source.nick) + " with message '" + str(e.arguments[0]) + "'"
        self.do_command(e, e.arguments[0])

    def on_pubmsg(self, c, e):
        """
        If a public message is received, perform command specified
        """
        # split the first word from the command, and send the rest to the command operation
        a = e.arguments[0].split(" ", 1)
        if len(a) > 1 and a[0] == "!musbot":
            self.do_command(e, a[1].strip())

        return


    def do_command(self, e, cmd):
        nick = e.source.nick
        c = self.connection

        # split the command by spaces
        splitcmd = cmd.split(" ")

        # here a variety of commands are added to the bot with various actions
        if splitcmd[0] == "disconnect":
            self.disconnect()

        elif splitcmd[0] == "die":
            self.die()

        elif splitcmd[0] == "asciiart":
            for line in asciiArt:
                c.notice(nick, line)

        # send the command to OSC for acid note
        elif splitcmd[0] == "acid":
            # check to make sure the command is in the proper format
            if (len(splitcmd) != 2) or (splitcmd[1].isdigit == False):
                c.notice(nick, "Improper command format; Use, '!musbot acid <freq>'")
            else:
                interfaceOSC.sendMessageOSC(splitcmd[1], "/acid")

        # send the command to OSC for snare
        elif splitcmd[0] == "snare":
            interfaceOSC.sendMessageOSC(0, "/snare")

        # send the command to OSC for kick
        elif splitcmd[0] == "kick":
            interfaceOSC.sendMessageOSC(0, "/kick")

        # send the command to OSC for hat
        elif splitcmd[0] == "hat":
            interfaceOSC.sendMessageOSC(0, "/hat")

        else:
            c.notice(nick, "Command not understood: " + cmd)

def main():
   
    try: 
        channel = "#mus2984"
        nickname = "musbot"
        server = "irc.oftc.net"
        port = 6667

        bot = musBot(channel, nickname, server, port)
        bot.start()
    except Exception, detail:
        print "Error in main: " + str(detail)

if __name__ == "__main__":
    '''
    ensures the main function is not executed if module is used in another script
    '''
    main()
