import random
n = 3 
a_list = [random.randrange(65, 91) for i in range(n)]
b_list = [chr(random.randrange(65, 91)) for i in range(n)]
print(a_list)
c_list = a_list + b_list + a_list * 2
print(c_list)

d_list =c_list.copy()
print(d_list)

e_list = [chr(i) for i in d_list]

print(e_list)
             

#f_list = [ord(i) for i in e_list]