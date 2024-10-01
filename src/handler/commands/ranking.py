from .base import Base
from src.utils import random_element
import codecs, json, os.path

POLE_JSON_PATH = os.path.abspath(os.path.dirname(__file__)) + '/../pole_controller/pole.json'

class Rank(Base):
    name = 'rank'
    
    def execute(self, command):
        sorted_rank = self.update_rank()
        msg = " 🏆 Pole ranking do baú 🏆\n\n"
        for n in sorted_rank:
            msg = msg + n +": " + str(sorted_rank[n]['points']) + "\n"

        self.reply(command, msg)
    
    def update_rank(self):
        pole = json.loads(open(POLE_JSON_PATH, 'r', encoding='utf-8').read())
        ranking = pole['ranking']
        sorted_rank = {key: val for key, val in sorted(ranking.items(), key = lambda ele: ele[1]['points'], reverse= True)}
        return sorted_rank
