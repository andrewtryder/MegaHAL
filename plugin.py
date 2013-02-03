# -*- coding: utf-8 -*-
###
# Copyright (c) 2013, spline
# All rights reserved.
#
#
###
# my libs
import time
import re
import random
import string
# extra supybot
import supybot.ircmsgs as ircmsgs
import supybot.conf as conf
# stock supybot
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
from supybot.i18n import PluginInternationalization, internationalizeDocstring
try:
    from cobe.brain import Brain
except ImportError:
    raise callbacks.Error, 'You need to install cobe. pip install cobe.'

_ = PluginInternationalization('MegaHAL')

@internationalizeDocstring
class MegaHAL(callbacks.Plugin):
    """Add the help for "@plugin help MegaHAL" here
    This should describe *how* to use this plugin."""
    threaded = True
    callAfter = ['MoobotFactoids', 'Factoids', 'Infobot']
    callBefore = ['Dunno']

    def __init__(self, irc):
        self.__parent = super(MegaHAL, self)
        self.__parent.__init__(irc)
        self._brainfile = conf.supybot.directories.data.dirize('MegaHAL.brain')
        self.last_replied = ircutils.IrcDict()

    def die(self):
        self.__parent.die()

    def _updateSentinel(self, channel):
        now = time.time()
        try:
            lastreplied = self.last_replied[channel]
        except KeyError:
            lastupdated = False
            self.last_replied[channel] = now
            self.log.debug("I have not spoke in {0} yet.".format(channel))
            return True

        if lastreplied:
            if now > (lastreplied + self.registryValue('waitTimeBetweenSpeaking', channel)):
                self.log.debug("I spoke more than {0} ago in {1}".format(lastreplied,channel))
                self.last_replied[channel] = now
                return True
            else:
                self.log.debug("I spoke less than {0} ago in {1}".format(lastreplied,channel))
                return False

    def _cleanText(self, text):
        text = text.decode("utf-8")
        text = ircutils.stripFormatting(text)
        text = re.sub("[^abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@.!?;:/%\$§\-_ ]", " ", text) # | re.UNICODE)
        text = re.sub("[ ]+", " ", text)
        text = text.strip()
        return text

    def _learn(self, irc, channel, text, probability):
        text = self._cleanText(text)
        if text:
            if len(text) > 0 and not text.isspace():
                b = Brain(self._brainfile)
                b.learn(text)
        # determine probability to respond.
        if random.randint(0, 100) < probability:
            # if we've randomly determined to talk, check the update time.
            sentinel = self._updateSentinel(channel)
            if sentinel:
                self._reply(irc, channel, text)

    def _reply(self, irc, channel, text):
        self.log.info("Trying to respond in %s" % channel)
        b = Brain(self._brainfile)
        response = b.reply(text).encode('utf-8')
        # delay the response here so we look real?
        irc.queueMsg(ircmsgs.privmsg(channel, response))

    def doPrivmsg(self, irc, msg):
        channel = msg.args[0].lower()
        text = msg.args[1].strip()
        # ignore ctcp, action and only messages in a channel.
        # if txt.startswith(conf.supybot.reply.whenAddressedBy.chars()):
        if ircmsgs.isCtcp(msg) or ircmsgs.isAction(msg) or not irc.isChannel(channel):
            return
        # on to the text. check if we're ignoring the text matching regex here.
        if re.match(self.registryValue('ignoreRegex'), text):
            return
        # should we strip urls from text?
        if self.registryValue('stripUrls'):
            text = re.sub('(http[^\s]*)', '', text)
        # determine probability if addressed or not.
        if callbacks.addressed(irc.nick, msg):
            text = re.sub('(' + irc.nick + '*?\W+)', '', text)
            probability = self.registryValue('probabilityWhenAddressed', channel)
        else:
            probability = self.registryValue('probability', channel)
        # finally, pass to our learn function.
        self._learn(irc, channel, text, probability)

    def corpuslearn(self, irc, msg, args, text):
        text = self._cleanText(text)
        if text and len(text) > 1 and not text.isspace():
            irc.reply("I am learning: {0}".format(text))
            b = Brain(self._brainfile)
            b.learn(text)
        else:
            irc.reply("After sanitizing, I did not have any text to learn.")
    corpuslearn = wrap(corpuslearn, [('checkCapability', 'admin'), ('text')])

    def corpusreply(self, irc, msg, args, text):
        b = Brain(self._brainfile)
        response = b.reply(text).encode('utf-8')
        irc.reply(response)
    corpusreply = wrap(corpusreply, [('checkCapability', 'admin'), ('text')])

Class = MegaHAL


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=250:
