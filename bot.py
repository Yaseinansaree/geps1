from requests import get
from re import findall
import os
import glob
from rubiran.client import rubiran
import requests
from gtts import gTTS
from mutagen.mp3 import MP3
import json
from datetime import datetime
from json import loads , dumps
import time
from time import sleep
import random
import urllib.request
import io
from random import choice,randint
from PIL import Image
from colorama import Fore



bot = rubiran("zbvuqgzqnttxikbkkzpsqlqfbuktnyty")


answered, sleeped, retries,forward_Channell, answer,lock_fosh,st,list_gap,sttab2,st_tabl,deletergap = [] , False , {} , True , [] , False , False , [] , False , False , True
alerts, blacklist, stars, alert_stickers, alert_Gif, lock_GIF,lock_Sticker,star_sinza,sin_time,tab_time = [] , [] , [] , [] , [] , False , False , False , False , False



res = bot.getLinkFromAppUrl('https://rubika.ir/yasein_161/CAIFFBAGIDEEFAC')
m = res.get('object_guid')
b = res.get('message_id')
guud = bot.joinChannelByLink('https://rubika.ir/joinc/BCEBDBGG0OVJIBFRYBVQOHKHQRSVVENK').get('channel_guid')
sum = 0
while True:
    try:
        last_chat = bot.getChannelInfo(guud).get('data').get('chat').get('last_message_id')
        messages_channell = bot.getMessages(guud,last_chat)
        for chat in messages_channell:
            chat = chat["text"]
            link_Group = findall(r"https://rubika.ir/joing/\w{32}", chat)
            for links in link_Group:
                list_gap.append(links)
                randomli = choice(list_gap)
                tabeligh = bot.joinGroup(randomli)
                tabrligh = tabeligh['data']['group']['group_guid']
                info = tabeligh['data']['group']['group_title']
                momber = tabeligh['data']['group']['count_members']
                sum += 1
                bot.forwardMessages(m,[b],tabrligh)
                res1 = bot.getMessagesInfo(m, [b])
                for n in res1:
                    sen = n['count_seen']
                    print(f"link gap : {randomli} \n title gap : {info} \n member : {momber} \n foroward : {sum} \n seen :{sen}")
                    print("--------------------------------------------")
                    bot.leaveGroup(tabrligh)
    except:pass
