import re

# search()
str1 = "qas man sun mop run"
a1 = re.search(r'm\w\w',str1)
print(a1.group())

# findall()
str2 = "qas man sun mop run"
a2 = re.findall(r'm\w\w',str2)
print(a2)

# match()
str3 = "man qas sun mop run"
a3 = re.match(r'm\w\w',str3)
print(a3.group())

# sub()
str4 = "i am learning javascript"
a4 = re.sub(r'javascript','python',str4)
print(a4)

# split()
str5 = "i :am, learning @javascript"
a5 = re.split(r'\W+',str5)
print(a5)

# 



