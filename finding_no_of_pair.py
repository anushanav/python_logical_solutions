
list =[10, 20, 20, 10, 10, 10]
# s = set(list)
s = []
for j in list:
    if j not in s:
        s.append(j)
print (s)
pairs = 0
for i in s:
    freq = list.count(i)
    pairs = pairs + freq//2
print (pairs)
