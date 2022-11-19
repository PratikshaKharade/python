# tuple

import numbers


a = (11,22,33,44,55)
print(a)
print(type(a))

a2 = ("snehal","shital",88,33)
print(a2)
print(a2[0])

# slicing
            # 0     1         2        3       4           5        
cities = ("pune","mumbai","wardha","nashik","sangamner","nagpur")
#            -6      -5        -4      -3         -2         -1
print(cities[1])
print(cities[1:5])
print(cities[1:-1])
print(cities[0:-3])
print(cities[::-1]) # reverce


# 
fruits = ("apple","banana","mango","grapes")
f1 = len(fruits)
print(f1)
# 

Numbers = (11,22,33,44,44,55,66,44,44,44,44)
print(min(Numbers))
print(max(Numbers))

n1 = Numbers.count(44)
n2 = Numbers.index(22)
n3 = sorted(Numbers)
print(n1)
print(n2)
print(n3)

print("pratiksha" not in ("pratiksha","shital","monika"))
print("pratiksha" in ("pratiksha","shital","monika"))


num = (44,55,33,44,55)
if(21 in num):
    print("no. is available")
else:
    print("no. is not available")


animals = ("dog","lion","cat","cow")
for animal in animals:
    print(animal) 

for i in range(len(animals)):
    print(animals[i])

