def help():
  return "This is a test command."
async def exec(req):
  await req.reply("Tested! Arguments: " + req.argument)
