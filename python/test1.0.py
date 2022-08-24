import abc


x=input('Enter any word:-')
y={}
for i in x:
    if i in y:
        y[i]=y[i]+1
    else:
        y[i]=1

for k, v in y.items():
    print(k+ " ==> "+str(v))