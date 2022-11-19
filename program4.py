
#  program 1
# x = 1 
# while x <= 10:
#     print(x)
#     x = x+1

#  program 1
from tkinter import PIESLICE


x = 10 
while x >= 0:
    print(x)
    x = x-1

# program 3
y = 2 
while(y <= 20):
    print(y)
    y = y + 2

# program 5 - break statement
# a = 1 
# while(a<=6):
#     print(a)
#     if(a==4):
#         break 
#     a = a+1

# program 6
a = 1 
while(a<=6):
    if(a==4):
        break 
    print(a)
    a = a+1 

# program 7
# m = 10
# while(m >= 1):
#     print(m)
#     if(m == 5):
#         break
#     m = m-1

# program 8
m = 10
while(m >= 1):
    if(m == 5):
        break
    print(m)
    m = m-1

# program 9 - continue statement
print('----------------------------------')



j = 1
while(j <=5):
    if(j == 3):
        j = j + 1 #4
        continue
    print(j)  # 1 #2 # 4 #5
    j = j + 1  # 2 #3 # 5 # 5


# s = 1
# while(s <= 6):
#     if(s == 3):
#         s = s + 1
#         continue
#     print(s) 




# for loop
names = ['pooja','sonali','aishwarya','monika']
# for item in names:
#     print(item)

for m in range(len(names)):
    print(m)
    print(names[m])


   
    

