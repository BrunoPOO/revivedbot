from .base import Base
import json
from src.config import encoding
from urllib.request import urlopen


class Butts(Base):
    name = 'butts'
    aliases = ['(_._)', '(_*_)', '(Y)']

    def execute(self, command):
        response = urlopen('http://api.obutts.ru/butts/5/10/random')
        data = json.loads(response.read().decode(encoding))
        url = 'http://media.obutts.ru/' + data[0]['preview']

        self.send_photo(command, photo=url)
