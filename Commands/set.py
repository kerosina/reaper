from Libs import toggles
import json
def help():
  return "Get a toggle's value"
async def exec(req):
  att = req.argument.partition(' ')[2]
  try:
    att = json.loads(att.lower())
  except:
    pass
  setattr(toggles,req.argument.split(" ")[0],att)
  tosend=""
  for toggle in dir(toggles):
    if not toggle.startswith("_"):
      tosend+="\n"+toggle+"->"+str(getattr(toggles,toggle))
  await req.embed(str(tosend[1:]))
