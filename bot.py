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
adminos_telebotos=['administrator', 'creator']
bpl_group_id = -1001250245627
token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['infomsg'])
def getinfo(m):
    bot.send_message(m.chat.id, str(m))        
@bot.message_handler(commands=['mute'])
def mutee(m):
    if m.chat.id!=m.from_user.id:
      try:
        chat_member = bot.get_chat_member(m.chat.id, m.from_user.id)
        reply_member = bot.get_chat_member(m.chat.id, m.reply_to_message.from_user.id)
        if bot.get_chat_member(m.chat.id, m.from_user.id).status in adminos_telebotos and bot.get_chat_member(m.chat.id, m.reply_to_message.from_user.id).status not in adminos_telebotos:
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
                    text='Кинул ' + ahref + ' в мут навсегда.'
                else:
                    text='Кинул ' + ahref + ' в мут '+str(i)+' '+datetext+'.'
                bot.send_message(m.chat.id, text, parse_mode='Markdown')
        else:
            bot.send_message(m.chat.id, 'Админа нельзя мутить, даже за пенисы.')
      except Exception as e:
        bot.send_message(m.chat.id, 'Вы долбанулись?')
        print(traceback.format_exc())

        
        
@bot.message_handler(commands=['ban'])
def banee(m):
    if m.chat.id!=m.from_user.id:
      try:
        chat_member = bot.get_chat_member(m.chat.id, m.from_user.id)
        reply_member = bot.get_chat_member(m.chat.id, m.reply_to_message.from_user.id)
        if bot.get_chat_member(m.chat.id, m.from_user.id).status in adminos_telebotos and bot.get_chat_member(m.chat.id, m.reply_to_message.from_user.id).status not in adminos_telebotos:
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
                bot.kick_chat_member(user_id=m.reply_to_message.from_user.id, chat_id=m.chat.id, until_date=untildate)
                if i==0:
                    text='Кинул ' + ahref + ' в бан навсегда.'
                else:
                    text='Кинул ' + ahref + ' в бан '+str(i)+' '+datetext+'.'
                bot.send_message(m.chat.id, text, parse_mode='Markdown')
        else:
            bot.send_message(m.chat.id, 'Админа нельзя банить, даже за пенисы.')
      except Exception as e:
        bot.send_message(m.chat.id, 'Вы долбанулись?')
        print(traceback.format_exc())        
        
@bot.message_handler(commands=['unmute'])
def unmutee(m): 
  if m.chat.id!=m.from_user.id:
      try:
        if bot.get_chat_member(m.chat.id, m.from_user.id).status in adminos_telebotos:
            ahref = '[' +m.reply_to_message.from_user.first_name + ']' + '(tg://user?id=' +  str(m.reply_to_message.from_user.id) + ')'
            bot.restrict_chat_member(can_send_messages=True, can_send_other_messages=True, user_id=m.reply_to_message.from_user.id, chat_id=m.chat.id)
            bot.send_message(m.chat.id, 'Анмутил '+ahref+'.', parse_mode='Markdown')
        else:
            bot.send_message(m.chat.id, 'Хм, у тебя нет паспорта! ВДРУГ ТЫ ПЕНИС?')
      except:
        bot.send_message(m.chat.id, 'Вы долбанулись?')
@bot.message_handler(commands=['unban'])
def unmutee(m): 
  if m.chat.id!=m.from_user.id:
      try:
        if bot.get_chat_member(m.chat.id, m.from_user.id).status in adminos_telebotos:
            ahref = '[' +m.reply_to_message.from_user.first_name + ']' + '(tg://user?id=' +  str(m.reply_to_message.from_user.id) + ')'
            bot.unban_chat_member(can_send_messages=True, can_send_other_messages=True, user_id=m.reply_to_message.from_user.id, chat_id=m.chat.id)
            bot.send_message(m.chat.id, 'Анбанил '+ahref+'.', parse_mode='Markdown')
        else:
            bot.send_message(m.chat.id, 'Хм, у тебя нет паспорта! ВДРУГ ТЫ ПЕНИС?')
      except:
        bot.send_message(m.chat.id, 'Вы долбанулись?')        
        bot.send_message(m.from_user.id, traceback.format_exc())        
print('7777')
bot.send_message(bpl_group_id,'Доброе утро, страна!')
bot.polling(none_stop=True,timeout=600)

