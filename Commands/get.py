from Libs import toggles
def help():
  return "Get a toggle's value"
async def exec(req):
  tosend=""
  if req.argument == "":
    for toggle in dir(toggles):
      if not toggle.startswith("_"):
        tosend+="\n"+toggle+"->"+str(getattr(toggles,toggle))
  else:
    tosend="\n"+str(getattr(toggles,req.argument))
  await req.embed(str(tosend[1:]))
