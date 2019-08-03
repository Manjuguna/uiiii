anytim1=(input())
catta=0
for i in range(0,len(anytim1)):
    suit=(anytim1[:i]+anytim1[i+1:])
    if(int(suit) % 8==0):
        catta=1
        break
if(catta==1):
    print("yes")
else:
    print("no")
