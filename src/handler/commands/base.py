import logging
from abc import ABC, abstractmethod


class Base(ABC):
    name = None
    aliases = []
    bot = None

    @abstractmethod
    def execute(self, command):
        pass

    def reply(self, command, text):
        logging.debug("Command %s: %s" % (str(command), text))

        self.bot.send_message(
            chat_id=command.chat_id,
            reply_to_message_id=command.message.message_id,
            text=text
        )

    def reply_with_photo(self, command, photo, caption = ""):
        self.bot.send_photo(chat_id=command.chat_id, reply_to_message_id=command.message.message_id, photo=photo, caption=caption)
    

    def send_photo(self, command, photo):
        self.bot.send_photo(chat_id=command.chat_id, photo=photo)

    def send_markdown(self, command, text):
        self.bot.send_message(
            chat_id=command.chat_id,
            text=text,
            parse_mode='Markdown'
        )

    def send_sticker(self, command, sticker):
        self.bot.send_sticker(chat_id=command.chat_id, sticker=sticker)
