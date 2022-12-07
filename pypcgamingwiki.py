import urllib.request
import requests
import json
import os
import sys


class Browser:
	def __init__(self, game):
		self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
		self.game = game
  
		#https://www.pcgamingwiki.com/w/api.php?action=parse&page=Elden_Ring&prop=wikitext&format=json

	def search(self):
		url = ("https://www.pcgamingwiki.com/w/api.php?action=query&list=search&srsearch={}&format=json".format(self.game))
		
		val = requests.get(url, headers=self.headers).text
		j = json.loads(val)
		val = j['query']['search'][0]['title']
		# j = json.loads(val)
		# print(j[3][0])		
		return val

	def parse(self, page):
		url = 'https://www.pcgamingwiki.com/w/api.php?action=parse&page={}&prop=wikitext&format=json'.format(str(page))
			
		val = requests.get(url, headers=self.headers, stream=True, allow_redirects=True).text
		j = json.loads(val) 
		val = (j['parse']['wikitext']['*'])
		val = val.split('|')
		try:
			os.remove("output.txt")
		except:
			pass
		with open('output.txt', "a") as f:
			for i in val:
				try: 
					x = i.split('=')
					k = x[0].strip(' ')
					v = x[1].strip(' ')
					if v != '\n':
						f.write(f'{k}=={v}' + '\n') 
				except:
					pass
				
			
	def pagedata(self):
		
		url = "https://steamdb.info/app/1534900/"
		val = requests.get(url, headers=self.headers, stream=True, allow_redirects=True).text
		with open('output.txt', "w") as f:
			f.write(val)

# x = input("Enter game name: ")
# G = Browser(x)
print(sys.argv[1])
G = Browser(sys.argv[1])
page = G.search()
G.parse(page)

#dirname = os.path.dirname(__file__)
#os.system(f'\"{dirname}\\output.txt\"')

#G.pagedata()

