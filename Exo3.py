import re 
import sys 

link = sys.argv[1]
pattern = r'(?P<protocol>[^./:]+)://(?P<domain>[^/]+)(?:/(?P<path>.*))?'
p = re.compile(pattern)
result = p.match(link)

groups = ['protocol', 'domain', 'path']

for group in groups : 
    if(result.group(group) is not None) :
        print("{} : {}".format(group.capitalize(),result.group(group)))
