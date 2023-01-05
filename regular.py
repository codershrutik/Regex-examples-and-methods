import re

nameage = """Janice is 22 and Theo is 31
Gabriel is 44 and Joey is 21"""
ages = re.findall(r'\d{1,3}',nameage)
names = re.findall(r'[A-Z][a-z]*',nameage)
print(ages)
print(names)

agedict = {}
x=0

for eachname in names:
    agedict[eachname] = ages[x]
    x+=1

print(agedict)