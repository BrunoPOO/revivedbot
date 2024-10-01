from .base import Base
from src.utils import random_element
import json, os.path

FAP_LIST_PATH = os.path.abspath(os.path.dirname(__file__)) + '/../fap_controller/fap_list.json'
FAP_RANK_PATH = os.path.abspath(os.path.dirname(__file__)) + '/../fap_controller/fap_rank.json'

class Fap(Base):
    name = 'fap'


    def execute(self, command):
        fap_list = json.loads(open(FAP_LIST_PATH, 'r', encoding='utf-8').read())
        fap_rank = json.loads(open(FAP_RANK_PATH, 'r', encoding='utf-8').read())
        tag = fap_list['fap_list']
        users = fap_rank['users']
        user_id = str(command.user_id)
        fap = random_element(tag)
        
        if user_id not in users:
            new_entry = {user_id: {'First Name': command.first_name, 'Most Faps':{fap: 1}}}
            users.update(new_entry)
            fap_rank['users'].update(users)
        else:
            if fap not in users[user_id]['Most Faps']:
                new_fap = {fap: 1}
                users[user_id]['Most Faps'].update(new_fap)
                fap_rank['users'].update(users)
            else:
                fap_count = users[user_id]['Most Faps'][fap] + 1
                users[user_id]['Most Faps'][fap] = fap_count
                fap_rank['users'].update(users)

        json.dump(fap_rank, open(FAP_RANK_PATH, 'w', encoding='utf-8'), indent= 4)
        msg = "O usuário [" + command.first_name + "](tg://user?id=" + str(command.user_id) + ") vai fapar para " + fap

        self.send_markdown(command, msg)
