from aiogram import Bot

class TgSenderBot:
    def __init__(self, token):
        self.bot = Bot(token = token) 
    
    def  send(self, msg, chat_id):
        self.bot.send_message(chat_id=chat_id, text=msg)