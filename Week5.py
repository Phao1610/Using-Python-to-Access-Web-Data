# import xml.etree.ElementTree as ET
# data = '''<person>
# 	<name>Toan Phao</name>
# 	<phone type = "intl">
# 		+1 734 303 4456
# 	</phone>
# 	<email hide="No nha"/>
# </person>'''

# tree = ET.fromstring(data)
# print('Name:',tree.find('name').text)
# print('Attr:',tree.find('email').get('hide'))

import xml.etree.ElementTree as ET
input = '''<stuff>
	<users>
		<user x="2">
			<id>001</id>
			<name>Toan Phao</name>
		</user>
		<user x="7">
			<id>009</id>
			<name>Truc</name>
		</user>
	</users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
	print('Name',item.find('name').text)
	print('Id',item.find('id').text)
	print('Attribute', item.get("x"))
