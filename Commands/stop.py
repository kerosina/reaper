import importlib,pkgutil
from Libs import stringutils,toggles
def help():
  return "Stop all commands that can be stopped"
async def exec(req):
  toggles.nuke=False
  toggles.spam=False
  toggles.pingspam=False
  await req.embed("Stopped running commands!")
