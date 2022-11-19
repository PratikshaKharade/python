# a = "hello"
# # print(a)

# # a1=a.count('a')
# # print(a1)

# # for i in range (len(a)):
# #     print(a[i])

# print(a[::-1])


q ='hello'
print(q)

#........................

q2 = 'hello'
print(q2[0])
print(q2[1])

# loops

name = "pratiksha"
for char in name:
    print(char)

    for x in range(len(name)):
        print(name[x])

# slicing

city = 'sangamner'
# city = city[1:5]
# city = city[1:8]
city = city[-7:-1]
print(city)

# upper(), lower()
city1 = 'Aurangabad'
a1 = city1.upper()
a2 = city1.lower()
print(a1)
print(a2)

# isupper(), islower()
city3 = 'CHANDRAPUR'
a3 = city3.isupper()
a4 = city3.islower()
print(a3)
print(a4)

# capitalize
city4 = 'pune'
a5 = city4.capitalize()
print(a5)

#startwith()

city5 = 'mumbai'
a6 = city5.startswith('mum')
a7 = city5.startswith('bai')
print(a6)
print(a7)

#endswith()
city6 = 'wardha'
a8 = city6.endswith('dha')
a9 = city6.endswith('war')
print(a8)
print(a9)

# index(), count()
city7 = 'sangamner'
a10 = city7.index('g')
print(a10)
a11 = city7.count('a')
print(a11)


# replace()
messegae = 'i am learning javascript'
a12 = messegae.replace('javascript','python')
print(a12)

# 