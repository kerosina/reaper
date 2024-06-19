from Libs import toggles,config,stringutils,log
from Backbone import discord
import time
def help():
  return "Spam a channel, pinging a select amount of random users in each message."
async def exec(req):
  if toggles.spamtext == None or (toggles.spamchid == None and not req.guild) or toggles.pingspam_useramount == None or toggles.pingspam_cooldown == None:
    await req.reply("Variables not set. Make sure to set spamtext and spamchid with " + config.prefix + "set. For spamchid, you can run this command in a server instead. You can also optionally modify pingspam_useramount or pingspam_cooldown (cooldown in seconds)." )
    return
  if toggles.spamchid == None:
    toggles.spamchid = req.channel.id
  try:
    await req.delete()
  except:
    pass
  toggles.pingspam = True
  await req.embed("Starting ping spam (stop it by using " + config.prefix  +"set pingspam false)")
  while toggles.pingspam:
    for idx, chunk in stringutils.chunks(discord.client.get_channel(int(toggles.spamchid)).guild.members,toggles.pingspam_useramount):
      msgtosp=toggles.spamtext
      for member in chunk:
        msgtosp=msgtosp + " <@!" + str(member.id) + ">"
      await discord.client.get_channel(int(toggles.spamchid)).send(msgtosp)
      time.sleep(toggles.pingspam_cooldown)
