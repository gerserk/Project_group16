import telepot
import time
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import json
from telepot.loop import MessageLoop
from personal import *

class MyBot:
    def __init__(self,token):
        self.token=token
        self.greeting_message = "Hello! Welcome to our smart airport. Please choose where you are from the menu"
        self.bot = telepot.Bot(token)
        #self.bot.message_loop(self.on_chat_message)#{'chat':self.message_handler,'callback_query':self.on_callback_query})
        MessageLoop(self.bot, {'chat': self.on_chat_message, 
                  'callback_query': self.on_callback_query}).run_as_thread()
         
            
    def on_chat_message(self,msg):
        content_type, chat_type, chat_id= telepot.glance(msg)
        self.chat_id=chat_id
        self.bot.sendMessage(chat_id,text=self.greeting_message)
        time.sleep(5)
        sec=msg['text']
        if sec=='/before':
            self.Before_checks(msg)
        if sec=='/after':
            self.After_checks(msg)
        
        
    def Before_checks(self, message):
        content_type, chat_type, chat_id= telepot.glance(message)
        
        button1=InlineKeyboardButton(text='shops',callback_data='Bshops')
        button2=InlineKeyboardButton(text='Cafe',callback_data='Bcafe')
            
        keyboard1=InlineKeyboardMarkup(inline_keyboard=[
            [button1],
            [button2],
            ])
        
        self.bot.sendMessage(chat_id,text='what kind of service?',reply_markup=keyboard1)
                
        time.sleep(5)
        
        
    def After_checks(self, message): 
        content_type, chat_type, chat_id= telepot.glance(message)
        
        button1=InlineKeyboardButton(text='shops',callback_data='Ashops')
        button2=InlineKeyboardButton(text='Cafe',callback_data='Acafe')
            
        keyboard1=InlineKeyboardMarkup(inline_keyboard=[
            [button1],
            [button2],
            ])
        
        self.bot.sendMessage(chat_id,text='what kind of service?',reply_markup=keyboard1)
        
        time.sleep(5)
    
    def on_callback_query(self,message):
        query_id, from_id, query_data=telepot.glance(message,flavor='callback_query')
        if(query_data=='Ashops'):
            self.bot.sendMessage(self.chat_id,text='Here is a list of all the shops with their description:')
        if(query_data=='Bshops'):
            self.bot.sendMessage(self.chat_id,text='Here is a list of all the shops with their description:')
            
        

if __name__ == "__main__":
    
    a=MyBot(TOKEN)
    time.sleep(300)
    
  
