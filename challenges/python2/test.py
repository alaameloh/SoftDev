import datetime
import pickle

tmp = "Listen, I was written on 1 Oct 18. How many days ago was it?"
import re
p = re.compile('[0-9]+ [a-zA-Z]{3} [0-9]+')
print(p.search(tmp).group())