from functools import reduce

# map()
list1 = [1991,1993,1995,1996,1998,1999]
list2 = []
for items in list1:
    # print(2022 - items)
    list2.append(2022 - items)
print(list2)

a1 = list(map(lambda x:2022 - x,list1))
print(a1)

listA = [1,2,3,4,45,6]
a2 = list(map(lambda x:3 * x, listA))
print(a2)


names = ['pratiksha','monika','shital','snehal']
a3 = list(map(lambda x:'hello' + " " + x,names))
print(a3)

# filter()
num = [12,23,34,45,65,43,22]
num1 = []
for item in num:
    if item > 30:
        num1.append(item)
print(num1)        

print(list(filter(lambda x:x>=30,num1)))

numbers = [11,22,33,44,55,66,77,88,99]
print(list(filter(lambda x:x%2 == 0, numbers)))

student = ['aa','aaa','aaaa','aaaqa','aaaa']
print(list(filter(lambda x:len(x) == 4, student)))

# reduce()

s1 = [2,3,4,5,6]
sum = 0
for item in s1:
    sum = sum + item
print(sum)    

s2 = [22,3,4,5,6]
print(reduce(lambda acc,nxtval:acc + nxtval,s2,50))
















