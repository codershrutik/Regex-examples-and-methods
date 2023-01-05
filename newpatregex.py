import re

#match series of range of characters
str1 = "sat,hat,map,pat,wet,get,mat,cat,fat"
allstr = re.findall("[^h-z]at",str1)
for i in allstr:
    print(i)