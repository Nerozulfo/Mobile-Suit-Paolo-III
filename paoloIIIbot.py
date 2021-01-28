import sys, time
import telepot
import wikipedia as wiki
from telepot.loop import MessageLoop

#dizionario letterale di tutto quello che dice il paolobot terzo 
paocabolario = {
    "notevole" : "NOTEVOLE",
    "hawaii" : "AUAAAAAAI",
    "trivellone" : "TRIVELLONE",
}

def handle(msg) :
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
#controlla che una key è presente in un messaggio
    if content_type == 'text':
        if msg['text'].lower().startswith('wiki'):
            wikicerca(bot,msg) 
        elif paocabolario.keys() in  msg['text'].lower():
            pao = paocabolario[msg['text'].lower()]
            bot.sendMessage(chat_id,pao)


def get_wiki(word):
    try:
        return wiki.summary(word)
    except:
        return "Not Found"


def wikicerca(bot, msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    
    #msgt= msg['text'].lower()
    
    #senderName= msg['first_name']
    #print("{}: {}".format(senderName, msg))

    if content_type == 'text'and msg['text'].lower().startswith('wiki'):
        bot.send_message(chat_id, get_wiki(msg['text'].lower()[5:]))
        print("Bot: Wikipedia summery of {}".format(msg[5:]))
    else:
        bot.send_message(chat_id, "Invalid command")
        print("Bot: Invalid command")

bot = telepot.Bot ("1518683321:AAEGRon3JfNklr_FgUTHGP8mMeXPHYpCe9c")
MessageLoop(bot,handle).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10)
