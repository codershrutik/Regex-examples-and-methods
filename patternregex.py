#match words with a particular pattern
import re
str1 = "sat,hat,map,pat,wet,get,mat,cat,spat,fat"
allstr = re.findall("[shmp]at",str1)
for i in allstr:
    print(i)