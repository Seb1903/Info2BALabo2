import re
tel = input("numéro de téléphone : ")
canvas =  r'\+[0-9]{2}\s[0-9]{3}\s[0-9]{2}\s[0-9]{2}\s[0-9]{2}'
c = re.compile(canvas)
print(c.match(tel) is not None)



entier = r'\+?[1-9][0-9]*'
entieri = input('votre entier : ')
e = re.compile(entier)
print(e.match(entieri) is not None)





