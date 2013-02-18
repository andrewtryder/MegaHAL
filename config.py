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
conf.registerGlobalValue(MegaHAL, 'ignoreRegex', registry.String('^[.@!$]', _("""Regex to ignore when learning text. Suggested to keep this as default.""")))
conf.registerGlobalValue(MegaHAL, 'stripUrls', registry.Boolean(True, _("""Remove urls from text so we do not learn them.""")))
conf.registerGlobalValue(MegaHAL, 'stripNicks', registry.Boolean(True, _("""Strip all nicks, including the bots, when learning?""")))
conf.registerChannelValue(MegaHAL, 'probability', registry.NonNegativeInteger(0, _("""Determines the percent of messages the bot will answer.""")))
conf.registerChannelValue(MegaHAL, 'probabilityWhenAddressed', registry.NonNegativeInteger(100, _("""Determines the percent of messages adressed to the bot the bot will answer.""")))
conf.registerChannelValue(MegaHAL, 'waitTimeBetweenSpeaking', registry.NonNegativeInteger(10, _("""Seconds to wait in a channel before speaking again.""")))
conf.registerChannelValue(MegaHAL, 'ignoreWaitTimeIfAddressed', registry.Boolean(True, _("""If directly addressed, should we ignore the wait time?""")))
conf.registerChannelValue(MegaHAL, 'responseDelay', registry.Boolean(True, _("""Delay responding by between 2 and 4 seconds to look more human?""")))
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=250:
