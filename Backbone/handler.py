import pkgutil,importlib,asyncio
from Libs import log
async def handle(req):
    log.logger.debug("Command argument(s): " + req.argument)
    log.logger.debug("Command argument count: " + str(len(req.arguments)) )
    log.logger.debug("Command argument list:" + "|".join(req.arguments))
    for command in [name for _, name, _ in pkgutil.iter_modules(['Commands'])]:
        if command==req.command:
            asyncio.create_task(importlib.import_module('Commands.'+req.command.replace(".","")).exec(req))
