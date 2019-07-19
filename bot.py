# -*- coding: utf-8 -*-
import os
import telebot
import time
import random
import threading
from emoji import emojize
from telebot import types
#  Ты ведь его не используешь лол
import traceback
adminos_telebotos=['administrator', 'creator']
bpl_group_id = -1001250245627
token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)
rep300={}
brit_id=850666493
bot_id=730711588
def checkspam(m):
    pass
def botrep():
    if rep300.get(bot_id) == None:
        rep300.update({bot_id:1})
    else:
        lastrep=rep300[bot_id]
        newrep=lastrep+1
        rep300.update({bot_id:newrep})
        
def usrep(usid):
    if rep300.get(usid) == None:
        rep300.update({usid:1})
    else:
        lastrep=rep300[usid]
        newrep=lastrep+1
        rep300.update({usid:newrep})        
@bot.message_handler(commands=['infomsg'])
def getinfo(m):
    checkspam(m)
    bot.send_message(m.chat.id, str(m))
    botrep()
    usrep(m.from_user.id)
@bot.message_handler(commands=['me'])
def meinfo(m):
    checkspam(m)
    usrep(m.from_user.id)
    try:
        test= 'a' + m.from_user.last_name
        lazt_name = m.from_user.last_name
    except:
        lazt_name = ''
    try:
        tts = 'Кличка ебаная: ' + m.from_user.first_name + ' ' + lazt_name + '\nАйди: ' + str(m.from_user.id) + '\nСтатус: ' + bot.get_chat_member(m.chat.id, m.from_user.id).status + '\nРепутация за день (до того момента, пока я не слетел): ' + str(rep300[m.from_user.id])
        bot.send_message(m.chat.id, tts)
        botrep()
    except:
        bot.send_message(m.chat.id, "Напиши сообщение, геище!")
        botrep()
@bot.message_handler(commands=['userinfo'])
def userinfo(m):
    checkspam(m)
    usrep(m.from_user.id)
    try:
        test= 'hui_osla' + m.from_user.last_name
        lazt_name = m.reply_to_message.from_user.last_name
    except:
        lazt_name = ''
    try:
        tts = 'Кличка ебаная: ' + m.reply_to_message.from_user.first_name + ' ' + lazt_name + '\nАйди: ' + str(m.reply_to_message.from_user.id) + '\nСтатус: ' + bot.get_chat_member(m.chat.id, m.reply_to_message.from_user.id).status + '\nРепутация за день (до того момента, пока я не слетел): ' + str(rep300.get(m.reply_to_message.from_user.id, "Он не написал сбщ, ебаклак!"))
        bot.send_message(m.chat.id, tts)
        botrep()
    except:
        bot.send_message(m.chat.id, "Этот гей не написал сообщениее!")     
        botrep()
@bot.message_handler(commands=['mute'])
def mutee(m):
    checkspam(m)
    usrep(m.from_user.id)
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
                botrep()
        else:
            bot.send_message(m.chat.id, 'Админа нельзя мутить, даже за пенисы.')
            botrep()
      except Exception as e:
        bot.send_message(m.chat.id, 'Вы долбанулись?')
        botrep()
        print(traceback.format_exc())

        
        
@bot.message_handler(commands=['ban'])
def banee(m):
    checkspam(m)
    usrep(m.from_user.id)
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
                botrep()
        else:
            bot.send_message(m.chat.id, 'Админа нельзя банить, даже за пенисы.')
            botrep()
      except Exception as e:
        bot.send_message(m.chat.id, 'Вы долбанулись?')
        botrep()
        print(traceback.format_exc())        
        
@bot.message_handler(commands=['unmute'])
def unmutee(m): 
  usrep(m.from_user.id)  
  if m.chat.id!=m.from_user.id:
      try:
        if bot.get_chat_member(m.chat.id, m.from_user.id).status in adminos_telebotos:
            ahref = '[' +m.reply_to_message.from_user.first_name + ']' + '(tg://user?id=' +  str(m.reply_to_message.from_user.id) + ')'
            bot.restrict_chat_member(can_send_messages=True, can_send_other_messages=True, user_id=m.reply_to_message.from_user.id, chat_id=m.chat.id)
            bot.send_message(m.chat.id, 'Анмутил '+ahref+'.', parse_mode='Markdown')
            botrep()
        else:
            bot.send_message(m.chat.id, 'Хм, у тебя нет паспорта! ВДРУГ ТЫ ПЕНИС?')
            botrep()
      except:
        bot.send_message(m.chat.id, 'Вы долбанулись?')
        botrep()
@bot.message_handler(commands=['unban'])
def unmutee(m):
  checkspam(m)
  usrep(m.from_user.id) 
  if m.chat.id!=m.from_user.id:
      try:
        if bot.get_chat_member(m.chat.id, m.from_user.id).status in adminos_telebotos and m.reply_to_message.from_user.id != bot_id:
            ahref = '[' +m.reply_to_message.from_user.first_name + ']' + '(tg://user?id=' +  str(m.reply_to_message.from_user.id) + ')'
            bot.unban_chat_member(can_send_messages=True, can_send_other_messages=True, user_id=m.reply_to_message.from_user.id, chat_id=m.chat.id)
            bot.send_message(m.chat.id, 'Анбанил '+ahref+'.', parse_mode='Markdown')
        else:
            bot.send_message(m.chat.id, 'Хм, у тебя нет паспорта! ВДРУГ ТЫ ПЕНИС?')
            botrep()
      except:
        bot.send_message(m.chat.id, 'Вы долбанулись?')
        botrep()
        bot.send_message(m.from_user.id, traceback.format_exc())        
@bot.message_handler(commands=['giverep'])
def giverep(m):
    checkspam(m)
    usrep(m.from_user.id)
    if m.from_user.id==brit_id:
        reptogive = int(m.text.split(' ', 1)[1])
        whotogive = m.reply_to_message.from_user.id
        if rep300.get(m.from_user.id) != None:
            lastrep=rep300[whotogive]
            newrep=lastrep+reptogive
            rep300.update({whotogive:newrep})
            bot.send_message(m.chat.id, 'Выдал.')
            botrep()
        else:
            lastrep=0
            newrep=lastrep+reptogive
            rep300.update({whotogive:newrep})
            bot.send_message(m.chat.id, 'Выдал.')
            botrep()
    else:
        bot.send_message(m.chat.id, 'Хм, у тебя нет паспорта! ВДРУГ ТЫ ПЕНИС?')
        botrep()
@bot.message_handler()
def msg_handler_text(m):
    usrep(m.from_user.id)
    global x
    if m.from_user.id not in ban:
       x=banns(m.from_user.id, m.chat.id, m.from_user.first_name)
    if x != 0:
        try:
            bot.delete_message(m.chat.id, m.message_id)
        except:
            pass 
    if 'cazino' in m.text and m.from_user.id == brit_id:
        bot.send_message(m.chat.id, 'Эй, игрок, приходи в казино поиграть,\nТы своим не поверишь глазам!\nЖдет тебя впереди деффичентов каскад\nТы готов? Проходите в VIP-заааааааааааал!\n\nЕбаный рооооооооот!\nЭтого казинооооооо!\nЗдесь диллер дурак,\nЁр буллшит фак!\nПорядок другоооооой!\n\nТы где их береееееешь?\nТы дегенераааааааат!\nПорядок у карт\nВ киосках был взяят,\nТы че, долбоеееееееб?')
    try:
        bot.send_message(brit_id, m.from_user.first_name+' '+str(timerss[m.chat.id]['messages']))
    except:
        bot.send_message(brit_id, m.from_user.first_name)
print('7777')
botrep()
bot.send_message(bpl_group_id,'Доброе утро, страна! (Я блять слетел, репутация улетела в пездак)')
x=0
ban=[]
timerss={}

    
    
def banns(id, chatid, name):
    global x
    i=0
    for ids in timerss:
        if timerss[ids]['id']==id:
            i=1
    if i==0:
        timerss.update({id:{'id':id,
                          'messages':0}})
        t=threading.Timer(3, unwarn, args=[id])  # За 15 секунд 5 сообщений твое ограничение? Че за пиздец, лул
        t.start()
    else:
        timerss[id]['messages']+=1
        if timerss[id]['messages']>=4:
            if id not in ban:
                bot.send_message(chatid, 'Деффичент '+name+' купил карты в киоске и стал диллером на 60 секунд.\nПОРЯДОК ДРУГООООООЙ')
            ban.append(id)
            #  Ты ведь ставишь untildate, telegram сам разбанит хммммммммм!
            untildate=int(time.time())
            untildate+=60
            try:
                bot.restrict_chat_member(can_send_messages=False, user_id=id, chat_id=chatid, until_date=untildate)
            except:
                pass
            return 1
    return 0

def unbannn(id, chatid):
    global x
    try:
        ban.remove(id)
        bot.restrict_chat_member(can_send_messages=True, can_send_other_messages=True, user_id=id, chat_id=chatid)
    except:
        pass    
def unwarn(id):
    global x
    try:
        del timerss[id]
    except:
        pass    
print('7777')
bot.polling(none_stop=True,timeout=600)

