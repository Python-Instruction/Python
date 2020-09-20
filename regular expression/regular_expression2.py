import re 
txt = "That will be 59 dollars"
# start with
x1 = re.search("^That", txt)
print(x1)
# Ends with
x2 = re.search("dollars$", txt)
print(x2)
# Search for the first white-space 
# character in the string
x3 = re.search("\s", txt)
print("The first white-space", x3.start())
#Either or
x4 = re.search("That|that", txt)
print(x4)
# Print a list of all matches
x5 = re.search("wi", txt)
print(x5)
# Return an empty list if no match was found
x6 = re.search("sun", txt)
print(x6)