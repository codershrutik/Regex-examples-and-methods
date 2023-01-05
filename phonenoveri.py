import re

phn = "444-333-4567"

if re.search("\w{3}-\w{3}-\w{4}",phn):
    print("It is an authentic phone number")