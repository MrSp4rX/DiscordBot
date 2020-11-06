#my user id = 603535335049265153

import scrap
import discord
import datetime
import wikipedia
import random

token = 'NzYxOTUwNzkxMDQwMTA2NTc2.X3iD-A.JxMCMvgYW_YUOk3TEpY_8m8d7cc'
abuse = ['bhosadike','madarchod','bsdk', 'bhsdk', 'betichod', 'chod', 'lund', 'gand ', 'jerk', 'lode', 'loda', 'madarchod', 'mdrchod', 'madar', 'chut', 'bc', 'mkchut', 'mc','mkc','lund','jhat','suwar','kutte','randi','bhosadi','m4drch0d','m4d4rch0d','mdrch0d','b#05adik3','bh05adik3','bh0sadike','bh0sad!ke','bho5adike','bh0sadike','bh0sad!ke','ch0d','m4d4rch0d','land','m@d@rc#0d','m@d@rch0d','m@d@rchod','l4nd','.bhosadike','.madarchod','.bsdk', '.bhsdk', '.betichod', '.chod', '.lund', '.gand ', '.jerk', '.lode', '.loda', '.madarchod', '.mdrchod', '.madar', '.chut', '.bc', '.mkchut', '.mc','.mkc','.lund','.jhat','.suwar','.kutte','.randi','.bhosadi','.m4drch0d','.m4d4rch0d','.mdrch0d','.b#05adik3','.bh05adik3','.bh0sadike','.bh0sad!ke','.bho5adike','.bh0sadike','.bh0sad!ke','.ch0d','.m4d4rch0d','.land','.m@d@rc#0d','.m@d@rch0d','.m@d@rchod','.l4nd','bhosadike.','madarchod.','bsdk.', 'bhsdk.', 'betichod.', 'chod.', 'lund.', 'gand ', 'jerk.', 'lode.', 'loda.', 'madarchod.', 'mdrchod.', 'madar.', 'chut.', 'bc.', 'mkchut.', 'mc.','mkc.','lund.','jhat.','suwar.','kutte.','randi.','bhosadi.','m4drch0d.','m4d4rch0d.','mdrch0d.','b#05adik3.','bh05adik3.','bh0sadike.','bh0sad!ke.','bho5adike.','bh0sadike.','bh0sad!ke.','ch0d.','m4d4rch0d.','land.','m@d@rc#0d.','m@d@rch0d.','m@d@rchod.','l4nd.']

abuse_reply = [
	'Bhosadi ke aisa thappad marunga tere muh ke dant gad se hoker girenge.',
	'Jija se bkchodi krta hai maderchod tamiz sikh lowde.',
	'Gand mei tere salayi ghusa ke swetter bna dunga.',
	'Jhant khayega mera behen ke lowda.',
	'Teri ammy ka asiq hun wo v khufiya asiq ati hai mujhse chummiya lene apne chut pe.',
	'Teri ammy ke gand ko mukka marke tod dunga maderchod baap se bakchodi',
	'Bhagg maderchod teri ammy toh nukkad ki randi hai re.',
	'300 rs wali randi ke aulad.',
	'Teri behn ko utha ke salwar ke sath hi pelunga.',
	'Hahahaha gandu tera baal pakad ke diwal se lada lada ke tera seer phod ke teri ammy ka mang bharunga',
	'Madarchod Zuban pe conrol karo warna gand faad denge',
	'Your Dady can only Abuse Samjha  Bhosadike'
]

global user
class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged on as', self.user)

	async def on_message(self, message):
		if message.author == self.user:
			return
		string = message.content
		if string != "":
			user = message.author.mention
			for word in abuse:
				userid = str(message.author.id)
				if word in string.lower() and userid != '603535335049265153' and userid != '598099871928680459':
					await message.channel.send(user+' '+str(random.choice(abuse_reply)))
					break
				else:
					pass
		if string.startswith('.'):
			if '.help' in string:
				await message.channel.send('''
Help is Here:
1. Use `.help` to see this  Message.
2. Use `.wikipedia text`  to Search anything on Wikipedia.
3. Use `.bot` to see Introduction of this Bot.
4. Use `.stylish` to Convert Normal text to Stylish Text.
5. Don't Abuse otherwise You have to pay for it.
6. Use `.ping` to See if bot is Replying or not.
7. Use `.image text` to see a Picture of your Category.

						Creator: Mr. SparX
''')
			if '.ping' in string:
				user = message.author.mention
				await message.channel.send(user+' Pong')
			elif '.stylish' in string:
				string =  string.replace('.stylish','')
				s = string.lower()
				s = s.replace('a','4',)
				s = s.replace('b','8',)
				s = s.replace('c','¢',)
				s = s.replace('e','3',)
				s = s.replace('g','9',)
				s = s.replace('h','#',)
				s = s.replace('i','!',)
				s = s.replace('j','√',)
				s = s.replace('o','0',)
				s = s.replace('p','9',)
				s = s.replace('r','®',)
				s = s.replace('s','5',)
				s = s.replace('t','7',)
				s = s.replace('v','√',)
				s = s.replace('y','¥',)
				s = s.replace('l','L')
				await message.channel.send(user+' Your Stylish Name is:\n\n'+s)
			elif '.image'  in string:
				string = string.replace('.image ','')
				# result = scrap.main(string)
				await message.channel.send(scrap.main(string))
			elif string == ".bot":
				hour = datetime.datetime.now().hour
				minute = datetime.datetime.now().minute
				day = datetime.datetime.now().strftime("%A")
				await message.channel.send("Hello :)\nThis is a Bot which is Created and Operated by Mr. SparX.\nDon't get confused with my name because I am a Big Bhosadiwala and my Creator is Bhut hard wala Harami.\nUse  `.help`  to Know More Commands.\nThank You!!!\nCurrent Time: "+str(hour)+":"+str(minute)+"\nCurrent Day: "+str(day)+"\n")
			elif ".wikipedia" in string:
				query = string.replace(".wikipedia", "")
				try:
					result = wikipedia.summary(query, sentences=2)
					await message.channel.send("According to Wikipedia:\n"+result)
					query = query.capitalize()
				except:
					query = query.capitalize()
					await message.channel.send(user+' I am sorry but I could not find Anything Over Wikipedia about '+query+'...  :pleading_face: ')
			else:
				pass
client = MyClient()
client.run(token)
