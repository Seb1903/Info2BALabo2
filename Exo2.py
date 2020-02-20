import sys 
#print('hello', sysargv[1])python Exo2.py Nombres.txt
with open(sys.argv[1]) as f : 
    texte = f.readlines()
    print(texte)
    















 # Question 2 explications
# En tapant python file.py dans le terminal, on peut lancer le fichier (et ses fonctions)
# importer sys 
# print('hello', sysargv[1]), sysargv représente les arguments de ce que l'on lance dans le terminal(file.py par ex)