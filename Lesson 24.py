import re
phonenumregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phonenumregex.search ('My number is 415-555-4242')
