# # conditionals

# # operators

# # 1)comparison  operator
# # 2)logical operator

# # < , > , == , !=  <= , >=
# # entity < entity  ==================> boolean
# # <  ==> less than
# # >  ==> greate than
# # <=  ==> less than or equal to
# # >=  ==> greater then or equal to
# # ==  ==> equal tham
# # !=  ==> not equal

# from subprocess import CREATE_NEW_CONSOLE


# a = 10
# b = 10
# print(a>b)

# print(10 > 11)
# print(10 < 11)
# print(10 <= 11)
# print(10 >= 11)
# print(10 != 10)
# print(10 != 12)

# # and
# print('-----------------------------')
# print(10 > 10 and 10 == 10)
# print(10 == 10 and 10 == 10)
# print(100 < 200 and 300 > 100)
# print(100 > 200 and 300 < 100)
# print(100 <= 200 and 300 >= 100)
# print(100 == 100 and 300 != 100)
# print(100 == 100 and 300 != 300)

# # or
# print('--------------------------------')
# print(10 > 10 or 10 == 10) # true
# print(10 == 10 or 10 == 10) # true
# print(100 < 200 or 300 > 100) # true
# print(100 > 200 or 300 < 100) # false
# print(100 <= 200 or 300 >= 100) # true
# print(100 == 100 or 300 != 100) #true
# print(100 == 100 or 300 != 300) # true


# if()




from pdb import post_mortem


tickets = 7

# if(tickets > 0 and tickets <= 5):
#     print(' 5 % discount ')

# if(tickets > 5 and tickets <= 10):
#     print(' 10 % discount ')

# if(tickets > 10):
#     print('20 % discount ')

if(tickets > 0 and tickets <= 5):
    print(' 5 % discount ')

elif(tickets > 5 and tickets <= 10):
    print(' 10 % discount ')

elif(tickets > 10):
    print('20 % discount ')

# 
marks = 98

# if(marks > 90):
#     print('grade A')
# if(marks > 75):
#     print('grade B')
# if(marks > 65):
#     print('grade c')      
# 
if(marks > 90):
    print('grade A')
elif(marks > 75):
    print('grade B')
elif(marks > 65):
    print('grade c')     
