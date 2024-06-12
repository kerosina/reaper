import pkgutil,importlib
async def handle(req):
    for command in [name for _, name, _ in pkgutil.iter_modules(['Commands'])]:
        if command==req.command:
            await importlib.import_module('Commands.'+req.command.replace(".","")).exec(req)
