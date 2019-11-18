#   import re - regular expressions module
import re
#   Counter
from collections import Counter
#   re-pattern, it't what we're searching
pattern = r'\w+'
#   list for results
all_results = []
miss_results = []

#   find requests
with open('urls.txt', 'r') as file:
    for row in file:
        name = re.findall( pattern, row )
        if len(name) > 0:
            all_results.append( name[0] )
        else:
            miss_results.append( name )

print(all_results)
print('пропуски', miss_results)
sort_all_results = Counter( all_results ).most_common() #   sort
for i in sort_all_results:
    print(i)
# print(sort_all_results)
print(len(all_results))
