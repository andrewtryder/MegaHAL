Supybot-MegaHAL
===============

Supybot plugin to make your bot talk. Think A.L.I.C.E. or MegaHal.

Warning/Disclaimer

    I must warn you that with any plugin which makes a bot talk, you run a serious risk
    of having the bot banned. Some people go *nuts* when bots talk not on command and
    will ban/perm you and your bot. By default, I have the config registry variables
    set to not talk very much, which can be changed. So, please, make sure that
    you set each individual channel to be respectful of those who own it. Keep
    the probability at 0 if you want the bot to never respond. Consider the code
    in testing since something like this will always encounter bugs.

Description

    What bot is complete without some type of plugin to make it talk?

Instructions

    You need cobe: pip install cobe

    Description of cobe: http://teichman.org/blog/2011/02/cobe.html

    After running my tests with 10+ channels for 1 week, my corpus is about 18Mb. I've not implemented
    a way to labotomize it just yet. I will have to see how it performs when the corpus hits 100MB+

    After that, the requirements are satisfied and this should work fine on Python 2.7+

    I suggest you check out the channel config variables to tweak things like probability and delay.

Inspiration/notes:

    * http://madcow.googlecode.com/svn-history/r1271/trunk/madcow/modules/megahal.py
    * http://gozerplugs.googlecode.com/hg-history/03ccbb46d89f95705e47699281053200c3aaee67/megahal.py
    * https://github.com/pteichman/kibot-modules/blob/master/kibot/modules/cobe.py
    * https://github.com/Spacexplosion/Quaking-Mad-Cow/blob/9c22130ebfdc663666e495df8f81f61bb5fac24a/madcow/modules/megahal.py
    * https://github.com/gsf/supybot-plugins/blob/1ccef4a72411bd14fb3115c520de1c002be8cbce/Supybot-plugins-20060723/Markov/plugin.py
    * https://github.com/bdrewery/PyBorg/blob/master/lib/pyborg/pyborg.py
    * https://github.com/Trixarian/Alia/blob/master/pyborg.py
    * http://git.jamessan.com/?p=Supybot/Markov.git
