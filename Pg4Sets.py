'''
s = {11,22,33,44,55,66,77,88,22,11,33}
print(s)
a = set()
print(a)
a.add(33)
a.add(55)
a.add(33)
a.add(33)
a.add("Shilpa")
print(a)
shilpa = ['Mond','Tues','Mond','Wed']
albert = ['Thu','Mond','Fri']
s = set(shilpa)
a = set(albert)
print(s|a)
print(s&a)
'''

'''
s = {11,22,33}
s.update(['aaa',999,555,222])
s.add(8888)
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)
'''
'''s = {11,22,33,44,55,66}
s.remove(44)
print(s)
if 999 in s:
    s.remove(999)
    print(s)'''

'''
s = {11,22,33,44,55,66}
s.discard(44)
print(s)
s.discard(9999)
print(s)'''
'''
a = {11,22,33,44,55}
b = {33,44,55,66,77}
print(a.intersection(b))
print(a.union(b))
'''
'''
a = {11,22,33,44,55,66}
b = {33,44,55,66,77}
a.intersection_update(b)
print(a, b)
#a={33, 66, 44, 55} b ={33, 66, 55, 44, 77}
b.intersection_update(a)
print(a, b)
'''
a = {11,22,33,44,55}
b = {33,44,55,66,77,88}
print(a-b)
print(b-a)
print(a^b)





