from rubpy import Bot
from requests import get
from _thread import start_new_thread
import time

def answer(bot,chat,msg,):
	try:
		bot.sendMessage(chat['object_guid'], get('http://api.hajiapi.tk/sokhan?text='+msg).text, message_id=chat['last_message']['message_id'])
	except:pass
	
bot=Bot(auth="ufmzlqqnvusrycuxbdejfgxwlrgwbond",)
answered=[]
bot_guid=("u0DQXtB0dec2771cdd3897c499a8f24b")
while(1):
	try:
		time(7)
		for chat in bot.getChatsUpdate():
			
				if 'SendMessages' in chat['access'] and chat['last_message']['type']=='Text':
					msg:str=chat['last_message']['text']
					if not chat['object_guid']+chat['last_message']['message_id']in answered:
						if not chat['last_message']['author_object_guid']==bot_guid:
							if msg:
								start_new_thread(answer,(bot,chat,msg,))
							answered.append(chat['object_guid']+chat['last_message']['message_id'])
	except:pass
