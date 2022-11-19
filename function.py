

# # x = 10
# # y = 20
# # print(x + y)
# # print(x - y)
# # print(x / y)
# # print(x % y)

# # a = 10
# # b = 20
# # print(a + b)
# # print(a - b)
# # print(a / b)
# # print(a % b)


# # # function

# # def calculator(p,q):
# #     print(p + q)
# #     print(p - q)
# #     print(p / q)
# #     print(p % q)
# # calculator(20,10)   

# # function without parameter and without returntype



# def sumA():
#     print(10 + 20)
# sumA() 
# sumA()
# sumA()
# sumA()   


# # function with parameter and without returntype

# def sumB(s,t):
#     print(s + t,"hello")
#     print(s + t)
#     print(s + t)
# sumB(30,40)
# sumB(30,10)
# sumB(100,400)
# sumB(10,40)    

# # function with parameter and with returntype

# def sumD(m,n):
#     return m + n
# b = sumD(500,400)
# print(b) 
# print(b+200) 
# print(b/20)  


# # # even or odd

# r = 200
# if(r % 2 == 0):
#     print('no. is even')
# else:
#     print('no. is odd')    

# aa = 9
# if(aa % 2 == 0):
#     print('no. is even')
# else:
#     print('no. is odd')      


# # 
# def even_odd(a1):
#     if(a1 % 2 == 0):
#         print('no id even')
#     else:
#         print('no.is odd') 
# even_odd(300)
# even_odd(55)


# 
# def operations(a,b):
#     a1 = a + b
#     a2 = a - b
#     a3 = a / b
#     a4 = a * b
#     a5 = a % b
#     return a1
# b1 = operations(10,5)
# print(b1)    

# function return list

# def operations(a,b):
#     a1 = a + b
#     a2 = a - b
#     a3 = a / b
#     a4 = a * b
#     a5 = a % b
#     return [a1,a2,a3,a4,a5]
# b1 = operations(10,5)
# print(b1)  

# function return tuple
# def operations(a,b):
#     a1 = a + b
#     a2 = a - b
#     a3 = a / b
#     a4 = a * b
#     a5 = a % b
#     return (a1,a2,a3,a4,a5)
# b1 = operations(100,50)
# print(b1)  

# def operations(a,b):
#     a1 = a + b
#     a2 = a - b
#     a3 = a / b
#     a4 = a * b
#     a5 = a % b
#     return a1,a2,a3,a4,a5
# b1 = operations(100,50)
# print(b1)  

# # function return dict

# def operations(a,b):
#     a1 = a + b
#     a2 = a - b
#     a3 = a / b
#     a4 = a * b
#     a5 = a % b
#     return {
#         "a1": a1,
#         "a2": a2,
#         "a3": a3,
#         "a4": a4,
#         "a5": a5
#     }
# b1 = operations(100,50)
# print(b1)
# print(b1['a1'])
# print(type(b1))  
# b1["a6"] = 100
# print(b1)

# function return set
from unicodedata import name

from setuptools import sic


def operations(a,b):
    a1 = a + b
    a2 = a - b
    a3 = a / b
    a4 = a * b
    a5 = a % b
    return {a1,a2,a3,a4,a5}
b1 = operations(100,50)
print(b1)  

# number as a parameter and number as return type 

# s1 = 100
# s2 = 200
# def add(x,y):
#     print(x + y)
# add(s1,s2)

s1 = 100
s2 = 200
def add(x,y):
    return x + y
s3 = add(s1,s2)
print(s3)

# passing list as a parameter
names = ['aishwarya','monika','poonam','pratiksha'] 
def addname(a):
     a.append('pooja')
     print(a)
addname(names) 
print(names)  

# passing dict as a parameter

person={
    "FirstName":"pratiksha",
    "LastNAme":"Kharade",
    "Age":24
}
def addcity(city):
    city['city']="sangamner"
    print(city)
addcity(person)
print(person)    


# passing function as parameter to another funtion

def sub(a,b):
    return a - b
# print(sub)

def subA(s1,s2,fn):
    q1 = fn(s1,s2)
    print(q1)
subA(100,50,sub)    

