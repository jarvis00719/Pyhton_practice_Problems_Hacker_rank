import math

# sqrt cannot end with - 2,3,7,8

nums= [9,15,48,144]
res = []
res_float = []

for i in nums:
    res.append(math.sqrt(i))
    
for y in res:
    frac,whole = math.modf(y)
    res_float.append(frac)
final = []

for z in res_float:

    if z>0:
        res_float.remove(z)
        final.append(z)
print(res_float)


    





        



