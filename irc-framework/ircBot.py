#! /usr/bin/env python

"""
    author:
    filename:
    description:
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
   
import irc.bot
import irc.strings
from irc.client import ip_numstr_to_quad, ip_quad_to_numstr

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
        print "Status: Received private message from " + str(e.source.nick) + " with command '" + str(e.arguments[0]) + "'"
        self.do_command(e, e.arguments[0])

    def on_pubmsg(self, c, e):
        """
        If a public message is received, perform command specified
        """
        a = e.arguments[0].split(":", 1)
        if len(a) > 1 and irc.strings.lower(a[0]) == irc.strings.lower(self.connection.get_nickname()):
            self.do_command(e, a[1].strip())
        print "Status: Received public message from " + str(e.source.nick) + " with command '" + str(e.arguments[0]) + "'"

        return


    def do_command(self, e, cmd):
        print "do command"
        nick = e.source.nick
        c = self.connection

        # here a variety of commands are added to the bot with various actions
        if cmd == "disconnect":
            self.disconnect()

        elif cmd == "die":
            self.die()

        else:
            c.notice(nick, "Not understood: " + cmd)

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
