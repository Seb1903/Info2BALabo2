import sys 
import re
#print('hello', sysargv[1])python Exo2.py Nombres.txt
nombre = r'\d+'
p = re.compile(nombre)
with open(sys.argv[1]) as f : 
    texte = f.readlines()
    for i in range(len(texte)) : 
        texte[i]



# prof :
with open(sys.argv[1]) as file : 
    for i, line in enumerate(file) :
        instances = p.findall(line)
        if len(instances) != 0 : 
            print('Line {}: {}'.format(i+1, ", ".join(instances)) )














 # Question 2 explications
# En tapant python file.py dans le terminal, on peut lancer le fichier (et ses fonctions)
# importer sys 
# print('hello', sysargv[1]), sysargv représente les arguments de ce que l'on lance dans le terminal(file.py par ex)