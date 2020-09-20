

import re 
txt = "That will be 59 dollars"
# Replace every white-space character
# with &   
print(re.sub("\s", "&", txt))

# dollars will replace with rupees. 
print(re.sub('dollars', 'rupees' , txt))