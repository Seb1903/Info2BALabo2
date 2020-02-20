# Question 2 explications
# En tapant python file.py dans le terminal, on peut lancer le fichier (et ses fonctions)
# importer sys 
# print('hello', sysargv[1]), sysargv représente les arguments de ce que l'on lance dans le terminal(file.py par ex)

import sys 
#print('hello', sysargv[1])
with open(str(sys.argv[1]), 'r') as file : 
    texte = file.read()
    print(texte)
    print(sys.argv[1])