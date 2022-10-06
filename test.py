a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
c = 4
r = 5
b = [x for x in a if 
     (x < c - 1) or 
     (x > c*(r-1)) or 
     (x % c == 0) or 
     ((x % c) == c-1)] 
g = 5
a = [1,2]
# while (g>0):
#     for x in a:
#         if x < 2:
#             continue
#         else:
#             print(x)
#             g-=1

a =[1,1,1,1,1,2,2,1,1,1]
print(1 in a)