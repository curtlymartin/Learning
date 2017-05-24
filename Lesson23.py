import re

message = 'Call me on 415-555-1011 tomorrow'

phonenumregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
mo=phonenumregex.search(message)
print (mo.group())