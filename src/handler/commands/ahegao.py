from .base import Base
import json
from urllib.request import urlopen
from src.config import encoding

class Ahegao(Base):
    name = 'ahegao'
    aliases = ['ahegão', 'ahegao', '🥵']

    def execute(self, command):
        response = urlopen('https://ahegao.egecelikci.com/api')
        data = json.loads(response.read().decode(encoding))
        url = data['msg']

        self.send_photo(command, photo=url)
