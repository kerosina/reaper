from Libs import toggles,config
from Backbone import discord
import time,asyncio

def help():
  return "Wipe server's channels"
async def exec(req):
  if req.guild == None and toggles.nukeserverid == None:
    await req.reply("Variables not set. Make sure to set nukeserverid with " + config.prefix + "set or run this command in a guild." )
    return
  if toggles.nukeserverid == None:
    toggles.nukeserverid = req.guild.id
  await req.delete() 
  await req.embed("Wiping all channels") 
  for channel in req.guild.channels:
    try:
      asyncio.create_task(channel.delete())
      time.sleep(0.1)
    except:
        pass
    
