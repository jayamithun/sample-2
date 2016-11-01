import json
from time import sleep
import requests

def match():
	d = {}
	count = 1
	template1 = "http://cricapi.com/api/cricket"
	data = requests.get(template1)
	js = data.json()
	if js['cache']:
		for i in js['data']:
			d[count] = [i["unique_id"],i['description']]
			count += 1
	return d

def details(y):
	template2 = "http://cricapi.com/api/cricketScore?unique_id="
	url = template2 + str(y)
	data = requests.get(url)
	js = data.json()
	print()
	if js['cache']:
		print(js['team-1'],"Vs",js['team-2'])
		print(js['score'])
		print(js['innings-requirement'])
	print()

x = match()
print("No.of Ongoing Matches:",len(x))
sleep(2)
print()
for k,i in enumerate(x,start=1):
	print(k,".",x[i][1])
	sleep(0.5)
print()

while True:
	try:
		select = input("Enter the S.No corresponding the match: ")
		if select.strip() == 'q':
			break
		details(x[int(select)][0])
	except:
		print("Invalid input!")