from .base import Base


class Start(Base):
    name = 'brunita'

    def execute(self, command):
        self.reply(command, 'OIkkk! :3')
