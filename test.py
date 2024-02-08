#Importing Libaries
from telethon import TelegramClient, events, sync
import info

#Client connection
client = TelegramClient('session_1', info.api_id, info.api_hash)
print ('connected')
#@client.on(events.NewMessage)
#async def my_event_handler(event):
    #if 'Partner found' in event.raw_text:
        #await event.reply('ce 19, sange\n@ssyaindyra')
    #if 'Partner found' in event.raw_text:
        #await event.reply('/next')
    #if 'Your partner' in event.raw_text:
        #await event.reply('/search')

@client.on(events.NewMessage(pattern='(?i)hi|hello')) 
async def handler(event):
    await event.respond('Hey!')
    

@client.on(events.NewMessage(pattern='(?i)Partner'))

async def handler(event):

    await event.respond('ce 19,sange\n@ssyaindyra')

@client.on(events.NewMessage(pattern='(?i)Partner'))

async def handler(event):

    await event.respond('/next')
    
@client.on(events.NewMessage(pattern='(?i)Your partner'))

async def handler(event):

    await event.respond('/search')
    
client.start()
client.run_until_disconnected()