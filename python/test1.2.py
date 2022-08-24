word=input('enter any word')
d={}
for k in word:
    d[k]=d.get(k,0)+1
    for k,v in d.items():
        print(f'{k} occurred {v} times' )