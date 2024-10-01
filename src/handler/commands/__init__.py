from src.handler.commands.base import Base
from src.handler.commands.chance import Chance
from src.handler.commands.get_stats import GetStats
from src.handler.commands.help import Help
from src.handler.commands.moderate import Moderate
from src.handler.commands.ping import Ping
from src.handler.commands.start import Start

from src.handler.commands.boobs import Boobs
from src.handler.commands.ahegao import Ahegao
from src.handler.commands.nekoimg import NekoBotImage
from src.handler.commands.borscht import Borscht
from src.handler.commands.butts import Butts
from src.handler.commands.facepalm import Facepalm
from src.handler.commands.meow import Meow
from src.handler.commands.vzhuh import Vzhuh
from src.handler.commands.woof import Woof
from src.handler.commands.xkcd import XKCD
from src.handler.commands.ranking import Rank
from src.handler.commands.fap import Fap
from src.handler.commands.sendcoffee import SendCoffee
from src.handler.commands.add_fap import Addfap
from src.handler.commands.fap_rank import FapRank
from src.handler.commands.cuck import Corno
from src.handler.commands.hentai import Hentai
from src.handler.commands.funny_and_cute import Loli

commands = {}
for clazz in Base.__subclasses__():
    command_name = getattr(clazz, 'name')
    command_aliases = getattr(clazz, 'aliases')
    instance = clazz()

    if command_name is not None:
        commands[command_name] = instance
    for command_alias in command_aliases:
        commands[command_alias] = instance
