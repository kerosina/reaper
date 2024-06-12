#   ██▀███  ▓█████ ▄▄▄       ██▓███  ▓█████  ██▀███
#  ▓██ ▒ ██▒▓█   ▀▒████▄    ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
#  ▓██ ░▄█ ▒▒███  ▒██  ▀█▄  ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
#  ▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██ ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄
#  ░██▓ ▒██▒░▒████▒▓█   ▓██▒▒██▒ ░  ░░▒████▒░██▓ ▒██▒
#  ░ ▒▓ ░▒▓░░░ ▒░ ░▒▒   ▓▒█░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
#    ░▒ ░ ▒░ ░ ░  ░ ▒   ▒▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
#    ░░   ░    ░    ░   ▒   ░░          ░     ░░   ░
#     ░        ░  ░     ░  ░            ░  ░   ░
import coloredlogs, logging
from Libs import config
logger = logging.getLogger("Reaper")
field_styles = {
    'asctime': {'color': 'green'},
    'hostname': {'color': 'magenta'},
    'processName': {'color': 'red'},
    'process': {'color': 'red'},
    'levelname': {'color': 'yellow', 'bold': True},
}
def install():
  coloredlogs.install(level=config.parsed["Preferences"].get("LogLevel","Info"),logger=logger, field_styles=field_styles)

