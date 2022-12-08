import requests
import json
import os


class Browser:
	def __init__(self, game, path):
		self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
		self.game = game
		self.path = ('{}\\output.txt').format(path)
		print(self.path)

		#https://www.pcgamingwiki.com/w/api.php?action=parse&page=Elden_Ring&prop=wikitext&format=json

	def search(self):
		url = ("https://www.pcgamingwiki.com/w/api.php?action=query&list=search&srsearch={}&format=json".format(self.game))
		
		val = requests.get(url, headers=self.headers, stream=True, allow_redirects=True).text
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
		return val

	def write(self, val):
		try:
			os.remove(self.path)
		except:
			pass
		pagedata = {}
		with open(self.path, "w+") as f:
			for i in val:
				try: 
					x = i.split('=')
					k = x[0].strip()
					v = x[1].strip()
					k = k.replace(' ', '_')
					v = v.replace(' ', '_')
					if (v != '\n') and (v != '\n\n') and (v != '\n\n\n') and (v != ''):
						f.write(f'{k}=={v}\n\n\n') 
						pagedata[k] = v
				except:
					pass
		print(pagedata['direct3d_versions'])
		return pagedata
				


