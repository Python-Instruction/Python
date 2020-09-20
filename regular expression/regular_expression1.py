

import re 
txt = "That will be 59 dollars"
# Find all digit characters:
x1 = re.findall("\d", txt)
print(x1)
# Search for a sequence that starts with "w", 
# followed by two (any) characters, and an "l":
x2 = re.findall("w..l", txt)
print(x2)
# A set of characters
x3 = re.findall("[a-m]", txt)
print(x3)
# start with
x4 = re.findall("^That", txt)
print(x4)
# Ends with
x5 = re.findall("dollars$", txt)
print(x5)

# Check if the string contains "wi"
# followed by 0 or more "l" characters:
x6 = re.findall("wil*", txt)
print(x6)
# Check if the string contains "wi"
# followed by one or more "l" characters:
x7 = re.findall("wil+", txt)
print(x7)
# Check if the string contains "wi"
# followed by exactly two "l" characters:
x8 = re.findall("wil{2}", txt)
print(x8)
#Either or
x9 = re.findall("That|that", txt)
print(x9)




