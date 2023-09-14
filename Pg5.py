'''a  = 77
b = a
print(id(a))
print(id(b))
b = 99
print(id(a))
print(id(b))'''
'''
import copy
a = [11,22,33,44]
b = copy.copy(a)
print(a,b)
print(id(a),id(b))
b[1] = 999
print(a,b)
print(id(a),id(b))
'''

import copy
a = [11,22,33,44,[10,20,30],999]
b = copy.deepcopy(a)
print(a,b)
print(id(a),id(b))
b[4][2] = 666
print(a,b)
print(id(a),id(b))





