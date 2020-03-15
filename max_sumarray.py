l = [-2,-3,4,-1,-2,1,5,-3]

summ_l = []
max = -1 * (10**5)
s =0
count = 0

for i in l:
    count +=1
    s += i
    summ_l.append(s)
    if max < s:
        max = s

print(summ_l)


for i in range(len(l)):
    for j in range(i,len(l)):
        count += 1
        summ_l[j]= summ_l[j]-l[i]
        if max<summ_l[j]:
            max = summ_l[j]
print(max,count)