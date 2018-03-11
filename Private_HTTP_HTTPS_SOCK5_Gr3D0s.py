import urllib.request
import json
import time
import sys
print("Fuente: %s\nExtrayendo.." %(time.strftime("%m-%d-%Y")))
try:
	response = json.loads(urllib.request.urlopen('https://checkerproxy.net/api/archive/%s'%(time.strftime("%Y-%m-%d"))).read().decode())
except:
	sys.exit("Error: API connection failure")
proxies_http_https = [proxy['addr'] for proxy in response if proxy['type'] == 1 or proxy['type'] == 2 and proxy['kind'] == 2 and proxy['timeout'] <= 20000 and proxy['timeout'] >= 10000]
proxies_socks = [proxy['addr'] for proxy in response if proxy['type'] == 4 and proxy['kind'] == 2 and proxy['timeout'] <= 20000]
if not len(proxies_http_https) or not len(proxies_socks):
	sys.exit('Proxyset no a publicado aún, intentalo dentro de unas pocas horas.')
try:
	with open('Proxies/http_https_ssl_output.txt','wt') as f:
		for p in proxies_http_https:
			f.write(p + '\n')
	with open('Proxies/socks_ssl_output.txt','wt') as f:
		for p in proxies_socks:
			f.write(p + '\n')
except:
	e = input('Missing \'Proxies\' Folder!')
	sys.exit()
o = input("Éxito:Sacado por GreDos Proxies/http_https_ssl_output.txt || {} Anónimo   HTTP/S Proxies \nÉxito:Sacado por GreDos Proxies/socks_ssl_output.txt || {} Anónimo SOCK5  Proxies \nGracias por usar este scraper de GreDos \nPresiona 'Enter' para salir..".format(len(proxies_http_https), len(proxies_socks)))



