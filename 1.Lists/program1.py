'''
*******************Lists*****************************
properties
1.Dynamic Size
2.Allows Items of Different Types

'''


# l=[10,20,30,40,50]
# print(l)                       # l = [10 , 20 , 30 , 40 , 50]
# print(l[3])                    #       0    1    2    3    4
# print(l[-1])                   #      -5   -4   -3   -2   -1
# print(l[-2])


#Some more properties of list 
# l=[ 10,20,30,40,50]
# l.append(30)
# print(l)
# l.insert(1,15)
# print(l)
# print(15 in l)
# print(l.count(30))
# print(l.index(30))

# l=[10,20,30,40,50,60,70,80]
# l.remove(20)
# print(l)
# print(l.pop())  # the poped value is returned and printed 
# print(l)        #by default pop deletes the last element 
# print(l.pop(2))   #value removed from index=2 
# print(l)
# del l[1]        #another way of deleting element 
# print(l)
# del l[0:2]     #deleting element based on index 
# print(l)

l=[10,40,20,50]
print(max(l))
print(min(l))
print(sum(l))
l.reverse()
print(l)
l.sort()
print(l)