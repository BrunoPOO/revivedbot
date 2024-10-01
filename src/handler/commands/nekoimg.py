from .base import Base
import json
from urllib.request import Request, urlopen
from src.config import encoding

class NekoBotImage(Base):
    name = 'nekoimg'
    aliases = ['nekobot', 'neko']

    def execute(self, command):
        try:
            if len(command.args) == 0:
                return self.reply(command, 'Usage: /nekoimg [img_type].\n\nTypes: hass, hmidriff, pgif, 4k, hentai, holo, hneko, neko, hkitsune, kemonomimi, anal, hanal, gonewild, kanna, ass, pussy, thigh, hthigh, gah, coffee, food, paizuri, tentacle, boobs, hboobs, yaoi\n\nExample: /nekoimg cofee')
            
            img_type = str(command.args[0])

            url_to_open = 'http://nekobot.xyz/api/image?type=' + img_type
            response = urlopen(Request(url=url_to_open, headers={'User-Agent': 'Mozilla/5.0'}))
            data = json.loads(response.read().decode(encoding))
            url = data['message']
            
            self.send_photo(command, photo=url)
                
        except Exception:
            return self.reply(command, 'Usage: /nekoimg [img_type].\n\nTypes: hass, hmidriff, pgif, 4k, hentai, holo, hneko, neko, hkitsune, kemonomimi, anal, hanal, gonewild, kanna, ass, pussy, thigh, hthigh, gah, coffee, food, paizuri, tentacle, boobs, hboobs, yaoi\n\nExample: /nekoimg cofee')
