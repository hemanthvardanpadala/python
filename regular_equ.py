import re

name_age = str(" Hemanth age is 19 Yash age is 12 Vicky age is 46 ")

ages = re.findall(r'\d{1,3}', name_age)
names = re.findall(r'[A-Z][a-z]*', name_age)

allinfo = {}

x=0
print(names)
print(ages)

for eachname in names:

    allinfo[eachname] = ages[x]
    x+=1
    
print(allinfo)