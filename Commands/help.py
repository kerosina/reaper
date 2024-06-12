import importlib,pkgutil
from Libs import stringutils
def help():
  return "Show all commands"
async def exec(req):
  tosend=""
  for command in [name for _, name, _ in pkgutil.iter_modules(['Commands'])]:
    tosend+="\n" + command + " | " + importlib.import_module('Commands.'+command).help()
  await req.embed(stringutils.align(tosend[1:],"|"))
