from .base import Base
import random


class Corno(Base):
    name = 'soucorno'

    def execute(self, command):
        pc = random.randint(0, 100)
        msg = "[" + command.first_name + "](tg://user?id=" + str(command.user_id) + ") é " + str(pc) + "% corno!"
        self.send_markdown(command, msg)

