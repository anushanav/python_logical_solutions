# Finding the smallest and biggest statue
# and the number of numbers left to complete sequence

statues=[8,1,0,4,7]
i = 0
small=statues[i]
big=0
for i in range(len(statues)):
     if statues[i]<small:
            small=statues[i]
     if statues[i]> big:
            big=statues[i]
print(big,small)
print (big-small-len(statues)+1)
        