from Libs import toggles,config
from Backbone import discord
def help():
  return "Spam a channel"
async def exec(req):
  if toggles.spamtext == None or toggles.spamchid == None:
    await req.reply("Variables not set. Make sure to set spamtext and spamchid with " + config.prefix + "set." )
    return
  try:
    await req.delete()
  except:
    pass
  toggles.spam = True
  await req.embed("Starting spam (stop it by using " + config.prefix  +"set spam false)")
  while toggles.spam:
    await discord.client.get_channel(int(toggles.spamchid)).send(toggles.spamtext)
