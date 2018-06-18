#!/usr/bin/python
import json
import sys
import requests
import re

apiurl = "https://stat.ripe.net/data/looking-glass/data.json?resource="
as_paths={}
prefix={}
origin={}

def GetDataFromApi(prefix):
	url = apiurl + prefix
	r = requests.get(url)
	output = json.loads(r.content)
	return output

def GetPrefix(data):
	for i in data['data']['rrcs']:
		for j in i['peers']:
			if j['prefix'] in prefix:
				prefix [j['prefix']] += 1
			else:
				prefix [j['prefix']] = 1
	for p in prefix:
		key = p
	return p

def GetOrigin(data):
	for i in data['data']['rrcs']:
		for j in i['peers']:
			origin_as = j['asn_origin']
			if origin_as in origin:
				origin [origin_as] += 1
			else:
				origin [origin_as] = 1
	for o in origin:
		key = o
	return key

def GetAS(data, OriginAS ):
	for i in data['data']['rrcs']:
		for j in i['peers']:
			a = j['as_path'].split(' ');
			curidx =  a.index(unicode.encode(str(OriginAS).decode("utf-8")));
			p = a[curidx-2] + ' ' + a[curidx-1] + ' ' + a[curidx]
			if p in as_paths:
				as_paths [p] += 1
			else:
				as_paths [p] = 1
	return as_paths

# Main

if len(sys.argv) < 2:
	print 'Syntax error. E.g: ' + sys.argv[0] + ' <PREFIX>' + ' <AS>'
	sys.exit()

route = sys.argv[1]
json_content = GetDataFromApi(route)
prefix = GetPrefix(json_content)
origin = GetOrigin(json_content)
as_paths = GetAS(json_content, origin )

for i in as_paths:
	print "as path tail: " + i
