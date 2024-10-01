from .base import Base
from collections import Counter
import json, os.path

FAP_RANK_PATH = os.path.abspath(os.path.dirname(__file__)) + '/../fap_controller/fap_rank.json'

class FapRank(Base):
    name = 'faprank'

    def execute(self, command):
        fap_rank = json.loads(open(FAP_RANK_PATH, 'r', encoding='utf-8').read())
        #user_id = str(command.user_id)
        user_rank = fap_rank['users']
        topfaps = {}
        for n in user_rank:
            for m in user_rank[n]['Most Faps']:
                #print("chegou aqui infelizmetne")
                if m not in topfaps:
                    topfaps[m] =  user_rank[n]['Most Faps'][m]
                else:
                    topfaps[m] +=  user_rank[n]['Most Faps'][m]
                #print("chegou aqui " + str(cn))
                #topfaps[m] = cn
        
        j =  Counter(topfaps)
        tops = j.most_common(3)
        topmsg = ""
        msg = "🏆 - TOP FAPADAS - 🏆\n\n"
        for i in range(3):
            topmsg = topmsg + str(i + 1) + "º - " + tops[i][0] + ": " + str(tops[i][1]) + "\n"
        msg = msg + topmsg + "\n------------------------------------------------------------" 
        rank = ""
        msg = msg + "\n🍆💦 Contador de Fapadas 💦🍆\n\n"
        for n in user_rank:
            #print(n)
            k = Counter(user_rank[n]['Most Faps'])
            highest_fap = k.most_common(1)
            #print('chegou aqui')
            #print(highest_fap)
            #print(user_rank[n]['First Name'] + ":\n" +  highest_fap[0][0] + ": " + str(highest_fap[0][1]))
            rank = rank + "👤 " +  user_rank[n]['First Name'] + ":\n💦" +  highest_fap[0][0] + ": " + str(highest_fap[0][1]) + "\n\n"
        msg = msg + rank
        self.reply(command, msg)
        #sorted_rank = {key: val for key, val in sorted(user_rank.items(), key = lambda ele: ele['Most Faps'][0], reverse= True)}
