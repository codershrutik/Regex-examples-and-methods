#find a word in a string
import re

if re.search("inform","we need to inform him with the latest information"):
    print("the word is present")

allinform = re.findall("inform","we need to inform him with the latest information")
for i in allinform:
    print(i)