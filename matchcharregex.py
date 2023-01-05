import re

randstr = '''keep the blue
 flag flying high 
 chelsea'''
print(randstr)

regex = re.compile("\n")
randstr = regex.sub("",randstr)
print(randstr)

rand = "12345str"
print("Matches: ",len(re.findall("\d",rand)))
print("Matches: ",len(re.findall("\D",rand)))
print("Matches: ",len(re.findall("\d{5}",rand)))

num = "123 1234 12345 123456 1234567"
print("Matches: ",len(re.findall("\d{5,7}",rand)))