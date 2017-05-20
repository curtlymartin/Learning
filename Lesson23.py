def isphonenumber(text):#415-555-
    if len(text) !=12:
        return False #not proper size
    for I in range(0,3):
        if not text[I].isdecimal():
            return False#no dash
    for I in range (4,7):
        if not text[I].isdecimal():
            return False #no first 3 digits
    