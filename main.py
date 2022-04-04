import requests,random,json,os,sys
import flask
import telebot
from telebot import types
from user_agent import generate_user_agent
from config import *
import logging
from config import *
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

call  = types.InlineKeyboardButton(text = "StArT BoT", callback_data = 'Suf')
program = types.InlineKeyboardButton(text='DevelopeR',url='https://t.me/MMPMMMM')
@bot.message_handler(commands=['start'])
def start(message):
	Keyy = types.InlineKeyboardMarkup()
	Keyy.row_width = 2
	Keyy.add(call,program)
	try:
		first = message.chat.first_name
		bot.send_message(message.chat.id,f"*- Hello {first}\n\n- The BoT HunT TikTok\n\n- BY:- @MMPMMMM*",parse_mode="markdown",reply_markup=Keyy)
		pass
	except:
		print('Error Token')
		exit()
@bot.callback_query_handler(func=lambda call: True)
def bin_mos(call):
	#hotmail
	if call.data =="Suf":
		check1(call.message)
	if call.data =="hotmail":
		check10(call.message)
	if call.data =="getmy1":
		getcheck1(call.message)
	if call.data =="getmy11":
		getcheck11(call.message)
	if call.data =="getmy21":
		getcheck21(call.message)
	if call.data =="getmy31":
		getcheck31(call.message)
	#outlook
	if call.data =="outlook":
		out1(call.message)
	if call.data =="o1":
		oo1(call.message)
	if call.data =="o2":
		oo2(call.message)
	if call.data =="o3":
		oo3(call.message)
	if call.data =="o4":
		oo4(call.message)
		
	#yahoo
	if call.data =="Yahoo":
		chek1(call.message)
	if call.data =="m1":
		ya1(call.message)
	if call.data =="m2":
		ya2(call.message)
	if call.data =="m3":
		ya3(call.message)
	if call.data =="m4":
		ya4(call.message)
	#mail.ru
	if call.data =="mailru":
		cherk1(call.message)
	if call.data =="r1":
		mailr1(call.message)
	if call.data =="r2":
		mailr2(call.message)
	if call.data =="r3":
		mailr3(call.message)
	if call.data =="r4":
		mailr4(call.message)
	#Aol
	if call.data =="aol":
		caol(call.message)
	if call.data =="a1":
		aoll1(call.message)
	if call.data =="a2":
		aoll2(call.message)
	if call.data =="a3":
		aoll3(call.message)
	if call.data =="a4":
		aoll4(call.message)
	#anything

def aoll1(message):
	     An = 0
	     Un = 0
	     ch = 0
	     z = 0
	     user = '1q2w3e4rt5yu6io7paos8dfogh9jk0lzxcvbbnm'
	     for im in range(5000):
	     	us = str(''.join((random.choice(user) for i in range(4))))
	     	email = us+'@aol.com'
	     	url = f"https://check.moahmedsalah.repl.co/api-v1/check-email/tiktok/?email={email}"
	     	req = requests.get(url).text
	     	print(req)
	     	if 'False' in req:
	     		print(f"Email Not Linked Tik Tok\n{email}\n\n")
	     	if "True" in req:
	     		print(f"Email Available Linked Tik Tok\n{email}\n\n")
	     		url = 'https://login.aol.com/account/module/create?validateField=yid'
	     		headers = {
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
'Connection': 'keep-alive',
'Content-Length': '18145',
'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'rxx=1vfldvwn9l2.2o9pnj7j&v=1; A1=d=AQABBFqnOWICEDjwmiRLg33xf8PJk7LqCf0FEgEBBgEKSmITY1xXb2UB_eMBAAcIWqc5YrLqCf0&S=AQAAAtgqjIvBD6rdgDf11Kpu26U; A3=d=AQABBFqnOWICEDjwmiRLg33xf8PJk7LqCf0FEgEBBgEKSmITY1xXb2UB_eMBAAcIWqc5YrLqCf0&S=AQAAAtgqjIvBD6rdgDf11Kpu26U; GUC=AQEBBgFiSgpjE0IgHgSX; A1S=d=AQABBFqnOWICEDjwmiRLg33xf8PJk7LqCf0FEgEBBgEKSmITY1xXb2UB_eMBAAcIWqc5YrLqCf0&S=AQAAAtgqjIvBD6rdgDf11Kpu26U&j=WORLD; BX=fq2fam9h3j9qq&b=3&s=hn; cmp=t=1649067849&j=0; __gpi=UID=0000036962154902:T=1649067874:RT=1649067874:S=ALNI_MYDCxbi1nMtreicYo_PQTz2fp2OAg; __gads=ID=063c7032ee7b8f7d:T=1649067874:S=ALNI_Mbyd1La8KJ95bSdo4DZk-gifCh7cg; _pubcid=9a0aaf21-d3d5-43fa-97c2-e7428deb3b2e; cto_bidid=5zXxk19Oc1hXbkl6MlJPViUyRlpBcDlnOUVYNTlzMWhSbFpkVVRKVkVkWU9pc2NYdUJRa05BTFd5TEJxZkFyMWdEanZZVTlla1A2UHhaeHpHUER2RHVFS04xN0J3UVJhVHklMkZaU0QxcEM3MjM1cmFLS1klM0Q; panoramaId_expiry=1649672684666; _cc_id=2a4bfd220ed3648dec80176a385833eb; panoramaId=b5a98fdf71e281ae241cd5b8696016d539383e863cbb39a924a19f14d47b4795; cto_bundle=r5gvFV83a0ZNWnRrVEd0UTZHUlBveVFCb0NiS1Y1cmRXbVlRMVJoem55SnQ5MzVwJTJGNmh5aGFpOVB3dmhBbkxBMDlJcW9ZM0lHeW9yJTJCJTJGdFklMkZwTjlaWEc0eVpOTmZ1cWVvd2llMTM0enZBS01HY2tCeFNKVnNZMk1UTGhQJTJCMWxMZXlEMmdzTExCcUVzQ2hEMTZTcEtMNjBSNSUyQmclM0QlM0Q; AS=v=1&s=0V6NUvZc&d=C624ad184|sCBMs5v.2QIcuPrP2.ETZ1KM6F.lloTY0t2UERYhF1Q0y3If09uZ_UB6Mx5CKCIyaWQWcCuMT2Ttci_E.uXiEmYkHn2GsSduKqc4X2OTwF.t9TrBCARrtCtwpYHAjh6f_GbnZa3v5srDmbR9nqNw.coXzYFXHNnRAAg7TjAVlpkbGwypvq.IGapf4bfhO.pvuCXIJoPJbukxjmvvrCAd3I4nzU0BKItlRkYTBBtAyud6UHOv69jTQXUzIautpaz7XL_03Ri2nW.TgCqEUvV2dGcZYRy9XZ5YLx9EVIApfNH23lw4jyZFvrNbOhsk4bgNn689P3Pwos8dtFNNqsF7SSPsaSGjS3FC2OFq0Ym.66AD90YuX0Ufgo7t_HvbOpm7LtxW_hfiKRZSSLuRBiTFC6JxU_78RyMEJF05wkncN0ya3DKmZ8bt.rrq4PnE6.DCtPF1KD7LWu3T18AN4NedjUa965nQAceCwC6qPIfmZwdIFuCTAM_w4VsZ3h3P0isATIRb06ueQeC122sSrHSOiT9nsFM4ZmpsQpa_UyEqxeJsM0kX1XKKJezbVKPw_gJ79dK.gGtA9X35EOIFWlXdG7RKMbmQFPeFZIQPhzsjmdJjuOjcMFnOSP6Ls5KqAKno5v0xfxmjKtnXU.6DoCSXbP0fBPMv25gnxGPu7mNwLC.ETgbTzxgzgsfvM0m2dxRUWQpn_p37jZOGUDJyFeiwoKimclwE.dtWrA11k87a1NKNcWsYeBO9899caR3DVb4T__CuzvjoG8fYfnxBWMtEfK9P1H_TpV4hvCC0j13wscPJvjPS0urRrWLaVHmecDKQTpRpU497xb22o698GejGqWQ7DBJOzlNTfewkAZaVJdxEepUtzzXS.pjsVMvDXsfLqWsCQ4bTp_lCYNAfS4e_vX0i_bTBUysjl4UN6hOqf7Xfapfv0A0LqT2zJMNsSvlTRvxKB_d8ehzhwmRB8ilbqGgaHdOct7rkK0dev5oZuDXkhACEsap9x4HxL6ITqtGQ7QosQLxlMHqTznjtWYPvgjbkzJGAfsAEou7ZqVqCDD2uk1qsJVADvdkvbK5TCAE1QWKBq1QSAiYJc.epIWwuXlimyo7d7Jdtidr20SRZtnl8CuRsthmg2rG3HxDrEgN01.MArNS0RifDhxqE_wrlAQLoINczubcRgteg4XgI0ypDFGfWMX1PLEx2CNsLYJc.bGHG7Ij.cmbU8PyBhfwaiNbJ3BcwsvuIsrypj_8D1d2qPhYhqvzEFNv_WuWIvs7nqow8LlM1TAgv5bShYkfgTw1ooHuB9Z4j6ftkYscdIo8kVFubFloSG7rIsQZDAwCZP3Zppd426tuu7AOs888WtO9ihBFnwvufHDb_0x_5.YeszfhL2o9Zd5nu9xLkRzyr4x76A08aSxmt04y3YggkVXvLGOQ9luDuUQddPIP8Ow--~A',
'Host': 'login.aol.com',
'Origin': 'https://login.aol.com',
'Referer': 'https://login.aol.com/account/create?intl=us&lang=en-US&specId=yidreg&done=https%3A%2F%2Fwww.aol.com%2F&altreg=1',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': "Windows",
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'User-Agent': str(generate_user_agent()),
'X-Requested-With': 'XMLHttpRequest'}
	     		data = {
'browser-fp-data': '{"language":"ar","colorDepth":24,"deviceMemory":2,"pixelRatio":1,"hardwareConcurrency":2,"timezoneOffset":-180,"timezone":"Asia/Baghdad","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":5,"hash":"2c14024bf8584c3f7f63f24ea490e812"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc. (NVIDIA)~ANGLE (NVIDIA, NVIDIA Quadro FX 360M  Direct3D11 vs_4_0 ps_4_0, D3D11)","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":49,"hash":"411659924ff38420049ac402a30466bc"},"audio":"124.04347527516074","resolution":{"w":"1280","h":"800"},"availableResolution":{"w":"760","h":"1280"},"ts":{"serve":1649092773919,"render":1649092781234}}',
'specId': 'yidreg',
'crumb': 'ZPqUo5LcUPJ',
'acrumb': '0V6NUvZc',
'done': 'https://www.aol.com/',
'attrSetIndex': '0',
'tos0': 'oath_freereg|us|en-US',
'firstName': 'Sufi',
'lastName': 'saade',
'yid': str(email),
'password': 'Msutafassad1',
'shortCountryCode': 'US',
'phone': '+12056757454',
'freeformGender': 'boy',
'signup':'',
}
	     		response = requests.post(url,headers=headers,data=data).text
	     		print(response)
	     		print(email)
	     		if ('"yid"') in response:
	     			print("غير متاح")
	     			Un+=1
	     		elif ('"birthDate"') in response:
	     			An+=1
	     			print("متاح ")
	     			url = f"https://alkabby4api.pythonanywhere.com/info/tiktok?user={us}"
	     			ree = requests.get(url).json()
	     			Name = str(ree['Name'])
	     			Followers = str(ree['Followers'])
	     			Following = str(ree['Following'])
	     			Likes = str(ree['Likes'])
	     			bot.send_message(message.chat.id,f"""SuFi BoT New HuNteR
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
User : {us}
Name : {Name}
Followers : {Followers}
Following : {Following}
Likes : {Likes}
Email : {email}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
Tele : @MMPMMMM""")
	     		else:
	     			print("fales")
	     			z+=1
	     	else:
	     		ch+=1
	     		prix  = types.InlineKeyboardButton(text = "Developer", url = 'https://t.me/MMPMMMM')
	     		mnm = types.InlineKeyboardMarkup()
	     		mnm.row_width = 1
	     		mnm.add(prix)
	     		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"WaiT For HunT MY FrienD\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nin User : {us}\nEmail : {email}\nUnavailable : {Un}\nAvailable : {An}\nCheck : {ch}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nBY : @MMPMMMM"),parse_mode='markdown',reply_markup=mnm)	
			
def aoll2(message):
	     An = 0
	     Un = 0
	     ch = 0
	     z = 0
	     user = '1q2w3e4rt5yu6io7paos8dfogh9jk0lzxcvbbnm'
	     for im in range(5000):
	     	us = str(''.join((random.choice(user) for i in range(5))))
	     	email = us+'@aol.com'
	     	url = f"https://check.moahmedsalah.repl.co/api-v1/check-email/tiktok/?email={email}"
	     	req = requests.get(url).text
	     	print(req)
	     	if 'False' in req:
	     		print(f"Email Not Linked Tik Tok\n{email}\n\n")
	     	if "True" in req:
	     		print(f"Email Available Linked Tik Tok\n{email}\n\n")
	     		url = 'https://login.aol.com/account/module/create?validateField=yid'
	     		headers = {
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
'Connection': 'keep-alive',
'Content-Length': '18145',
'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'rxx=1vfldvwn9l2.2o9pnj7j&v=1; A1=d=AQABBFqnOWICEDjwmiRLg33xf8PJk7LqCf0FEgEBBgEKSmITY1xXb2UB_eMBAAcIWqc5YrLqCf0&S=AQAAAtgqjIvBD6rdgDf11Kpu26U; A3=d=AQABBFqnOWICEDjwmiRLg33xf8PJk7LqCf0FEgEBBgEKSmITY1xXb2UB_eMBAAcIWqc5YrLqCf0&S=AQAAAtgqjIvBD6rdgDf11Kpu26U; GUC=AQEBBgFiSgpjE0IgHgSX; A1S=d=AQABBFqnOWICEDjwmiRLg33xf8PJk7LqCf0FEgEBBgEKSmITY1xXb2UB_eMBAAcIWqc5YrLqCf0&S=AQAAAtgqjIvBD6rdgDf11Kpu26U&j=WORLD; BX=fq2fam9h3j9qq&b=3&s=hn; cmp=t=1649067849&j=0; __gpi=UID=0000036962154902:T=1649067874:RT=1649067874:S=ALNI_MYDCxbi1nMtreicYo_PQTz2fp2OAg; __gads=ID=063c7032ee7b8f7d:T=1649067874:S=ALNI_Mbyd1La8KJ95bSdo4DZk-gifCh7cg; _pubcid=9a0aaf21-d3d5-43fa-97c2-e7428deb3b2e; cto_bidid=5zXxk19Oc1hXbkl6MlJPViUyRlpBcDlnOUVYNTlzMWhSbFpkVVRKVkVkWU9pc2NYdUJRa05BTFd5TEJxZkFyMWdEanZZVTlla1A2UHhaeHpHUER2RHVFS04xN0J3UVJhVHklMkZaU0QxcEM3MjM1cmFLS1klM0Q; panoramaId_expiry=1649672684666; _cc_id=2a4bfd220ed3648dec80176a385833eb; panoramaId=b5a98fdf71e281ae241cd5b8696016d539383e863cbb39a924a19f14d47b4795; cto_bundle=r5gvFV83a0ZNWnRrVEd0UTZHUlBveVFCb0NiS1Y1cmRXbVlRMVJoem55SnQ5MzVwJTJGNmh5aGFpOVB3dmhBbkxBMDlJcW9ZM0lHeW9yJTJCJTJGdFklMkZwTjlaWEc0eVpOTmZ1cWVvd2llMTM0enZBS01HY2tCeFNKVnNZMk1UTGhQJTJCMWxMZXlEMmdzTExCcUVzQ2hEMTZTcEtMNjBSNSUyQmclM0QlM0Q; AS=v=1&s=0V6NUvZc&d=C624ad184|sCBMs5v.2QIcuPrP2.ETZ1KM6F.lloTY0t2UERYhF1Q0y3If09uZ_UB6Mx5CKCIyaWQWcCuMT2Ttci_E.uXiEmYkHn2GsSduKqc4X2OTwF.t9TrBCARrtCtwpYHAjh6f_GbnZa3v5srDmbR9nqNw.coXzYFXHNnRAAg7TjAVlpkbGwypvq.IGapf4bfhO.pvuCXIJoPJbukxjmvvrCAd3I4nzU0BKItlRkYTBBtAyud6UHOv69jTQXUzIautpaz7XL_03Ri2nW.TgCqEUvV2dGcZYRy9XZ5YLx9EVIApfNH23lw4jyZFvrNbOhsk4bgNn689P3Pwos8dtFNNqsF7SSPsaSGjS3FC2OFq0Ym.66AD90YuX0Ufgo7t_HvbOpm7LtxW_hfiKRZSSLuRBiTFC6JxU_78RyMEJF05wkncN0ya3DKmZ8bt.rrq4PnE6.DCtPF1KD7LWu3T18AN4NedjUa965nQAceCwC6qPIfmZwdIFuCTAM_w4VsZ3h3P0isATIRb06ueQeC122sSrHSOiT9nsFM4ZmpsQpa_UyEqxeJsM0kX1XKKJezbVKPw_gJ79dK.gGtA9X35EOIFWlXdG7RKMbmQFPeFZIQPhzsjmdJjuOjcMFnOSP6Ls5KqAKno5v0xfxmjKtnXU.6DoCSXbP0fBPMv25gnxGPu7mNwLC.ETgbTzxgzgsfvM0m2dxRUWQpn_p37jZOGUDJyFeiwoKimclwE.dtWrA11k87a1NKNcWsYeBO9899caR3DVb4T__CuzvjoG8fYfnxBWMtEfK9P1H_TpV4hvCC0j13wscPJvjPS0urRrWLaVHmecDKQTpRpU497xb22o698GejGqWQ7DBJOzlNTfewkAZaVJdxEepUtzzXS.pjsVMvDXsfLqWsCQ4bTp_lCYNAfS4e_vX0i_bTBUysjl4UN6hOqf7Xfapfv0A0LqT2zJMNsSvlTRvxKB_d8ehzhwmRB8ilbqGgaHdOct7rkK0dev5oZuDXkhACEsap9x4HxL6ITqtGQ7QosQLxlMHqTznjtWYPvgjbkzJGAfsAEou7ZqVqCDD2uk1qsJVADvdkvbK5TCAE1QWKBq1QSAiYJc.epIWwuXlimyo7d7Jdtidr20SRZtnl8CuRsthmg2rG3HxDrEgN01.MArNS0RifDhxqE_wrlAQLoINczubcRgteg4XgI0ypDFGfWMX1PLEx2CNsLYJc.bGHG7Ij.cmbU8PyBhfwaiNbJ3BcwsvuIsrypj_8D1d2qPhYhqvzEFNv_WuWIvs7nqow8LlM1TAgv5bShYkfgTw1ooHuB9Z4j6ftkYscdIo8kVFubFloSG7rIsQZDAwCZP3Zppd426tuu7AOs888WtO9ihBFnwvufHDb_0x_5.YeszfhL2o9Zd5nu9xLkRzyr4x76A08aSxmt04y3YggkVXvLGOQ9luDuUQddPIP8Ow--~A',
'Host': 'login.aol.com',
'Origin': 'https://login.aol.com',
'Referer': 'https://login.aol.com/account/create?intl=us&lang=en-US&specId=yidreg&done=https%3A%2F%2Fwww.aol.com%2F&altreg=1',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': "Windows",
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'User-Agent': str(generate_user_agent()),
'X-Requested-With': 'XMLHttpRequest'}
	     		data = {
'browser-fp-data': '{"language":"ar","colorDepth":24,"deviceMemory":2,"pixelRatio":1,"hardwareConcurrency":2,"timezoneOffset":-180,"timezone":"Asia/Baghdad","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":5,"hash":"2c14024bf8584c3f7f63f24ea490e812"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc. (NVIDIA)~ANGLE (NVIDIA, NVIDIA Quadro FX 360M  Direct3D11 vs_4_0 ps_4_0, D3D11)","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":49,"hash":"411659924ff38420049ac402a30466bc"},"audio":"124.04347527516074","resolution":{"w":"1280","h":"800"},"availableResolution":{"w":"760","h":"1280"},"ts":{"serve":1649092773919,"render":1649092781234}}',
'specId': 'yidreg',
'crumb': 'ZPqUo5LcUPJ',
'acrumb': '0V6NUvZc',
'done': 'https://www.aol.com/',
'attrSetIndex': '0',
'tos0': 'oath_freereg|us|en-US',
'firstName': 'Sufi',
'lastName': 'saade',
'yid': str(email),
'password': 'Msutafassad1',
'shortCountryCode': 'US',
'phone': '+12056757454',
'freeformGender': 'boy',
'signup':'',
}
	     		response = requests.post(url,headers=headers,data=data).text
	     		print(response)
	     		print(email)
	     		if ('"yid"') in response:
	     			print("غير متاح")
	     			Un+=1
	     		elif ('"birthDate"') in response:
	     			An+=1
	     			print("متاح ")
	     			url = f"https://alkabby4api.pythonanywhere.com/info/tiktok?user={us}"
	     			ree = requests.get(url).json()
	     			Name = str(ree['Name'])
	     			Followers = str(ree['Followers'])
	     			Following = str(ree['Following'])
	     			Likes = str(ree['Likes'])
	     			bot.send_message(message.chat.id,f"""SuFi BoT New HuNteR
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
User : {us}
Name : {Name}
Followers : {Followers}
Following : {Following}
Likes : {Likes}
Email : {email}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
Tele : @MMPMMMM""")
	     		else:
	     			print("fales")
	     			z+=1
	     	else:
	     		ch+=1
	     		prix  = types.InlineKeyboardButton(text = "Developer", url = 'https://t.me/MMPMMMM')
	     		mnm = types.InlineKeyboardMarkup()
	     		mnm.row_width = 1
	     		mnm.add(prix)
	     		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"WaiT For HunT MY FrienD\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nin User : {us}\nEmail : {email}\nUnavailable : {Un}\nAvailable : {An}\nCheck : {ch}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nBY : @MMPMMMM"),parse_mode='markdown',reply_markup=mnm)
	
def aoll3(message):
	     An = 0
	     Un = 0
	     ch = 0
	     z = 0
	     user = '1q2w3e4rt5yu6io7paos8dfogh9jk0lzxcvbbnm'
	     for im in range(5000):
	     	us = str(''.join((random.choice(user) for i in range(6))))
	     	email = us+'@aol.com'
	     	url = f"https://check.moahmedsalah.repl.co/api-v1/check-email/tiktok/?email={email}"
	     	req = requests.get(url).text
	     	print(req)
	     	if 'False' in req:
	     		print(f"Email Not Linked Tik Tok\n{email}\n\n")
	     	if "True" in req:
	     		print(f"Email Available Linked Tik Tok\n{email}\n\n")
	     		url = 'https://login.aol.com/account/module/create?validateField=yid'
	     		headers = {
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
'Connection': 'keep-alive',
'Content-Length': '18145',
'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'rxx=1vfldvwn9l2.2o9pnj7j&v=1; A1=d=AQABBFqnOWICEDjwmiRLg33xf8PJk7LqCf0FEgEBBgEKSmITY1xXb2UB_eMBAAcIWqc5YrLqCf0&S=AQAAAtgqjIvBD6rdgDf11Kpu26U; A3=d=AQABBFqnOWICEDjwmiRLg33xf8PJk7LqCf0FEgEBBgEKSmITY1xXb2UB_eMBAAcIWqc5YrLqCf0&S=AQAAAtgqjIvBD6rdgDf11Kpu26U; GUC=AQEBBgFiSgpjE0IgHgSX; A1S=d=AQABBFqnOWICEDjwmiRLg33xf8PJk7LqCf0FEgEBBgEKSmITY1xXb2UB_eMBAAcIWqc5YrLqCf0&S=AQAAAtgqjIvBD6rdgDf11Kpu26U&j=WORLD; BX=fq2fam9h3j9qq&b=3&s=hn; cmp=t=1649067849&j=0; __gpi=UID=0000036962154902:T=1649067874:RT=1649067874:S=ALNI_MYDCxbi1nMtreicYo_PQTz2fp2OAg; __gads=ID=063c7032ee7b8f7d:T=1649067874:S=ALNI_Mbyd1La8KJ95bSdo4DZk-gifCh7cg; _pubcid=9a0aaf21-d3d5-43fa-97c2-e7428deb3b2e; cto_bidid=5zXxk19Oc1hXbkl6MlJPViUyRlpBcDlnOUVYNTlzMWhSbFpkVVRKVkVkWU9pc2NYdUJRa05BTFd5TEJxZkFyMWdEanZZVTlla1A2UHhaeHpHUER2RHVFS04xN0J3UVJhVHklMkZaU0QxcEM3MjM1cmFLS1klM0Q; panoramaId_expiry=1649672684666; _cc_id=2a4bfd220ed3648dec80176a385833eb; panoramaId=b5a98fdf71e281ae241cd5b8696016d539383e863cbb39a924a19f14d47b4795; cto_bundle=r5gvFV83a0ZNWnRrVEd0UTZHUlBveVFCb0NiS1Y1cmRXbVlRMVJoem55SnQ5MzVwJTJGNmh5aGFpOVB3dmhBbkxBMDlJcW9ZM0lHeW9yJTJCJTJGdFklMkZwTjlaWEc0eVpOTmZ1cWVvd2llMTM0enZBS01HY2tCeFNKVnNZMk1UTGhQJTJCMWxMZXlEMmdzTExCcUVzQ2hEMTZTcEtMNjBSNSUyQmclM0QlM0Q; AS=v=1&s=0V6NUvZc&d=C624ad184|sCBMs5v.2QIcuPrP2.ETZ1KM6F.lloTY0t2UERYhF1Q0y3If09uZ_UB6Mx5CKCIyaWQWcCuMT2Ttci_E.uXiEmYkHn2GsSduKqc4X2OTwF.t9TrBCARrtCtwpYHAjh6f_GbnZa3v5srDmbR9nqNw.coXzYFXHNnRAAg7TjAVlpkbGwypvq.IGapf4bfhO.pvuCXIJoPJbukxjmvvrCAd3I4nzU0BKItlRkYTBBtAyud6UHOv69jTQXUzIautpaz7XL_03Ri2nW.TgCqEUvV2dGcZYRy9XZ5YLx9EVIApfNH23lw4jyZFvrNbOhsk4bgNn689P3Pwos8dtFNNqsF7SSPsaSGjS3FC2OFq0Ym.66AD90YuX0Ufgo7t_HvbOpm7LtxW_hfiKRZSSLuRBiTFC6JxU_78RyMEJF05wkncN0ya3DKmZ8bt.rrq4PnE6.DCtPF1KD7LWu3T18AN4NedjUa965nQAceCwC6qPIfmZwdIFuCTAM_w4VsZ3h3P0isATIRb06ueQeC122sSrHSOiT9nsFM4ZmpsQpa_UyEqxeJsM0kX1XKKJezbVKPw_gJ79dK.gGtA9X35EOIFWlXdG7RKMbmQFPeFZIQPhzsjmdJjuOjcMFnOSP6Ls5KqAKno5v0xfxmjKtnXU.6DoCSXbP0fBPMv25gnxGPu7mNwLC.ETgbTzxgzgsfvM0m2dxRUWQpn_p37jZOGUDJyFeiwoKimclwE.dtWrA11k87a1NKNcWsYeBO9899caR3DVb4T__CuzvjoG8fYfnxBWMtEfK9P1H_TpV4hvCC0j13wscPJvjPS0urRrWLaVHmecDKQTpRpU497xb22o698GejGqWQ7DBJOzlNTfewkAZaVJdxEepUtzzXS.pjsVMvDXsfLqWsCQ4bTp_lCYNAfS4e_vX0i_bTBUysjl4UN6hOqf7Xfapfv0A0LqT2zJMNsSvlTRvxKB_d8ehzhwmRB8ilbqGgaHdOct7rkK0dev5oZuDXkhACEsap9x4HxL6ITqtGQ7QosQLxlMHqTznjtWYPvgjbkzJGAfsAEou7ZqVqCDD2uk1qsJVADvdkvbK5TCAE1QWKBq1QSAiYJc.epIWwuXlimyo7d7Jdtidr20SRZtnl8CuRsthmg2rG3HxDrEgN01.MArNS0RifDhxqE_wrlAQLoINczubcRgteg4XgI0ypDFGfWMX1PLEx2CNsLYJc.bGHG7Ij.cmbU8PyBhfwaiNbJ3BcwsvuIsrypj_8D1d2qPhYhqvzEFNv_WuWIvs7nqow8LlM1TAgv5bShYkfgTw1ooHuB9Z4j6ftkYscdIo8kVFubFloSG7rIsQZDAwCZP3Zppd426tuu7AOs888WtO9ihBFnwvufHDb_0x_5.YeszfhL2o9Zd5nu9xLkRzyr4x76A08aSxmt04y3YggkVXvLGOQ9luDuUQddPIP8Ow--~A',
'Host': 'login.aol.com',
'Origin': 'https://login.aol.com',
'Referer': 'https://login.aol.com/account/create?intl=us&lang=en-US&specId=yidreg&done=https%3A%2F%2Fwww.aol.com%2F&altreg=1',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': "Windows",
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'User-Agent': str(generate_user_agent()),
'X-Requested-With': 'XMLHttpRequest'}
	     		data = {
'browser-fp-data': '{"language":"ar","colorDepth":24,"deviceMemory":2,"pixelRatio":1,"hardwareConcurrency":2,"timezoneOffset":-180,"timezone":"Asia/Baghdad","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":5,"hash":"2c14024bf8584c3f7f63f24ea490e812"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc. (NVIDIA)~ANGLE (NVIDIA, NVIDIA Quadro FX 360M  Direct3D11 vs_4_0 ps_4_0, D3D11)","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":49,"hash":"411659924ff38420049ac402a30466bc"},"audio":"124.04347527516074","resolution":{"w":"1280","h":"800"},"availableResolution":{"w":"760","h":"1280"},"ts":{"serve":1649092773919,"render":1649092781234}}',
'specId': 'yidreg',
'crumb': 'ZPqUo5LcUPJ',
'acrumb': '0V6NUvZc',
'done': 'https://www.aol.com/',
'attrSetIndex': '0',
'tos0': 'oath_freereg|us|en-US',
'firstName': 'Sufi',
'lastName': 'saade',
'yid': str(email),
'password': 'Msutafassad1',
'shortCountryCode': 'US',
'phone': '+12056757454',
'freeformGender': 'boy',
'signup':'',
}
	     		response = requests.post(url,headers=headers,data=data).text
	     		print(response)
	     		print(email)
	     		if ('"yid"') in response:
	     			print("غير متاح")
	     			Un+=1
	     		elif ('"birthDate"') in response:
	     			An+=1
	     			print("متاح ")
	     			url = f"https://alkabby4api.pythonanywhere.com/info/tiktok?user={us}"
	     			ree = requests.get(url).json()
	     			Name = str(ree['Name'])
	     			Followers = str(ree['Followers'])
	     			Following = str(ree['Following'])
	     			Likes = str(ree['Likes'])
	     			bot.send_message(message.chat.id,f"""SuFi BoT New HuNteR
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
User : {us}
Name : {Name}
Followers : {Followers}
Following : {Following}
Likes : {Likes}
Email : {email}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
Tele : @MMPMMMM""")
	     		else:
	     			print("fales")
	     			z+=1
	     	else:
	     		ch+=1
	     		prix  = types.InlineKeyboardButton(text = "Developer", url = 'https://t.me/MMPMMMM')
	     		mnm = types.InlineKeyboardMarkup()
	     		mnm.row_width = 1
	     		mnm.add(prix)
	     		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"WaiT For HunT MY FrienD\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nin User : {us}\nEmail : {email}\nUnavailable : {Un}\nAvailable : {An}\nCheck : {ch}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nBY : @MMPMMMM"),parse_mode='markdown',reply_markup=mnm)
	     		
def aoll4(message):
	     An = 0
	     Un = 0
	     ch = 0
	     z = 0
	     user = '1q2w3e4rt5yu6io7paos8dfogh9jk0lzxcvbbnm'
	     for im in range(5000):
	     	us = str(''.join((random.choice(user) for i in range(7))))
	     	email = us+'@aol.com'
	     	url = f"https://check.moahmedsalah.repl.co/api-v1/check-email/tiktok/?email={email}"
	     	req = requests.get(url).text
	     	print(req)
	     	if 'False' in req:
	     		print(f"Email Not Linked Tik Tok\n{email}\n\n")
	     	if "True" in req:
	     		print(f"Email Available Linked Tik Tok\n{email}\n\n")
	     		url = 'https://login.aol.com/account/module/create?validateField=yid'
	     		headers = {
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
'Connection': 'keep-alive',
'Content-Length': '18145',
'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'rxx=1vfldvwn9l2.2o9pnj7j&v=1; A1=d=AQABBFqnOWICEDjwmiRLg33xf8PJk7LqCf0FEgEBBgEKSmITY1xXb2UB_eMBAAcIWqc5YrLqCf0&S=AQAAAtgqjIvBD6rdgDf11Kpu26U; A3=d=AQABBFqnOWICEDjwmiRLg33xf8PJk7LqCf0FEgEBBgEKSmITY1xXb2UB_eMBAAcIWqc5YrLqCf0&S=AQAAAtgqjIvBD6rdgDf11Kpu26U; GUC=AQEBBgFiSgpjE0IgHgSX; A1S=d=AQABBFqnOWICEDjwmiRLg33xf8PJk7LqCf0FEgEBBgEKSmITY1xXb2UB_eMBAAcIWqc5YrLqCf0&S=AQAAAtgqjIvBD6rdgDf11Kpu26U&j=WORLD; BX=fq2fam9h3j9qq&b=3&s=hn; cmp=t=1649067849&j=0; __gpi=UID=0000036962154902:T=1649067874:RT=1649067874:S=ALNI_MYDCxbi1nMtreicYo_PQTz2fp2OAg; __gads=ID=063c7032ee7b8f7d:T=1649067874:S=ALNI_Mbyd1La8KJ95bSdo4DZk-gifCh7cg; _pubcid=9a0aaf21-d3d5-43fa-97c2-e7428deb3b2e; cto_bidid=5zXxk19Oc1hXbkl6MlJPViUyRlpBcDlnOUVYNTlzMWhSbFpkVVRKVkVkWU9pc2NYdUJRa05BTFd5TEJxZkFyMWdEanZZVTlla1A2UHhaeHpHUER2RHVFS04xN0J3UVJhVHklMkZaU0QxcEM3MjM1cmFLS1klM0Q; panoramaId_expiry=1649672684666; _cc_id=2a4bfd220ed3648dec80176a385833eb; panoramaId=b5a98fdf71e281ae241cd5b8696016d539383e863cbb39a924a19f14d47b4795; cto_bundle=r5gvFV83a0ZNWnRrVEd0UTZHUlBveVFCb0NiS1Y1cmRXbVlRMVJoem55SnQ5MzVwJTJGNmh5aGFpOVB3dmhBbkxBMDlJcW9ZM0lHeW9yJTJCJTJGdFklMkZwTjlaWEc0eVpOTmZ1cWVvd2llMTM0enZBS01HY2tCeFNKVnNZMk1UTGhQJTJCMWxMZXlEMmdzTExCcUVzQ2hEMTZTcEtMNjBSNSUyQmclM0QlM0Q; AS=v=1&s=0V6NUvZc&d=C624ad184|sCBMs5v.2QIcuPrP2.ETZ1KM6F.lloTY0t2UERYhF1Q0y3If09uZ_UB6Mx5CKCIyaWQWcCuMT2Ttci_E.uXiEmYkHn2GsSduKqc4X2OTwF.t9TrBCARrtCtwpYHAjh6f_GbnZa3v5srDmbR9nqNw.coXzYFXHNnRAAg7TjAVlpkbGwypvq.IGapf4bfhO.pvuCXIJoPJbukxjmvvrCAd3I4nzU0BKItlRkYTBBtAyud6UHOv69jTQXUzIautpaz7XL_03Ri2nW.TgCqEUvV2dGcZYRy9XZ5YLx9EVIApfNH23lw4jyZFvrNbOhsk4bgNn689P3Pwos8dtFNNqsF7SSPsaSGjS3FC2OFq0Ym.66AD90YuX0Ufgo7t_HvbOpm7LtxW_hfiKRZSSLuRBiTFC6JxU_78RyMEJF05wkncN0ya3DKmZ8bt.rrq4PnE6.DCtPF1KD7LWu3T18AN4NedjUa965nQAceCwC6qPIfmZwdIFuCTAM_w4VsZ3h3P0isATIRb06ueQeC122sSrHSOiT9nsFM4ZmpsQpa_UyEqxeJsM0kX1XKKJezbVKPw_gJ79dK.gGtA9X35EOIFWlXdG7RKMbmQFPeFZIQPhzsjmdJjuOjcMFnOSP6Ls5KqAKno5v0xfxmjKtnXU.6DoCSXbP0fBPMv25gnxGPu7mNwLC.ETgbTzxgzgsfvM0m2dxRUWQpn_p37jZOGUDJyFeiwoKimclwE.dtWrA11k87a1NKNcWsYeBO9899caR3DVb4T__CuzvjoG8fYfnxBWMtEfK9P1H_TpV4hvCC0j13wscPJvjPS0urRrWLaVHmecDKQTpRpU497xb22o698GejGqWQ7DBJOzlNTfewkAZaVJdxEepUtzzXS.pjsVMvDXsfLqWsCQ4bTp_lCYNAfS4e_vX0i_bTBUysjl4UN6hOqf7Xfapfv0A0LqT2zJMNsSvlTRvxKB_d8ehzhwmRB8ilbqGgaHdOct7rkK0dev5oZuDXkhACEsap9x4HxL6ITqtGQ7QosQLxlMHqTznjtWYPvgjbkzJGAfsAEou7ZqVqCDD2uk1qsJVADvdkvbK5TCAE1QWKBq1QSAiYJc.epIWwuXlimyo7d7Jdtidr20SRZtnl8CuRsthmg2rG3HxDrEgN01.MArNS0RifDhxqE_wrlAQLoINczubcRgteg4XgI0ypDFGfWMX1PLEx2CNsLYJc.bGHG7Ij.cmbU8PyBhfwaiNbJ3BcwsvuIsrypj_8D1d2qPhYhqvzEFNv_WuWIvs7nqow8LlM1TAgv5bShYkfgTw1ooHuB9Z4j6ftkYscdIo8kVFubFloSG7rIsQZDAwCZP3Zppd426tuu7AOs888WtO9ihBFnwvufHDb_0x_5.YeszfhL2o9Zd5nu9xLkRzyr4x76A08aSxmt04y3YggkVXvLGOQ9luDuUQddPIP8Ow--~A',
'Host': 'login.aol.com',
'Origin': 'https://login.aol.com',
'Referer': 'https://login.aol.com/account/create?intl=us&lang=en-US&specId=yidreg&done=https%3A%2F%2Fwww.aol.com%2F&altreg=1',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': "Windows",
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'User-Agent': str(generate_user_agent()),
'X-Requested-With': 'XMLHttpRequest'}
	     		data = {
'browser-fp-data': '{"language":"ar","colorDepth":24,"deviceMemory":2,"pixelRatio":1,"hardwareConcurrency":2,"timezoneOffset":-180,"timezone":"Asia/Baghdad","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":5,"hash":"2c14024bf8584c3f7f63f24ea490e812"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc. (NVIDIA)~ANGLE (NVIDIA, NVIDIA Quadro FX 360M  Direct3D11 vs_4_0 ps_4_0, D3D11)","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":49,"hash":"411659924ff38420049ac402a30466bc"},"audio":"124.04347527516074","resolution":{"w":"1280","h":"800"},"availableResolution":{"w":"760","h":"1280"},"ts":{"serve":1649092773919,"render":1649092781234}}',
'specId': 'yidreg',
'crumb': 'ZPqUo5LcUPJ',
'acrumb': '0V6NUvZc',
'done': 'https://www.aol.com/',
'attrSetIndex': '0',
'tos0': 'oath_freereg|us|en-US',
'firstName': 'Sufi',
'lastName': 'saade',
'yid': str(email),
'password': 'Msutafassad1',
'shortCountryCode': 'US',
'phone': '+12056757454',
'freeformGender': 'boy',
'signup':'',
}
	     		response = requests.post(url,headers=headers,data=data).text
	     		print(response)
	     		print(email)
	     		if ('"yid"') in response:
	     			print("غير متاح")
	     			Un+=1
	     		elif ('"birthDate"') in response:
	     			An+=1
	     			print("متاح ")
	     			url = f"https://alkabby4api.pythonanywhere.com/info/tiktok?user={us}"
	     			ree = requests.get(url).json()
	     			Name = str(ree['Name'])
	     			Followers = str(ree['Followers'])
	     			Following = str(ree['Following'])
	     			Likes = str(ree['Likes'])
	     			bot.send_message(message.chat.id,f"""SuFi BoT New HuNteR
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
User : {us}
Name : {Name}
Followers : {Followers}
Following : {Following}
Likes : {Likes}
Email : {email}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
Tele : @MMPMMMM""")
	     		else:
	     			print("fales")
	     			z+=1
	     	else:
	     		ch+=1
	     		prix  = types.InlineKeyboardButton(text = "Developer", url = 'https://t.me/MMPMMMM')
	     		mnm = types.InlineKeyboardMarkup()
	     		mnm.row_width = 1
	     		mnm.add(prix)
	     		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"WaiT For HunT MY FrienD\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nin User : {us}\nEmail : {email}\nUnavailable : {Un}\nAvailable : {An}\nCheck : {ch}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nBY : @MMPMMMM"),parse_mode='markdown',reply_markup=mnm)

def mailr1(message):
     	An = 0
     	Un = 0
     	ch = 0
     	Fal = 0
     	z = 0
     	user = '1q2w3e4rt5yu6io7paos8dfogh9jk0lzxcvbbnm'
     	for im in range(5000):
     		us = str(''.join((random.choice(user) for i in range(4))))
     		email = us+'@mail.ru'
     		url = f"https://check.moahmedsalah.repl.co/api-v1/check-email/tiktok/?email={email}"
     		req = requests.get(url).text
     		print(req)
     		if 'False' in req:
	     		Fal+=1
	     		print(f"Email Not Linked Tik Tok\n{email}\n\n")
	     	if "True" in req:
	     		print(f"Email Available Linked Tik Tok\n{email}\n\n")
	     		head = {
		  "user-agent": str(generate_user_agent()),
	     	}
	     		url = f"https://account.mail.ru/api/v1/user/exists?email={email}"
	     		req = requests.post(url, headers=head).text
	     		print(req)
	     		if '"exists":true' in req:
	     			Un+=1
	     			print("UnAvailable")
	     		if '"exists":false' in req:
	     			An+=1
	     			print("Available  :   {mail}")
	     			url = f"https://alkabby4api.pythonanywhere.com/info/tiktok?user={us}"
	     			ree = requests.get(url).json()
	     			Name = str(ree['Name'])
	     			Followers = str(ree['Followers'])
	     			Following = str(ree['Following'])
	     			Likes = str(ree['Likes'])
	     			bot.send_message(message.chat.id,f"""SuFi BoT New HuNteR
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
User : {us}
Name : {Name}
Followers : {Followers}
Following : {Following}
Likes : {Likes}
Email : {email}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
Tele : @MMPMMMM""")
	     		else:
	     			print("fales")
	     			z+=1
	     	else:
	     		ch+=1
	     		prix  = types.InlineKeyboardButton(text = "Developer", url = 'https://t.me/MMPMMMM')
	     		mnm = types.InlineKeyboardMarkup()
	     		mnm.row_width = 1
	     		mnm.add(prix)
	     		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"WaiT For HunT MY FrienD\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nin User : {us}\nEmail : {email}\nUnavailable : {Un}\nAvailable : {An}\nCheck : {ch}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nBY : @MMPMMMM"),parse_mode='markdown',reply_markup=mnm)
	     		
	     		
def mailr2(message):
     	An = 0
     	Un = 0
     	ch = 0
     	Fal = 0
     	z = 0
     	user = '1q2w3e4rt5yu6io7paos8dfogh9jk0lzxcvbbnm'
     	for im in range(5000):
     		us = str(''.join((random.choice(user) for i in range(5))))
     		email = us+'@mail.ru'
     		url = f"https://check.moahmedsalah.repl.co/api-v1/check-email/tiktok/?email={email}"
     		req = requests.get(url).text
     		print(req)
     		if 'False' in req:
	     		Fal+=1
	     		print(f"Email Not Linked Tik Tok\n{email}\n\n")
	     	if "True" in req:
	     		print(f"Email Available Linked Tik Tok\n{email}\n\n")
	     		head = {
		  "user-agent": str(generate_user_agent()),
	     	}
	     		url = f"https://account.mail.ru/api/v1/user/exists?email={email}"
	     		req = requests.post(url, headers=head).text
	     		print(req)
	     		if '"exists":true' in req:
	     			Un+=1
	     			print("UnAvailable")
	     		if '"exists":false' in req:
	     			An+=1
	     			print("Available  :   {mail}")
	     			url = f"https://alkabby4api.pythonanywhere.com/info/tiktok?user={us}"
	     			ree = requests.get(url).json()
	     			Name = str(ree['Name'])
	     			Followers = str(ree['Followers'])
	     			Following = str(ree['Following'])
	     			Likes = str(ree['Likes'])
	     			bot.send_message(message.chat.id,f"""SuFi BoT New HuNteR
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
User : {us}
Name : {Name}
Followers : {Followers}
Following : {Following}
Likes : {Likes}
Email : {email}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
Tele : @MMPMMMM""")
	     		else:
	     			print("fales")
	     			z+=1
	     	else:
	     		ch+=1
	     		prix  = types.InlineKeyboardButton(text = "Developer", url = 'https://t.me/MMPMMMM')
	     		mnm = types.InlineKeyboardMarkup()
	     		mnm.row_width = 1
	     		mnm.add(prix)
	     		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"WaiT For HunT MY FrienD\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nin User : {us}\nEmail : {email}\nUnavailable : {Un}\nAvailable : {An}\nCheck : {ch}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nBY : @MMPMMMM"),parse_mode='markdown',reply_markup=mnm)
	
def mailr3(message):
     	An = 0
     	Un = 0
     	ch = 0
     	Fal = 0
     	z = 0
     	user = '1q2w3e4rt5yu6io7paos8dfogh9jk0lzxcvbbnm'
     	for im in range(5000):
     		us = str(''.join((random.choice(user) for i in range(6))))
     		email = us+'@mail.ru'
     		url = f"https://check.moahmedsalah.repl.co/api-v1/check-email/tiktok/?email={email}"
     		req = requests.get(url).text
     		print(req)
     		if 'False' in req:
	     		Fal+=1
	     		print(f"Email Not Linked Tik Tok\n{email}\n\n")
	     	if "True" in req:
	     		print(f"Email Available Linked Tik Tok\n{email}\n\n")
	     		head = {
		  "user-agent": str(generate_user_agent()),
	     	}
	     		url = f"https://account.mail.ru/api/v1/user/exists?email={email}"
	     		req = requests.post(url, headers=head).text
	     		print(req)
	     		if '"exists":true' in req:
	     			Un+=1
	     			print("UnAvailable")
	     		if '"exists":false' in req:
	     			An+=1
	     			print("Available  :   {mail}")
	     			url = f"https://alkabby4api.pythonanywhere.com/info/tiktok?user={us}"
	     			ree = requests.get(url).json()
	     			Name = str(ree['Name'])
	     			Followers = str(ree['Followers'])
	     			Following = str(ree['Following'])
	     			Likes = str(ree['Likes'])
	     			bot.send_message(message.chat.id,f"""SuFi BoT New HuNteR
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
User : {us}
Name : {Name}
Followers : {Followers}
Following : {Following}
Likes : {Likes}
Email : {email}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
Tele : @MMPMMMM""")
	     		else:
	     			print("fales")
	     			z+=1
	     	else:
	     		ch+=1
	     		prix  = types.InlineKeyboardButton(text = "Developer", url = 'https://t.me/MMPMMMM')
	     		mnm = types.InlineKeyboardMarkup()
	     		mnm.row_width = 1
	     		mnm.add(prix)
	     		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"WaiT For HunT MY FrienD\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nin User : {us}\nEmail : {email}\nUnavailable : {Un}\nAvailable : {An}\nCheck : {ch}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nBY : @MMPMMMM"),parse_mode='markdown',reply_markup=mnm)
	     		
def mailr4(message):
     	An = 0
     	Un = 0
     	ch = 0
     	Fal = 0
     	z = 0
     	user = '1q2w3e4rt5yu6io7paos8dfogh9jk0lzxcvbbnm'
     	for im in range(5000):
     		us = str(''.join((random.choice(user) for i in range(7))))
     		email = us+'@mail.ru'
     		url = f"https://check.moahmedsalah.repl.co/api-v1/check-email/tiktok/?email={email}"
     		req = requests.get(url).text
     		print(req)
     		if 'False' in req:
	     		Fal+=1
	     		print(f"Email Not Linked Tik Tok\n{email}\n\n")
	     	if "True" in req:
	     		print(f"Email Available Linked Tik Tok\n{email}\n\n")
	     		head = {
		  "user-agent": str(generate_user_agent()),
	     	}
	     		url = f"https://account.mail.ru/api/v1/user/exists?email={email}"
	     		req = requests.post(url, headers=head).text
	     		print(req)
	     		if '"exists":true' in req:
	     			Un+=1
	     			print("UnAvailable")
	     		if '"exists":false' in req:
	     			An+=1
	     			print("Available  :   {mail}")
	     			url = f"https://alkabby4api.pythonanywhere.com/info/tiktok?user={us}"
	     			ree = requests.get(url).json()
	     			Name = str(ree['Name'])
	     			Followers = str(ree['Followers'])
	     			Following = str(ree['Following'])
	     			Likes = str(ree['Likes'])
	     			bot.send_message(message.chat.id,f"""SuFi BoT New HuNteR
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
User : {us}
Name : {Name}
Followers : {Followers}
Following : {Following}
Likes : {Likes}
Email : {email}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
Tele : @MMPMMMM""")
	     		else:
	     			print("fales")
	     			z+=1
	     	else:
	     		ch+=1
	     		prix  = types.InlineKeyboardButton(text = "Developer", url = 'https://t.me/MMPMMMM')
	     		mnm = types.InlineKeyboardMarkup()
	     		mnm.row_width = 1
	     		mnm.add(prix)
	     		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"WaiT For HunT MY FrienD\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nin User : {us}\nEmail : {email}\nUnavailable : {Un}\nAvailable : {An}\nCheck : {ch}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nBY : @MMPMMMM"),parse_mode='markdown',reply_markup=mnm)	  
	
	
def ya1(message):
	     An = 0
	     Un = 0
	     ch = 0
	     z = 0
	     user = '1q2w3e4rt5yu6io7paos8dfogh9jk0lzxcvbbnm'
	     for im in range(5000):
	     	us = str(''.join((random.choice(user) for i in range(4))))
	     	email = us+'@yahoo.com'
	     	url = f"https://check.moahmedsalah.repl.co/api-v1/check-email/tiktok/?email={email}"
	     	req = requests.get(url).text
	     	print(req)
	     	if 'False' in req:
	     		print(f"Email Not Linked Tik Tok\n{email}\n\n")
	     	if "True" in req:
	     		print(f"Email Available Linked Tik Tok\n{email}\n\n")
	     		url = 'https://login.yahoo.com/account/module/create?validateField=yid'
	     		headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '18027',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'B=5gsr3qhgv30ah&b=3&s=4j; A1=d=AQABBFGB8WECEB1BGQBpDndGxwOUC9Rjc1gFEgEBBgFqI2LvYlxXb2UB_eMBAAcIUYHxYdRjc1g&S=AQAAAj5BvWvy6pR5f2C2qcz1rP0; A3=d=AQABBFGB8WECEB1BGQBpDndGxwOUC9Rjc1gFEgEBBgFqI2LvYlxXb2UB_eMBAAcIUYHxYdRjc1g&S=AQAAAj5BvWvy6pR5f2C2qcz1rP0; GUC=AQEBBgFiI2pi70IgYASX; A1S=d=AQABBFGB8WECEB1BGQBpDndGxwOUC9Rjc1gFEgEBBgFqI2LvYlxXb2UB_eMBAAcIUYHxYdRjc1g&S=AQAAAj5BvWvy6pR5f2C2qcz1rP0&j=WORLD; cmp=t=1648955763&j=0; AS=v=1&s=2PCvHGnT&d=B624a6828|huO_Mmz.2SrYAJxT6NSU2_dHCCDO0rBnrpbReXLcvBwg3vd1h1xRO60PUKFX1stdT9jv880ARoWXql4v5oNff_7opA__g55tnsZ3GeP7eVYMKPwt7ZX0hy4Q52POE4wG1nE9Kz8ndcVlafKZkJsiapuYKpLi.swuLypX6m50DkIiyhGiX13IA_xsSa5MfBRj7rQ13tJ7_DOiE7.elO35puHC2k.6BRvyTf82SGx6GJddodEgtakF7Ig8yyHTeheeY2HENlmK7df1bFx_AjA7xhbLewTzdd6.x7EaSAs_21wLbJwqyZstujGHuy7nNPjGHa.s2skOEusqgNZPUGRR3yn9p9ww8CaT64dQDFsyv9XYdw11iYgRvbklC4NWJ5nhrKtQzS6_sHTLkvfP3x.1xEzj50q3qSZ3hVdqW8_AxVpVOM2yJIvU0tL6ykVKLI_4.Pz2N0VmiikF5HEoVhttSmrnfh2OKgPg_rHDUMBFI6UNvEs_cW2BFv9B5KpZbEV26S_8RObVz1h71kRZUxYVEUVAanjb.1UzD1ptR53D_HpbJwzvKT4gP9O2C_7IPXXeW8pzsbgKsGoIwekQsxSh1qecPcFa0XK0N59_vkOhhfZHhAOJ4ojzSlJNfd6UAExFoRtagCbEudexVCdBzDmVvxBuzs1QxMs8R10WXJ1rnLTwbmT2R1Gf.jEnkj2yIp.FywrpHCcpy5Ty8MKDrpID7QZ78iF018LPaC2u0I4HyP.0Wp5LDaYzyYYLUI4n4cAc6ml_jN.rVRzOoC7k8UU8b2AOlg5QaqZKJ7Y8JWqLcyGUYE8kufvWckcUALl3_1FKc5BdsXwyZLr5TnlumI5eroXm3ijMSwNpMvdzrHzrde3JVmvLO1dGBu.e6CiyKMPXfe6B65h4uq1USspktfo-~A',
    'Host': 'login.yahoo.com',
    'Origin': 'https://login.yahoo.com',
    'Referer': 'https://login.yahoo.com/account/create?.lang=ar-JO&src=homepage&specId=yidReg&done=https%3A%2F%2Fwww.yahoo.com',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': str(generate_user_agent()),
    'X-Requested-With': 'XMLHttpRequest'}
	     		data = {
'browser-fp-data': '{"language":"ar","colorDepth":24,"deviceMemory":2,"pixelRatio":1,"hardwareConcurrency":2,"timezoneOffset":-180,"timezone":"Asia/Baghdad","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":5,"hash":"2c14024bf8584c3f7f63f24ea490e812"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc. (NVIDIA)~ANGLE (NVIDIA, NVIDIA Quadro FX 360M  Direct3D11 vs_4_0 ps_4_0, D3D11)","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":49,"hash":"411659924ff38420049ac402a30466bc"},"audio":"124.04347527516074","resolution":{"w":"1280","h":"800"},"availableResolution":{"w":"760","h":"1280"},"ts":{"serve":1649039063588,"render":1649039065281}}',
'specId': 'yidReg',
'crumb': 'Si.2mSpANy1',
'acrumb': '2PCvHGnT',
'done': 'https://www.yahoo.com',
'attrSetIndex': '0',
'tos0': 'oath_freereg|xa|en-JO',
"firstName": "Sufi",
"lastName": "saad",
'yid': str(email),
'password': 'Mustafasaad1',
"shortCountryCode": "AF",
"phone": "205753557",
"freeformGender": "boy",
    }
	     		response = requests.post(url,headers=headers,data=data).text
	     		print(response)
	     		print(email)
	     		if ('"yid"') in response:
	     			print("غير متاح")
	     			Un+=1
	     		elif ('"birthDate"') in response:
	     			An+=1
	     			print("متاح ")
	     			url = f"https://alkabby4api.pythonanywhere.com/info/tiktok?user={us}"
	     			ree = requests.get(url).json()
	     			Name = str(ree['Name'])
	     			Followers = str(ree['Followers'])
	     			Following = str(ree['Following'])
	     			Likes = str(ree['Likes'])
	     			bot.send_message(message.chat.id,f"""SuFi BoT New HuNteR
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
User : {us}
Name : {Name}
Followers : {Followers}
Following : {Following}
Likes : {Likes}
Email : {email}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
Tele : @MMPMMMM""")
	     		else:
	     			print("fales")
	     			z+=1
	     	else:
	     		ch+=1
	     		prix  = types.InlineKeyboardButton(text = "Developer", url = 'https://t.me/MMPMMMM')
	     		mnm = types.InlineKeyboardMarkup()
	     		mnm.row_width = 1
	     		mnm.add(prix)
	     		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"WaiT For HunT MY FrienD\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nin User : {us}\nEmail : {email}\nUnavailable : {Un}\nAvailable : {An}\nCheck : {ch}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nBY : @MMPMMMM"),parse_mode='markdown',reply_markup=mnm)	
	     		
def ya2(message):
	     An = 0
	     Un = 0
	     ch = 0
	     Fal = 0
	     z = 0
	     user = '1q2w3e4rt5yu6io7paos8dfogh9jk0lzxcvbbnm'
	     for im in range(5000):
	     	us = str(''.join((random.choice(user) for i in range(5))))
	     	email = us+'@yahoo.com'
	     	url = f"https://check.moahmedsalah.repl.co/api-v1/check-email/tiktok/?email={email}"
	     	req = requests.get(url).text
	     	print(req)
	     	if 'False' in req:
	     		Fal+=1
	     		print(f"Email Not Linked Tik Tok\n{email}\n\n")
	     	if "True" in req:
	     		print(f"Email Available Linked Tik Tok\n{email}\n\n")
	     		url = 'https://login.yahoo.com/account/module/create?validateField=yid'
	     		headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '18027',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'B=5gsr3qhgv30ah&b=3&s=4j; A1=d=AQABBFGB8WECEB1BGQBpDndGxwOUC9Rjc1gFEgEBBgFqI2LvYlxXb2UB_eMBAAcIUYHxYdRjc1g&S=AQAAAj5BvWvy6pR5f2C2qcz1rP0; A3=d=AQABBFGB8WECEB1BGQBpDndGxwOUC9Rjc1gFEgEBBgFqI2LvYlxXb2UB_eMBAAcIUYHxYdRjc1g&S=AQAAAj5BvWvy6pR5f2C2qcz1rP0; GUC=AQEBBgFiI2pi70IgYASX; A1S=d=AQABBFGB8WECEB1BGQBpDndGxwOUC9Rjc1gFEgEBBgFqI2LvYlxXb2UB_eMBAAcIUYHxYdRjc1g&S=AQAAAj5BvWvy6pR5f2C2qcz1rP0&j=WORLD; cmp=t=1648955763&j=0; AS=v=1&s=2PCvHGnT&d=B624a6828|huO_Mmz.2SrYAJxT6NSU2_dHCCDO0rBnrpbReXLcvBwg3vd1h1xRO60PUKFX1stdT9jv880ARoWXql4v5oNff_7opA__g55tnsZ3GeP7eVYMKPwt7ZX0hy4Q52POE4wG1nE9Kz8ndcVlafKZkJsiapuYKpLi.swuLypX6m50DkIiyhGiX13IA_xsSa5MfBRj7rQ13tJ7_DOiE7.elO35puHC2k.6BRvyTf82SGx6GJddodEgtakF7Ig8yyHTeheeY2HENlmK7df1bFx_AjA7xhbLewTzdd6.x7EaSAs_21wLbJwqyZstujGHuy7nNPjGHa.s2skOEusqgNZPUGRR3yn9p9ww8CaT64dQDFsyv9XYdw11iYgRvbklC4NWJ5nhrKtQzS6_sHTLkvfP3x.1xEzj50q3qSZ3hVdqW8_AxVpVOM2yJIvU0tL6ykVKLI_4.Pz2N0VmiikF5HEoVhttSmrnfh2OKgPg_rHDUMBFI6UNvEs_cW2BFv9B5KpZbEV26S_8RObVz1h71kRZUxYVEUVAanjb.1UzD1ptR53D_HpbJwzvKT4gP9O2C_7IPXXeW8pzsbgKsGoIwekQsxSh1qecPcFa0XK0N59_vkOhhfZHhAOJ4ojzSlJNfd6UAExFoRtagCbEudexVCdBzDmVvxBuzs1QxMs8R10WXJ1rnLTwbmT2R1Gf.jEnkj2yIp.FywrpHCcpy5Ty8MKDrpID7QZ78iF018LPaC2u0I4HyP.0Wp5LDaYzyYYLUI4n4cAc6ml_jN.rVRzOoC7k8UU8b2AOlg5QaqZKJ7Y8JWqLcyGUYE8kufvWckcUALl3_1FKc5BdsXwyZLr5TnlumI5eroXm3ijMSwNpMvdzrHzrde3JVmvLO1dGBu.e6CiyKMPXfe6B65h4uq1USspktfo-~A',
    'Host': 'login.yahoo.com',
    'Origin': 'https://login.yahoo.com',
    'Referer': 'https://login.yahoo.com/account/create?.lang=ar-JO&src=homepage&specId=yidReg&done=https%3A%2F%2Fwww.yahoo.com',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': str(generate_user_agent()),
    'X-Requested-With': 'XMLHttpRequest'}
	     		data = {
'browser-fp-data': '{"language":"ar","colorDepth":24,"deviceMemory":2,"pixelRatio":1,"hardwareConcurrency":2,"timezoneOffset":-180,"timezone":"Asia/Baghdad","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":5,"hash":"2c14024bf8584c3f7f63f24ea490e812"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc. (NVIDIA)~ANGLE (NVIDIA, NVIDIA Quadro FX 360M  Direct3D11 vs_4_0 ps_4_0, D3D11)","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":49,"hash":"411659924ff38420049ac402a30466bc"},"audio":"124.04347527516074","resolution":{"w":"1280","h":"800"},"availableResolution":{"w":"760","h":"1280"},"ts":{"serve":1649039063588,"render":1649039065281}}',
'specId': 'yidReg',
'crumb': 'Si.2mSpANy1',
'acrumb': '2PCvHGnT',
'done': 'https://www.yahoo.com',
'attrSetIndex': '0',
'tos0': 'oath_freereg|xa|en-JO',
"firstName": "Sufi",
"lastName": "saad",
'yid': str(email),
'password': 'Mustafasaad1',
"shortCountryCode": "AF",
"phone": "205753557",
"freeformGender": "boy",
    }
	     		response = requests.post(url,headers=headers,data=data).text
	     		print(response)
	     		print(email)
	     		if ('"yid"') in response:
	     			Un+=1
	     			print("غير متاح")
	     		elif ('"birthDate"') in response:
	     			An+=1
	     			print("متاح ")
	     			url = f"https://alkabby4api.pythonanywhere.com/info/tiktok?user={us}"
	     			ree = requests.get(url).json()
	     			Name = str(ree['Name'])
	     			Followers = str(ree['Followers'])
	     			Following = str(ree['Following'])
	     			Likes = str(ree['Likes'])
	     			bot.send_message(message.chat.id,f"""SuFi BoT New HuNteR
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
User : {us}
Name : {Name}
Followers : {Followers}
Following : {Following}
Likes : {Likes}
Email : {email}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
Tele : @MMPMMMM""")
	     		else:
	     			print("fales")
	     			z+=1
	     	else:
	     		ch+=1
	     		prix  = types.InlineKeyboardButton(text = "Developer", url = 'https://t.me/MMPMMMM')
	     		mnm = types.InlineKeyboardMarkup()
	     		mnm.row_width = 1
	     		mnm.add(prix)
	     		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"WaiT For HunT MY FrienD\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nin User : {us}\nEmail : {email}\nUnavailable : {Un}\nAvailable : {An}\nCheck : {ch}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nBY : @MMPMMMM"),parse_mode='markdown',reply_markup=mnm)
	     		
def ya3(message):
	     An = 0
	     Un = 0
	     ch = 0
	     Fal = 0
	     z = 0
	     user = '1q2w3e4rt5yu6io7paos8dfogh9jk0lzxcvbbnm'
	     for im in range(5000):
	     	us = str(''.join((random.choice(user) for i in range(6))))
	     	email = us+'@yahoo.com'
	     	url = f"https://check.moahmedsalah.repl.co/api-v1/check-email/tiktok/?email={email}"
	     	req = requests.get(url).text
	     	print(req)
	     	if 'False' in req:
	     		Fal+=1
	     		print(f"Email Not Linked Tik Tok\n{email}\n\n")
	     	if "True" in req:
	     		print(f"Email Available Linked Tik Tok\n{email}\n\n")
	     		url = 'https://login.yahoo.com/account/module/create?validateField=yid'
	     		headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '18027',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'B=5gsr3qhgv30ah&b=3&s=4j; A1=d=AQABBFGB8WECEB1BGQBpDndGxwOUC9Rjc1gFEgEBBgFqI2LvYlxXb2UB_eMBAAcIUYHxYdRjc1g&S=AQAAAj5BvWvy6pR5f2C2qcz1rP0; A3=d=AQABBFGB8WECEB1BGQBpDndGxwOUC9Rjc1gFEgEBBgFqI2LvYlxXb2UB_eMBAAcIUYHxYdRjc1g&S=AQAAAj5BvWvy6pR5f2C2qcz1rP0; GUC=AQEBBgFiI2pi70IgYASX; A1S=d=AQABBFGB8WECEB1BGQBpDndGxwOUC9Rjc1gFEgEBBgFqI2LvYlxXb2UB_eMBAAcIUYHxYdRjc1g&S=AQAAAj5BvWvy6pR5f2C2qcz1rP0&j=WORLD; cmp=t=1648955763&j=0; AS=v=1&s=2PCvHGnT&d=B624a6828|huO_Mmz.2SrYAJxT6NSU2_dHCCDO0rBnrpbReXLcvBwg3vd1h1xRO60PUKFX1stdT9jv880ARoWXql4v5oNff_7opA__g55tnsZ3GeP7eVYMKPwt7ZX0hy4Q52POE4wG1nE9Kz8ndcVlafKZkJsiapuYKpLi.swuLypX6m50DkIiyhGiX13IA_xsSa5MfBRj7rQ13tJ7_DOiE7.elO35puHC2k.6BRvyTf82SGx6GJddodEgtakF7Ig8yyHTeheeY2HENlmK7df1bFx_AjA7xhbLewTzdd6.x7EaSAs_21wLbJwqyZstujGHuy7nNPjGHa.s2skOEusqgNZPUGRR3yn9p9ww8CaT64dQDFsyv9XYdw11iYgRvbklC4NWJ5nhrKtQzS6_sHTLkvfP3x.1xEzj50q3qSZ3hVdqW8_AxVpVOM2yJIvU0tL6ykVKLI_4.Pz2N0VmiikF5HEoVhttSmrnfh2OKgPg_rHDUMBFI6UNvEs_cW2BFv9B5KpZbEV26S_8RObVz1h71kRZUxYVEUVAanjb.1UzD1ptR53D_HpbJwzvKT4gP9O2C_7IPXXeW8pzsbgKsGoIwekQsxSh1qecPcFa0XK0N59_vkOhhfZHhAOJ4ojzSlJNfd6UAExFoRtagCbEudexVCdBzDmVvxBuzs1QxMs8R10WXJ1rnLTwbmT2R1Gf.jEnkj2yIp.FywrpHCcpy5Ty8MKDrpID7QZ78iF018LPaC2u0I4HyP.0Wp5LDaYzyYYLUI4n4cAc6ml_jN.rVRzOoC7k8UU8b2AOlg5QaqZKJ7Y8JWqLcyGUYE8kufvWckcUALl3_1FKc5BdsXwyZLr5TnlumI5eroXm3ijMSwNpMvdzrHzrde3JVmvLO1dGBu.e6CiyKMPXfe6B65h4uq1USspktfo-~A',
    'Host': 'login.yahoo.com',
    'Origin': 'https://login.yahoo.com',
    'Referer': 'https://login.yahoo.com/account/create?.lang=ar-JO&src=homepage&specId=yidReg&done=https%3A%2F%2Fwww.yahoo.com',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': str(generate_user_agent()),
    'X-Requested-With': 'XMLHttpRequest'}
	     		data = {
'browser-fp-data': '{"language":"ar","colorDepth":24,"deviceMemory":2,"pixelRatio":1,"hardwareConcurrency":2,"timezoneOffset":-180,"timezone":"Asia/Baghdad","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":5,"hash":"2c14024bf8584c3f7f63f24ea490e812"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc. (NVIDIA)~ANGLE (NVIDIA, NVIDIA Quadro FX 360M  Direct3D11 vs_4_0 ps_4_0, D3D11)","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":49,"hash":"411659924ff38420049ac402a30466bc"},"audio":"124.04347527516074","resolution":{"w":"1280","h":"800"},"availableResolution":{"w":"760","h":"1280"},"ts":{"serve":1649039063588,"render":1649039065281}}',
'specId': 'yidReg',
'crumb': 'Si.2mSpANy1',
'acrumb': '2PCvHGnT',
'done': 'https://www.yahoo.com',
'attrSetIndex': '0',
'tos0': 'oath_freereg|xa|en-JO',
"firstName": "Sufi",
"lastName": "saad",
'yid': str(email),
'password': 'Mustafasaad1',
"shortCountryCode": "AF",
"phone": "205753557",
"freeformGender": "boy",
    }
	     		response = requests.post(url,headers=headers,data=data).text
	     		print(response)
	     		print(email)
	     		if ('"yid"') in response:
	     			Un+=1
	     			print("غير متاح")
	     		elif ('"birthDate"') in response:
	     			An+=1
	     			print("متاح ")
	     			url = f"https://alkabby4api.pythonanywhere.com/info/tiktok?user={us}"
	     			ree = requests.get(url).json()
	     			Name = str(ree['Name'])
	     			Followers = str(ree['Followers'])
	     			Following = str(ree['Following'])
	     			Likes = str(ree['Likes'])
	     			bot.send_message(message.chat.id,f"""SuFi BoT New HuNteR
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
User : {us}
Name : {Name}
Followers : {Followers}
Following : {Following}
Likes : {Likes}
Email : {email}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
Tele : @MMPMMMM""")
	     		else:
	     			print("fales")
	     			z+=1
	     	else:
	     		ch+=1
	     		prix  = types.InlineKeyboardButton(text = "Developer", url = 'https://t.me/MMPMMMM')
	     		mnm = types.InlineKeyboardMarkup()
	     		mnm.row_width = 1
	     		mnm.add(prix)
	     		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"WaiT For HunT MY FrienD\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nin User : {us}\nEmail : {email}\nUnavailable : {Un}\nAvailable : {An}\nCheck : {ch}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nBY : @MMPMMMM"),parse_mode='markdown',reply_markup=mnm)
	     		
def ya4(message):
	     An = 0
	     Un = 0
	     ch = 0
	     Fal = 0
	     z = 0
	     user = '1q2w3e4rt5yu6io7paos8dfogh9jk0lzxcvbbnm'
	     for im in range(5000):
	     	us = str(''.join((random.choice(user) for i in range(7))))
	     	email = us+'@yahoo.com'
	     	url = f"https://check.moahmedsalah.repl.co/api-v1/check-email/tiktok/?email={email}"
	     	req = requests.get(url).text
	     	print(req)
	     	if 'False' in req:
	     		Fal+=1
	     		print(f"Email Not Linked Tik Tok\n{email}\n\n")
	     	if "True" in req:
	     		print(f"Email Available Linked Tik Tok\n{email}\n\n")
	     		url = 'https://login.yahoo.com/account/module/create?validateField=yid'
	     		headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '18027',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'B=5gsr3qhgv30ah&b=3&s=4j; A1=d=AQABBFGB8WECEB1BGQBpDndGxwOUC9Rjc1gFEgEBBgFqI2LvYlxXb2UB_eMBAAcIUYHxYdRjc1g&S=AQAAAj5BvWvy6pR5f2C2qcz1rP0; A3=d=AQABBFGB8WECEB1BGQBpDndGxwOUC9Rjc1gFEgEBBgFqI2LvYlxXb2UB_eMBAAcIUYHxYdRjc1g&S=AQAAAj5BvWvy6pR5f2C2qcz1rP0; GUC=AQEBBgFiI2pi70IgYASX; A1S=d=AQABBFGB8WECEB1BGQBpDndGxwOUC9Rjc1gFEgEBBgFqI2LvYlxXb2UB_eMBAAcIUYHxYdRjc1g&S=AQAAAj5BvWvy6pR5f2C2qcz1rP0&j=WORLD; cmp=t=1648955763&j=0; AS=v=1&s=2PCvHGnT&d=B624a6828|huO_Mmz.2SrYAJxT6NSU2_dHCCDO0rBnrpbReXLcvBwg3vd1h1xRO60PUKFX1stdT9jv880ARoWXql4v5oNff_7opA__g55tnsZ3GeP7eVYMKPwt7ZX0hy4Q52POE4wG1nE9Kz8ndcVlafKZkJsiapuYKpLi.swuLypX6m50DkIiyhGiX13IA_xsSa5MfBRj7rQ13tJ7_DOiE7.elO35puHC2k.6BRvyTf82SGx6GJddodEgtakF7Ig8yyHTeheeY2HENlmK7df1bFx_AjA7xhbLewTzdd6.x7EaSAs_21wLbJwqyZstujGHuy7nNPjGHa.s2skOEusqgNZPUGRR3yn9p9ww8CaT64dQDFsyv9XYdw11iYgRvbklC4NWJ5nhrKtQzS6_sHTLkvfP3x.1xEzj50q3qSZ3hVdqW8_AxVpVOM2yJIvU0tL6ykVKLI_4.Pz2N0VmiikF5HEoVhttSmrnfh2OKgPg_rHDUMBFI6UNvEs_cW2BFv9B5KpZbEV26S_8RObVz1h71kRZUxYVEUVAanjb.1UzD1ptR53D_HpbJwzvKT4gP9O2C_7IPXXeW8pzsbgKsGoIwekQsxSh1qecPcFa0XK0N59_vkOhhfZHhAOJ4ojzSlJNfd6UAExFoRtagCbEudexVCdBzDmVvxBuzs1QxMs8R10WXJ1rnLTwbmT2R1Gf.jEnkj2yIp.FywrpHCcpy5Ty8MKDrpID7QZ78iF018LPaC2u0I4HyP.0Wp5LDaYzyYYLUI4n4cAc6ml_jN.rVRzOoC7k8UU8b2AOlg5QaqZKJ7Y8JWqLcyGUYE8kufvWckcUALl3_1FKc5BdsXwyZLr5TnlumI5eroXm3ijMSwNpMvdzrHzrde3JVmvLO1dGBu.e6CiyKMPXfe6B65h4uq1USspktfo-~A',
    'Host': 'login.yahoo.com',
    'Origin': 'https://login.yahoo.com',
    'Referer': 'https://login.yahoo.com/account/create?.lang=ar-JO&src=homepage&specId=yidReg&done=https%3A%2F%2Fwww.yahoo.com',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': str(generate_user_agent()),
    'X-Requested-With': 'XMLHttpRequest'}
	     		data = {
'browser-fp-data': '{"language":"ar","colorDepth":24,"deviceMemory":2,"pixelRatio":1,"hardwareConcurrency":2,"timezoneOffset":-180,"timezone":"Asia/Baghdad","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":5,"hash":"2c14024bf8584c3f7f63f24ea490e812"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc. (NVIDIA)~ANGLE (NVIDIA, NVIDIA Quadro FX 360M  Direct3D11 vs_4_0 ps_4_0, D3D11)","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":49,"hash":"411659924ff38420049ac402a30466bc"},"audio":"124.04347527516074","resolution":{"w":"1280","h":"800"},"availableResolution":{"w":"760","h":"1280"},"ts":{"serve":1649039063588,"render":1649039065281}}',
'specId': 'yidReg',
'crumb': 'Si.2mSpANy1',
'acrumb': '2PCvHGnT',
'done': 'https://www.yahoo.com',
'attrSetIndex': '0',
'tos0': 'oath_freereg|xa|en-JO',
"firstName": "Sufi",
"lastName": "saad",
'yid': str(email),
'password': 'Mustafasaad1',
"shortCountryCode": "AF",
"phone": "205753557",
"freeformGender": "boy",
    }
	     		response = requests.post(url,headers=headers,data=data).text
	     		print(response)
	     		print(email)
	     		if ('"yid"') in response:
	     			Un+=1
	     			print("غير متاح")
	     		elif ('"birthDate"') in response:
	     			An+=1
	     			print("متاح ")
	     			url = f"https://alkabby4api.pythonanywhere.com/info/tiktok?user={us}"
	     			ree = requests.get(url).json()
	     			Name = str(ree['Name'])
	     			Followers = str(ree['Followers'])
	     			Following = str(ree['Following'])
	     			Likes = str(ree['Likes'])
	     			bot.send_message(message.chat.id,f"""SuFi BoT New HuNteR
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
User : {us}
Name : {Name}
Followers : {Followers}
Following : {Following}
Likes : {Likes}
Email : {email}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
Tele : @MMPMMMM""")
	     		else:
	     			print("fales")
	     			z+=1
	     	else:
	     		ch+=1
	     		prix  = types.InlineKeyboardButton(text = "Developer", url = 'https://t.me/MMPMMMM')
	     		mnm = types.InlineKeyboardMarkup()
	     		mnm.row_width = 1
	     		mnm.add(prix)
	     		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"WaiT For HunT MY FrienD\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nin User : {us}\nEmail : {email}\nUnavailable : {Un}\nAvailable : {An}\nCheck : {ch}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nBY : @MMPMMMM"),parse_mode='markdown',reply_markup=mnm)
	     		
def oo1(message):
	An = 0
	Un = 0
	ch = 0
	Fal = 0
	z = 0
	user = '1q2w3e4rt5yu6io7paos8dfogh9jk0lzxcvbbnm'
	for im in range(5000):
		us = str(''.join((random.choice(user) for i in range(7))))
		email = us+'@outlook.com'
		url = f"https://check.moahmedsalah.repl.co/api-v1/check-email/tiktok/?email={email}"
		req = requests.get(url).text
		print(req)
		if 'False' in req:
			Fal+=1
			print(f"Email Not Linked Tik Tok\n{email}\n\n")
		if "True" in req:
			print(f"Email Available Linked Tik Tok\n{email}\n\n")
			url = f"https://signup.live.com/signup?username={email}"
			headers = {
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US;q=0.9,en;q=0.8",
"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "Windows",
"sec-fetch-dest": "document",
"sec-fetch-mode": "navigate",
"sec-fetch-site": "none",
"sec-fetch-user": "?1",
"upgrade-insecure-requests": "1",
"User-Agent": str(generate_user_agent()),
}
			data = {'username': str(email),}
			req = requests.post(url,
			headers=headers, data=data).text
			if '"isAvailable":1' in req:
			 An+=1
			 print(f"Available   :   {email}")
			 mol = (f"""Email Availabla\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nEmail : {email}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nTele : @MMPMMMM""")
			 print(mol)
			 url = f"https://alkabby4api.pythonanywhere.com/info/tiktok?user={us}"
			 ree = requests.get(url).json()
			 Name = str(ree['Name'])
			 Followers = str(ree['Followers'])
			 Following = str(ree['Following'])
			 Likes = str(ree['Likes'])
			 bot.send_message(message.chat.id,f""" SuFi BoT New HuNteR
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
User : {us}
Name : {Name}
Followers : {Followers}
Following : {Following}
Likes : {Likes}
Email : {email}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
Tele : @MMPMMMM""")
			 
			else:
				Un+=1
				print("ليس متاح")
				z+=1
		else:
			ch+=1
			prix  = types.InlineKeyboardButton(text = "Developer", url = 'https://t.me/MMPMMMM')
			mnm = types.InlineKeyboardMarkup()
			mnm.row_width = 1
			mnm.add(prix)
			bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"WaiT For HunT MY FrienD\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nin User : {us}\nEmail : {email}\nUnavailable : {Un}\nAvailable : {An}\nCheck : {ch}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nBY : @MMPMMMM"),parse_mode='markdown',reply_markup=mnm)		


def oo2(message):
	An = 0
	Un = 0
	ch = 0
	Fal = 0
	z = 0
	user = '1q2w3e4rt5yu6io7paos8dfogh9jk0lzxcvbbnm'
	for im in range(5000):
		us = str(''.join((random.choice(user) for i in range(6))))
		email = us+'@outlook.com'
		url = f"https://check.moahmedsalah.repl.co/api-v1/check-email/tiktok/?email={email}"
		req = requests.get(url).text
		print(req)
		if 'False' in req:
			Fal+=1
			print(f"Email Not Linked Tik Tok\n{email}\n\n")
		if "True" in req:
			print(f"Email Available Linked Tik Tok\n{email}\n\n")
			url = f"https://signup.live.com/signup?username={email}"
			headers = {
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US;q=0.9,en;q=0.8",
"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "Windows",
"sec-fetch-dest": "document",
"sec-fetch-mode": "navigate",
"sec-fetch-site": "none",
"sec-fetch-user": "?1",
"upgrade-insecure-requests": "1",
"User-Agent": str(generate_user_agent()),
}
			data = {'username': str(email),}
			req = requests.post(url,
			headers=headers, data=data).text
			if '"isAvailable":1' in req:
			 An+=1
			 print(f"Available   :   {email}")
			 mol = (f"""Email Availabla\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nEmail : {email}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nTele : @MMPMMMM""")
			 print(mol)
			 url = f"https://alkabby4api.pythonanywhere.com/info/tiktok?user={us}"
			 ree = requests.get(url).json()
			 Name = str(ree['Name'])
			 Followers = str(ree['Followers'])
			 Following = str(ree['Following'])
			 Likes = str(ree['Likes'])
			 bot.send_message(message.chat.id,f""" SuFi BoT New HuNteR
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
User : {us}
Name : {Name}
Followers : {Followers}
Following : {Following}
Likes : {Likes}
Email : {email}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
Tele : @MMPMMMM""")
			 
			else:
				Un+=1
				print("ليس متاح")
				z+=1
		else:
			ch+=1
			prix  = types.InlineKeyboardButton(text = "Developer", url = 'https://t.me/MMPMMMM')
			mnm = types.InlineKeyboardMarkup()
			mnm.row_width = 1
			mnm.add(prix)
			bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"WaiT For HunT MY FrienD\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nin User : {us}\nEmail : {email}\nUnavailable : {Un}\nAvailable : {An}\nCheck : {ch}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nBY : @MMPMMMM"),parse_mode='markdown',reply_markup=mnm)

def oo3(message):
	An = 0
	Un = 0
	ch = 0
	Fal = 0
	z = 0
	user = '1q2w3e4rt5yu6io7paos8dfogh9jk0lzxcvbbnm'
	for im in range(5000):
		us = str(''.join((random.choice(user) for i in range(6))))
		email = us+'@outlook.com'
		url = f"https://check.moahmedsalah.repl.co/api-v1/check-email/tiktok/?email={email}"
		req = requests.get(url).text
		print(req)
		if 'False' in req:
			Fal+=1
			print(f"Email Not Linked Tik Tok\n{email}\n\n")
		if "True" in req:
			print(f"Email Available Linked Tik Tok\n{email}\n\n")
			url = f"https://signup.live.com/signup?username={email}"
			headers = {
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US;q=0.9,en;q=0.8",
"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "Windows",
"sec-fetch-dest": "document",
"sec-fetch-mode": "navigate",
"sec-fetch-site": "none",
"sec-fetch-user": "?1",
"upgrade-insecure-requests": "1",
"User-Agent": str(generate_user_agent()),
}
			data = {'username': str(email),}
			req = requests.post(url,
			headers=headers, data=data).text
			if '"isAvailable":1' in req:
			 An+=1
			 print(f"Available   :   {email}")
			 mol = (f"""Email Availabla\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nEmail : {email}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nTele : @MMPMMMM""")
			 print(mol)
			 url = f"https://alkabby4api.pythonanywhere.com/info/tiktok?user={us}"
			 ree = requests.get(url).json()
			 Name = str(ree['Name'])
			 Followers = str(ree['Followers'])
			 Following = str(ree['Following'])
			 Likes = str(ree['Likes'])
			 bot.send_message(message.chat.id,f""" SuFi BoT New HuNteR
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
User : {us}
Name : {Name}
Followers : {Followers}
Following : {Following}
Likes : {Likes}
Email : {email}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
Tele : @MMPMMMM""")
			else:
				Un+=1
				print("ليس متاح")
				z+=1
		else:
			ch+=1
			prix  = types.InlineKeyboardButton(text = "Developer", url = 'https://t.me/MMPMMMM')
			mnm = types.InlineKeyboardMarkup()
			mnm.row_width = 1
			mnm.add(prix)
			bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"WaiT For HunT MY FrienD\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nin User {us}\nEmail : {email}\nUnavailable : {Un}\nAvailable : {An}\nCheck : {ch}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nBY : @MMPMMMM"),parse_mode='markdown',reply_markup=mnm)		
			
def oo4(message):
	An = 0
	Un = 0
	ch = 0
	Fal = 0
	z = 0
	user = '1q2w3e4rt5yu6io7paos8dfogh9jk0lzxcvbbnm'
	for im in range(5000):
		us = str(''.join((random.choice(user) for i in range(7))))
		email = us+'@outlook.com'
		url = f"https://check.moahmedsalah.repl.co/api-v1/check-email/tiktok/?email={email}"
		req = requests.get(url).text
		print(req)
		if 'False' in req:
			Fal+=1
			print(f"Email Not Linked Tik Tok\n{email}\n\n")
		if "True" in req:
			print(f"Email Available Linked Tik Tok\n{email}\n\n")
			url = f"https://signup.live.com/signup?username={email}"
			headers = {
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US;q=0.9,en;q=0.8",
"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "Windows",
"sec-fetch-dest": "document",
"sec-fetch-mode": "navigate",
"sec-fetch-site": "none",
"sec-fetch-user": "?1",
"upgrade-insecure-requests": "1",
"User-Agent": str(generate_user_agent()),
}
			data = {'username': str(email),}
			req = requests.post(url,
			headers=headers, data=data).text
			if '"isAvailable":1' in req:
			 An+=1
			 print(f"Available   :   {email}")
			 mol = (f"""Email Availabla\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nEmail : {email}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nTele : @MMPMMMM""")
			 print(mol)
			 url = f"https://alkabby4api.pythonanywhere.com/info/tiktok?user={us}"
			 ree = requests.get(url).json()
			 Name = str(ree['Name'])
			 Followers = str(ree['Followers'])
			 Following = str(ree['Following'])
			 Likes = str(ree['Likes'])
			 bot.send_message(message.chat.id,f""" SuFi BoT New HuNteR
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
User : {us}
Name : {Name}
Followers : {Followers}
Following : {Following}
Likes : {Likes}
Email : {email}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
Tele : @MMPMMMM""")

			else:
				Un+=1
				print("ليس متاح")
				z+=1
		else:
			ch+=1
			prix  = types.InlineKeyboardButton(text = "Developer", url = 'https://t.me/MMPMMMM')
			mnm = types.InlineKeyboardMarkup()
			mnm.row_width = 1
			mnm.add(prix)
			bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"WaiT For HunT MY FrienD\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nin User : {us}\nEmail : {email}\nUnavailable : {Un}\nAvailable : {An}\nCheck : {ch}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nBY : @MMPMMMM"),parse_mode='markdown',reply_markup=mnm)	     										
def getcheck31(message):
	An = 0
	Un = 0
	ch = 0
	Fal = 0
	z = 0
	user = '1q2w3e4rt5yu6io7paos8dfogh9jk0lzxcvbbnm'
	for im in range(5000):
		us = str(''.join((random.choice(user) for i in range(7))))
		email = us+'@hotmail.com'
		url = f"https://check.moahmedsalah.repl.co/api-v1/check-email/tiktok/?email={email}"
		req = requests.get(url).text
		print(req)
		if 'False' in req:
			Fal+=1
			print(f"Email Not Linked Tik Tok\n{email}\n\n")
		if "True" in req:
			print(f"Email Available Linked Tik Tok\n{email}\n\n")
			url = f"https://signup.live.com/signup?username={email}"
			headers = {
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US;q=0.9,en;q=0.8",
"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "Windows",
"sec-fetch-dest": "document",
"sec-fetch-mode": "navigate",
"sec-fetch-site": "none",
"sec-fetch-user": "?1",
"upgrade-insecure-requests": "1",
"User-Agent": str(generate_user_agent()),
}
			data = {'username': str(email),}
			req = requests.post(url,
			headers=headers, data=data).text
			if '"isAvailable":1' in req:
			 An+=1
			 print(f"Available   :   {email}")
			 mol = (f"""Email Availabla\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nEmail : {email}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nTele : @MMPMMMM""")
			 print(mol)
			 url = f"https://alkabby4api.pythonanywhere.com/info/tiktok?user={us}"
			 ree = requests.get(url).json()
			 Name = str(ree['Name'])
			 Followers = str(ree['Followers'])
			 Following = str(ree['Following'])
			 Likes = str(ree['Likes'])
			 bot.send_message(message.chat.id,f""" SuFi BoT New HuNteR
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
User : {us}
Name : {Name}
Followers : {Followers}
Following : {Following}
Likes : {Likes}
Email : {email}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
Tele : @MMPMMMM""")
			 
			else:
				Un+=1
				print("ليس متاح")
				z+=1
		else:
			ch+=1
			prix  = types.InlineKeyboardButton(text = "Developer", url = 'https://t.me/MMPMMMM')
			mnm = types.InlineKeyboardMarkup()
			mnm.row_width = 1
			mnm.add(prix)
			bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"WaiT For HunT MY FrienD\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nin User : {us}\nEmail : {email}\nUnavailable : {Un}\nAvailable : {An}\nCheck : {ch}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nBY : @MMPMMMM"),parse_mode='markdown',reply_markup=mnm)		


def getcheck21(message):
	An = 0
	Un = 0
	ch = 0
	Fal = 0
	z = 0
	user = '1q2w3e4rt5yu6io7paos8dfogh9jk0lzxcvbbnm'
	for im in range(5000):
		us = str(''.join((random.choice(user) for i in range(6))))
		email = us+'@hotmail.com'
		url = f"https://check.moahmedsalah.repl.co/api-v1/check-email/tiktok/?email={email}"
		req = requests.get(url).text
		print(req)
		if 'False' in req:
			Fal+=1
			print(f"Email Not Linked Tik Tok\n{email}\n\n")
		if "True" in req:
			print(f"Email Available Linked Tik Tok\n{email}\n\n")
			url = f"https://signup.live.com/signup?username={email}"
			headers = {
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US;q=0.9,en;q=0.8",
"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "Windows",
"sec-fetch-dest": "document",
"sec-fetch-mode": "navigate",
"sec-fetch-site": "none",
"sec-fetch-user": "?1",
"upgrade-insecure-requests": "1",
"User-Agent": str(generate_user_agent()),
}
			data = {'username': str(email),}
			req = requests.post(url,
			headers=headers, data=data).text
			if '"isAvailable":1' in req:
			 An+=1
			 print(f"Available   :   {email}")
			 mol = (f"""Email Availabla\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nEmail : {email}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nTele : @MMPMMMM""")
			 print(mol)
			 url = f"https://alkabby4api.pythonanywhere.com/info/tiktok?user={us}"
			 ree = requests.get(url).json()
			 Name = str(ree['Name'])
			 Followers = str(ree['Followers'])
			 Following = str(ree['Following'])
			 Likes = str(ree['Likes'])
			 bot.send_message(message.chat.id,f""" SuFi BoT New HuNteR
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
User : {us}
Name : {Name}
Followers : {Followers}
Following : {Following}
Likes : {Likes}
Email : {email}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
Tele : @MMPMMMM""")
			 
			else:
				Un+=1
				print("ليس متاح")
				z+=1
		else:
			ch+=1
			prix  = types.InlineKeyboardButton(text = "Developer", url = 'https://t.me/MMPMMMM')
			mnm = types.InlineKeyboardMarkup()
			mnm.row_width = 1
			mnm.add(prix)
			bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"WaiT For HunT MY FrienD\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nin User : {us}\nEmail : {email}\nUnavailable : {Un}\nAvailable : {An}\nCheck : {ch}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nBY : @MMPMMMM"),parse_mode='markdown',reply_markup=mnm)

def getcheck11(message):
	An = 0
	Un = 0
	ch = 0
	Fal = 0
	z = 0
	user = '1q2w3e4rt5yu6io7paos8dfogh9jk0lzxcvbbnm'
	for im in range(5000):
		us = str(''.join((random.choice(user) for i in range(5))))
		email = us+'@hotmail.com'
		url = f"https://check.moahmedsalah.repl.co/api-v1/check-email/tiktok/?email={email}"
		req = requests.get(url).text
		print(req)
		if 'False' in req:
			Fal+=1
			print(f"Email Not Linked Tik Tok\n{email}\n\n")
		if "True" in req:
			print(f"Email Available Linked Tik Tok\n{email}\n\n")
			url = f"https://signup.live.com/signup?username={email}"
			headers = {
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US;q=0.9,en;q=0.8",
"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "Windows",
"sec-fetch-dest": "document",
"sec-fetch-mode": "navigate",
"sec-fetch-site": "none",
"sec-fetch-user": "?1",
"upgrade-insecure-requests": "1",
"User-Agent": str(generate_user_agent()),
}
			data = {'username': str(email),}
			req = requests.post(url,
			headers=headers, data=data).text
			if '"isAvailable":1' in req:
			 An+=1
			 print(f"Available   :   {email}")
			 mol = (f"""Email Availabla\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nEmail : {email}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nTele : @MMPMMMM""")
			 print(mol)
			 url = f"https://alkabby4api.pythonanywhere.com/info/tiktok?user={us}"
			 ree = requests.get(url).json()
			 Name = str(ree['Name'])
			 Followers = str(ree['Followers'])
			 Following = str(ree['Following'])
			 Likes = str(ree['Likes'])
			 bot.send_message(message.chat.id,f""" SuFi BoT New HuNteR
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
User : {us}
Name : {Name}
Followers : {Followers}
Following : {Following}
Likes : {Likes}
Email : {email}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
Tele : @MMPMMMM""")
			else:
				Un+=1
				print("ليس متاح")
				z+=1
		else:
			ch+=1
			prix  = types.InlineKeyboardButton(text = "Developer", url = 'https://t.me/MMPMMMM')
			mnm = types.InlineKeyboardMarkup()
			mnm.row_width = 1
			mnm.add(prix)
			bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"WaiT For HunT MY FrienD\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nin User {us}\nEmail : {email}\nUnavailable : {Un}\nAvailable : {An}\nCheck : {ch}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nBY : @MMPMMMM"),parse_mode='markdown',reply_markup=mnm)		
			
def getcheck1(message):
	An = 0
	Un = 0
	ch = 0
	Fal = 0
	z = 0
	user = '1q2w3e4rt5yu6io7paos8dfogh9jk0lzxcvbbnm'
	for im in range(5000):
		us = str(''.join((random.choice(user) for i in range(4))))
		email = us+'@hotmail.com'
		url = f"https://check.moahmedsalah.repl.co/api-v1/check-email/tiktok/?email={email}"
		req = requests.get(url).text
		print(req)
		if 'False' in req:
			Fal+=1
			print(f"Email Not Linked Tik Tok\n{email}\n\n")
		if "True" in req:
			print(f"Email Available Linked Tik Tok\n{email}\n\n")
			url = f"https://signup.live.com/signup?username={email}"
			headers = {
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US;q=0.9,en;q=0.8",
"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "Windows",
"sec-fetch-dest": "document",
"sec-fetch-mode": "navigate",
"sec-fetch-site": "none",
"sec-fetch-user": "?1",
"upgrade-insecure-requests": "1",
"User-Agent": str(generate_user_agent()),
}
			data = {'username': str(email),}
			req = requests.post(url,
			headers=headers, data=data).text
			if '"isAvailable":1' in req:
			 An+=1
			 print(f"Available   :   {email}")
			 mol = (f"""Email Availabla\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nEmail : {email}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nTele : @MMPMMMM""")
			 print(mol)
			 url = f"https://alkabby4api.pythonanywhere.com/info/tiktok?user={us}"
			 ree = requests.get(url).json()
			 Name = str(ree['Name'])
			 Followers = str(ree['Followers'])
			 Following = str(ree['Following'])
			 Likes = str(ree['Likes'])
			 bot.send_message(message.chat.id,f""" SuFi BoT New HuNteR
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
User : {us}
Name : {Name}
Followers : {Followers}
Following : {Following}
Likes : {Likes}
Email : {email}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
Tele : @MMPMMMM""")

			else:
				Un+=1
				print("ليس متاح")
				z+=1
		else:
			ch+=1
			prix  = types.InlineKeyboardButton(text = "Developer", url = 'https://t.me/MMPMMMM')
			mnm = types.InlineKeyboardMarkup()
			mnm.row_width = 1
			mnm.add(prix)
			bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=(f"WaiT For HunT MY FrienD\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nin User : {us}\nEmail : {email}\nUnavailable : {Un}\nAvailable : {An}\nCheck : {ch}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nBY : @MMPMMMM"),parse_mode='markdown',reply_markup=mnm)		

def check10(message):
	getc  = types.InlineKeyboardButton(text = "4 LeTTerS", callback_data = 'getmy1')
	get1x  = types.InlineKeyboardButton(text = "5 LeTTerS", callback_data = 'getmy11')
	get2s  = types.InlineKeyboardButton(text = "6 LeTTerS", callback_data = 'getmy21')
	get3l  = types.InlineKeyboardButton(text = "7 LeTTerS", callback_data = 'getmy31')
	gemfy10 = types.InlineKeyboardMarkup()
	gemfy10.row_width = 2
	gemfy10.add(getc,get1x,get2s,get3l)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="ChOOsE DeaR",parse_mode='markdown',reply_markup=gemfy10)

def chek1(message):
	getc  = types.InlineKeyboardButton(text = "4 LeTTerS", callback_data = 'm1')
	get1x  = types.InlineKeyboardButton(text = "5 LeTTerS", callback_data = 'm2')
	get2s  = types.InlineKeyboardButton(text = "6 LeTTerS", callback_data = 'm3')
	get3l  = types.InlineKeyboardButton(text = "7 LeTTerS", callback_data = 'm4')
	gemfy10 = types.InlineKeyboardMarkup()
	gemfy10.row_width = 2
	gemfy10.add(getc,get1x,get2s,get3l)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="ChOOsE DeaR",parse_mode='markdown',reply_markup=gemfy10)
	
def cherk1(message):
	getc  = types.InlineKeyboardButton(text = "4 LeTTerS", callback_data = 'r1')
	get1x  = types.InlineKeyboardButton(text = "5 LeTTerS", callback_data = 'r2')
	get2s  = types.InlineKeyboardButton(text = "6 LeTTerS", callback_data = 'r3')
	get3l  = types.InlineKeyboardButton(text = "7 LeTTerS", callback_data = 'r4')
	gemfy10 = types.InlineKeyboardMarkup()
	gemfy10.row_width = 2
	gemfy10.add(getc,get1x,get2s,get3l)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="ChOOsE DeaR",parse_mode='markdown',reply_markup=gemfy10)
	
def out1(message):
	getc  = types.InlineKeyboardButton(text = "4 LeTTerS", callback_data = 'o1')
	get1x  = types.InlineKeyboardButton(text = "5 LeTTerS", callback_data = 'o2')
	get2s  = types.InlineKeyboardButton(text = "6 LeTTerS", callback_data = 'o3')
	get3l  = types.InlineKeyboardButton(text = "7 LeTTerS", callback_data = 'o4')
	gemfy10 = types.InlineKeyboardMarkup()
	gemfy10.row_width = 2
	gemfy10.add(getc,get1x,get2s,get3l)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="ChOOsE DeaR",parse_mode='markdown',reply_markup=gemfy10)
	
def caol(message):
	getc  = types.InlineKeyboardButton(text = "4 LeTTerS", callback_data = 'a1')
	get1x  = types.InlineKeyboardButton(text = "5 LeTTerS", callback_data = 'a2')
	get2s  = types.InlineKeyboardButton(text = "6 LeTTerS", callback_data = 'a3')
	get3l  = types.InlineKeyboardButton(text = "7 LeTTerS", callback_data = 'a4')
	gemfy10 = types.InlineKeyboardMarkup()
	gemfy10.row_width = 2
	gemfy10.add(getc,get1x,get2s,get3l)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="ChOOsE DeaR",parse_mode='markdown',reply_markup=gemfy10)

	
def check1(message):
	Yahoo  = types.InlineKeyboardButton(text = "Yahoo", callback_data = 'Yahoo')
	Hotmail  = types.InlineKeyboardButton(text = "HotMail", callback_data = 'hotmail')
	mailru  = types.InlineKeyboardButton(text = "MailRu", callback_data = 'mailru')
	outlook = types.InlineKeyboardButton(text = "OutlooK", callback_data = 'outlook')
	aol = types.InlineKeyboardButton(text = "Aol", callback_data = 'aol')
	gemfy1 = types.InlineKeyboardMarkup()
	gemfy1.row_width = 2
	gemfy1.add(Yahoo,aol,Hotmail,outlook,mailru)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="ChOOsE EmaiL DeaR",parse_mode='markdown',reply_markup=gemfy1)
	
@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://new-boto.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    
bot.polling()
