from Backbone import discord
import time
def help():
  return "Purge a selected number of your own messages"
async def exec(req):
  if not req.argument.isdigit():
    await req.reply("Invalid number!")
    return
  async for message in req.channel.history(limit=int(req.argument)):
    if message.author.id == discord.client.user.id:
      try:
        await message.delete()
      except:
        pass
      time.sleep(0.3)
