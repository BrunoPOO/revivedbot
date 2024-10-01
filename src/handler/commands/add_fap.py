from src.handler import commands
from .base import Base
import json, os.path
from src.config import config

FAP_LIST_PATH = os.path.abspath(os.path.dirname(__file__)) + '/../fap_controller/fap_list.json'
MAIN_GROUP_ID = -1001365583838

class Addfap(Base):
    aliases = ['add_fap', 'remove_fap', 'list_fap']
    gods = config.getlist('bot', 'god_mode', type=int)

    def execute(self, command):
        fap_list = json.loads(open(FAP_LIST_PATH, 'r', encoding='utf-8').read())
        faps = fap_list['fap_list']
        try:
            if not self.__is_admin(command) and not command.is_private():
                return self.reply(command, "Você não tem permissão para usar este comando.")

            if command.is_private():
                return self.reply(command, "Você não pode utilizar este comando aqui.")

            if not self.__is_main_group(command):
                return self.reply(command, "Comando não disponivel no chat atual.")

            if len(command.args) == 0 and not command.name == 'list_fap':
                raise IndexError

            if command.name == 'add_fap':
                tag = ' '.join(command.args)
                if(tag not in faps):
                    fap_list['fap_list'].append(tag)
                    #self.reply(command, tag)
                    json.dump(fap_list, open(FAP_LIST_PATH, 'w', encoding='utf-8'), indent= 4)
                    return self.reply(command, "Nova tag adicionada: " + tag)
                else:
                    return self.reply(command, "Tag já adicionada na lista")

            if command.name == 'remove_fap':
                tag = ' '.join(command.args)
                if(tag not in faps):
                    return self.reply(command, "Tag não encontrada")
                else:
                    fap_list['fap_list'].remove(tag)
                    json.dump(fap_list, open(FAP_LIST_PATH, 'w', encoding='utf-8'), indent= 4)
                    return self.reply(command, "Tag removida: " + tag)
            if command.name == 'list_fap':
                tag_list = '\n'.join(faps)
                return self.reply(command, tag_list)
        except (IndexError, ValueError):
            self.reply(command, """Uso do comando:
/add_fap <tag>
/remove_fap <tag> para deletar""")

    #Sim copiado do moderate
    def __is_admin(self, entity):
        user_id = entity.message.from_user.id
        admin_ids = list(map(lambda m: m.user.id, self.bot.get_chat_administrators(entity.chat_id)))

        return user_id in admin_ids \
               or user_id in self.gods
    
    def __is_main_group(self, entity):
        group_id = entity.message.chat.id
        if(group_id == MAIN_GROUP_ID):
            return True
        else:
            return False
