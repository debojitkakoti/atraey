import logging

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

BACKEND = 'Slack'  # Errbot will start in text mode (console only mode) and will answer commands from there.

BOT_DATA_DIR = r'/root/atraey/bot/data'
BOT_EXTRA_PLUGIN_DIR = '/root/atraey/bot/plugins'

BOT_LOG_FILE = r'/root/atraey/bot/errbot.log'
BOT_LOG_LEVEL = logging.DEBUG

BOT_ADMINS = ('debojitkakoti88', )  # !! Don't leave that to "CHANGE ME" if you connect your errbot to a chat system !!

# The identity, or credentials, used to connect to a server
BOT_IDENTITY = {
    # XMPP (Jabber) mode
    # 'username': 'err@localhost',  # The JID of the user you have created for the bot
    # 'password': 'changeme',       # The corresponding password for this user
    # 'server': ('host.domain.tld',5222), # server override

    ## HipChat mode (Comment the above if using this mode)
    # 'username' : '12345_123456@chat.hipchat.com',
    # 'password' : 'changeme',
    ## Group admins can create/view tokens on the settings page after logging
    ## in on HipChat's website
    # 'token'    : 'ed4b74d62833267d98aa99f312ff04',
    ## If you're using HipChat server (self-hosted HipChat) then you should set
    ## the endpoint below. If you don't use HipChat server but use the hosted version
    ## of HipChat then you may leave this commented out.
    # 'endpoint' : 'https://api.hipchat.com'

    ## Slack mode (comment the others above if using this mode)
    'token': 'xoxb-127650793362-dm43EsCVUqfQscxfDpLBIYXh',

    ## Telegram mode (comment the others above if using this mode)
    # 'token': '103419016:AAbcd1234...',

    ## IRC mode (Comment the others above if using this mode)
    # 'nickname' : 'err-chatbot',
    # 'username' : 'err-chatbot',    # optional, defaults to nickname if omitted
    # 'password' : None,             # optional
    # 'server' : 'irc.freenode.net',
    # 'port': 6667,                  # optional
    # 'ssl': False,                  # optional
    # 'ipv6': False,                 # optional
    # 'nickserv_password': None,     # optional
    ## Optional: Specify an IP address or hostname (vhost), and a
    ## port, to use when making the connection. Leave port at 0
    ## if you have no source port preference.
    ##    example: 'bind_address': ('my-errbot.io', 0)
    # 'bind_address': ('localhost', 0),
}
##########################################################################
# Prefix configuration                                                   #
##########################################################################

# Command prefix, the prefix that is expected in front of commands directed
# at the bot.
#
# Note: When writing plugins,you should always use the default '!'.
# If the prefix is changed from the default, the help strings will be
# automatically adjusted for you.
#
# BOT_PREFIX = '!'
#
# Uncomment the following and set it to True if you want the prefix to be
# optional for normal chat.
# (Meaning messages sent directly to the bot as opposed to within a MUC)
#BOT_PREFIX_OPTIONAL_ON_CHAT = False

# You might wish to have your bot respond by being called with certain
# names, rather than the BOT_PREFIX above. This option allows you to
# specify alternative prefixes the bot will respond to in addition to
# the prefix above.
BOT_ALT_PREFIXES = ('atraey',)

JENKINS_URL = 'http://139.59.12.124:8080/'
JENKINS_USERNAME = 'admin'
JENKINS_PASSWORD = 'admin'

METRIC_INDEX = 'metricbeat'
ES_HOST = 'http://139.59.17.53:9200'
HOST_URL = 'http://139.59.12.124'
