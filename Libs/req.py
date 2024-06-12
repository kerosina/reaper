#   ██▀███  ▓█████ ▄▄▄       ██▓███  ▓█████  ██▀███
#  ▓██ ▒ ██▒▓█   ▀▒████▄    ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
#  ▓██ ░▄█ ▒▒███  ▒██  ▀█▄  ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
#  ▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██ ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄
#  ░██▓ ▒██▒░▒████▒▓█   ▓██▒▒██▒ ░  ░░▒████▒░██▓ ▒██▒
#  ░ ▒▓ ░▒▓░░░ ▒░ ░▒▒   ▓▒█░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
#    ░▒ ░ ▒░ ░ ░  ░ ▒   ▒▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
#    ░░   ░    ░    ░   ▒   ░░          ░     ░░   ░
#     ░        ░  ░     ░  ░            ░  ░   ░
from Libs import config,stringutils
import copy
class Req(object):
    def __init__(self, message):
        self.message = message
    async def reply(self,msg):
      await self.channel.send(msg,delete_after=int(config.parsed["Preferences"].get("DeleteAfter",5)))
    async def embed(self,msg):
      await self.channel.send(stringutils.generate_embed(msg),delete_after=int(config.parsed["Preferences"].get("DeleteAfter",5)))
    def __getattr__(self, attr):
        return getattr(self.message, attr)
def messagetoreq(message):
    req=Req(message)
    req.content = message.content[len(config.prefix):]
    req.command = message.content[len(config.prefix):].split(" ")[0]
    req.argument = message.content[(len(message.content[len(config.prefix):].split(" ")[0])+2):] if (len(message.content) >= (len(message.content[len(config.prefix):].split(" ")[0])+2)) else ""
    req.arguments = req.argument.split(" ")
    return req
