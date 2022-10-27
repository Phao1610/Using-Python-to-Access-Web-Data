import json 
# data = '''{
# 	"name": "Toan Phao",
# 	"phone": {
# 		"type": "intl",
# 		"number" : "+1 734 303 4456"
# 	},
# 	"email" : {
# 		"hide" : "yes"
# 	}
# }'''
data = open('app.json',"r")
info = json.loads(data.read())

print('User count: ',len(info))
for item in info:
	print('Name',item['name'])
	print('Id', item['id'])
	print('Attribute', item['x'])
# info = json.loads(data)
# print('Name: ',info["name"])
# print('Hide: ',info["email"]["hide"])
# data = 'app.json'

# with open(data, 'r', encoding='utf-8') as f:
#     info = json.loads(data)
# 	print('Name: ',info["name"])
# 	print('Hide: ',info["email"]["hide"])