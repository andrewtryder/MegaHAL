###
# Copyright (c) 2013, spline
# All rights reserved.
#
#
###

import supybot.conf as conf
import supybot.registry as registry
from supybot.i18n import PluginInternationalization, internationalizeDocstring

_ = PluginInternationalization('MegaHAL')

def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified himself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('MegaHAL', True)


MegaHAL = conf.registerPlugin('MegaHAL')
conf.registerGlobalValue(MegaHAL,'ignoreRegex',registry.String('^[.@!$]', _("""Regex to ignore when learning text. Suggested to keep this as default.""")))
conf.registerGlobalValue(MegaHAL,'stripUrls',registry.Boolean(True, _("""Remove urls from text so we do not learn them.""")))
conf.registerGlobalValue(MegaHAL,'ignoreChannels',registry.String('', _("""List of #channels, separated by commas, to ignore. Bot will not learn nor reply in them.""")))
conf.registerChannelValue(MegaHAL,'probability',registry.Integer(0, _("""Determines the percent of messages the bot will answer.""")))
conf.registerChannelValue(MegaHAL,'probabilityWhenAddressed',registry.Integer(100, _("""Determines the percent of messages adressed to the bot the bot will answer.""")))
conf.registerChannelValue(MegaHAL,'waitTimeBetweenSpeaking',registry.Integer(10, _("""Seconds to wait in a channel before speaking again.""")))
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=250:
