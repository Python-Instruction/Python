

import re 
txt = "That will be 59 dollars"
#Split at each white-space character
x1 = re.split("\s", txt)
print(x1)
#Split the string only at the first occurrence
x2 = re.split("\s", txt, 1)
print(x2)

