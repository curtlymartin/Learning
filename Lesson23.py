def isnumcheck(text):  #415-555-
    if len(text) != 12:
        return False #not proper size
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False#no area code
    if text[3] != '-':
        return False #no dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False #no first 3 digits
    if text[7] != '-':
        return False #no second dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False #missing last 4 digits
    return True

<<<<<<< HEAD
message = 'Call me on 415-555-1011 tomorrow'

phonenumregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
mo=phonenumregex.search(message)
print (mo.group())

print('fjkvkd')

=======
print(isnumcheck('415-555-5554'))
>>>>>>> parent of f388fe9... regex example
