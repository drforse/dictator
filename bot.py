# -*- coding: utf-8 -*-
import os
import telebot
import time
import random
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
import traceback

bpl_group_id = 1250245627
token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['infomsg'])
def getinfo(m):
    bot.send_message(m.chat.id, str(m))        
@bot.message_handler(commands=['mute'])
def mutee(m):
    if m.chat.id!=m.from_user.id:
      try:
        if m.from_user.id in GLOBALADMINS and m.reply_to_message.from_user.id not in GLOBALADMINS:
            text=m.text.split(' ')
            try:
                timee=text[1]
                i=int(timee[:-1])
                number=timee[len(timee)-1]
            except:
                i=0
                number='m'
            
            untildate=int(time.time())
            if number=='m':
                untildate+=i*60
                datetext='минут'
            if number=='h':
                untildate+=i*3600
                datetext='часов'
            if number=='d':
                untildate+=i*3600*24
                datetext='дней'
                           
            print(untildate)
            
            if m.reply_to_message!=None:
                ahref = '[' +m.reply_to_message.from_user.first_name + ']' + '(tg://user?id=' +  str(m.reply_to_message.from_user.id) + ')'
                bot.restrict_chat_member(can_send_messages=False, user_id=m.reply_to_message.from_user.id, chat_id=m.chat.id, until_date=untildate)
                if i==0:
                    text='🔇Поставила ' + ahref + ' в угол навсегда.'
                else:
                    text='🔇Поставила ' + ahref + ' в угол на '+str(i)+' '+datetext+'.'
                bot.send_message(m.chat.id, text, parse_mode='Markdown')
        else:
            bot.send_message(m.chat.id, 'Да как ты разговариваешь со старшими!')
      except Exception as e:
        bot.send_message(m.chat.id, 'Голова болит...')
        
print('7777')
bot.send_message(bpl_group_id,'Доброе утро, страна!')
bot.polling(none_stop=True,timeout=600)

