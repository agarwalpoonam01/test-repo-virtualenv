import requests
from requests.exceptions import Timeout
from flask import json
print("Making First Request")
def myrequests():
	i = 40
	url_o = "http://localhost:8000/server-speed?test="
	while i > 0:
		try:
			url_t = url_o + str(i)
			resp = requests.post(url = url_t)
			print(resp)
		except Timeout as ex:
			print(json.dumps({'success':False}), 408, {'ContentType':'application/json'})
		print("Making Second Request")
		i = i - 1
myrequests()