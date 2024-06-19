from Libs import config
def help():
  return "Debug the bot."
async def exec(req):
  if config.parsed["Preferences"]["LogLevel"].lower() != "debug":
    await req.reply("Program must have LogLevel `debug` to use this command.")
    return
  await req.embed(f"Guild members: {str(req.guild.members)}")
