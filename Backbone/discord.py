#   ██▀███  ▓█████ ▄▄▄       ██▓███  ▓█████  ██▀███  
#  ▓██ ▒ ██▒▓█   ▀▒████▄    ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
#  ▓██ ░▄█ ▒▒███  ▒██  ▀█▄  ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
#  ▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██ ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
#  ░██▓ ▒██▒░▒████▒▓█   ▓██▒▒██▒ ░  ░░▒████▒░██▓ ▒██▒
#  ░ ▒▓ ░▒▓░░░ ▒░ ░▒▒   ▓▒█░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
#    ░▒ ░ ▒░ ░ ░  ░ ▒   ▒▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
#    ░░   ░    ░    ░   ▒   ░░          ░     ░░   ░ 
#     ░        ░  ░     ░  ░            ░  ░   ░     
import discord
from Libs import log,config
from Libs import req as reqlib
from Backbone import handler
import traceback
logger=log.logger
if config.parsed.get("Secrets") == None:
    raise Exception("Invalid configuration. Recreate it.")
if config.parsed["Secrets"].get("Token") == None:
    raise Exception("Invalid configuration. No token.")
class Client(discord.Client):
    async def on_ready(self):
        logger.info('Logged on as '+self.user.name)
        logger.debug('ID: ' + str(self.user.id))
    async def on_message(self, message):
        try:
          logger.debug('Received message ' + message.content + ' from ID ' + str(message.author.id))
          # only respond to ourselves
          if message.author.id != self.user.id or not message.content.startswith(config.prefix):
              return
          req=reqlib.messagetoreq(message)        
          logger.debug('Received command ' + req.content)
          if req.content == 'ping':
              await req.channel.send('pong')
          await handler.handle(req)
          try:
              await message.delete()
          except:
              pass
        except Exception as e:
          logger.error(traceback.format_exc())
client = Client()
def run():
  client.run(config.parsed["Secrets"].get("Token"),log_handler=None)
