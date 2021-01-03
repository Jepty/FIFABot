import asyncio
import datetime
from telethon import events
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

from config import (API_ID, API_HASH, SESSION_STRING)

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

@client.on(events.NewMessage)  
async def register(event):

    print(event.chat.username)

    if event.chat.username == 'statistika_fifa_penalty_fast':

        with open('log.conf', 'r') as f:
            send_mess = f.read()
            print(send_mess)
            await client.send_message('TesFifBot', send_mess)
  
        msg = event.message.message

        for i in range(len(msg)):
            if msg[i] == "(":
                a = int(msg[i+1])

            if msg[i] == ")":
                b = int(msg[i-1])

        print(a,b)
        total = 0
        try:
            total = a + b
        except:
            pass

        with open ('log.conf', 'w') as f:
            f.write(str(total))
            print (total, ' new')         

@client.on(events.MessageEdited)
async def recallmessage(event):
    print(event.chat.username)
    if event.chat.username == 'statistika_fifa_penalty_fast':
        msg = event.message.message

        for i in range(len(msg)):
            if msg[i] == "(":
                a = int(msg[i+1])

            if msg[i] == ")":
                b = int(msg[i-1])

        print(a,b)
        total = 0
        try:
            total = a + b
        except:
            pass

        with open ('log.conf', 'w') as f:
            f.write(str(total))
            print (total, ' edit') 

if __name__ == '__main__':
    while True:
        try:
            client.start()
            client.run_until_disconnected()
        except:
            pass
