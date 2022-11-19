# # positional arguments

# def cityState(city,state):
#     print(city)
#     print(state)
# # cityState('mh','mumbai')    
# cityState(state='mh',city='mumbai')

# # # Default arguments 

# def sum(a=10,b=20):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)
#     print(a%b)
# sum()   
# sum(30,40)    


# # # variable length arguments 

# # number of arguments know
# def num(s,t,p):
#     print(s+t+p)
# num(20,20,20)   

# number of arguments not know

def sumA(*args):
    # print(args)
    sum = 0
    for i in args:
        sum += i
    return sum
a1 = sumA(22,33,44,55,66,77)    
print(a1)

def sumB(h,j,*args):
    print(h)
    print(j)
    print(args)
    print(type(args))
sumB(11,22,33,44,55,66,77)


# keyword variable length argument

def person(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, val in kwargs.items():
        print(key,val)
person(firstName="pratiksha",Lastname="kharade",age=24)    



