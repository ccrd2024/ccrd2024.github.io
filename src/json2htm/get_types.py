import os,sys
ts=[]
n=0
for a in os.walk(sys.path[0]):
    a2=[]
    for b in a[2]:
        if b[-5:]=='.json':a2.append(b)
    a3=a2.copy()
    for b in a3:
        n+=1
        if n%1000==0:print(n)
        f=open(pa:='%s/%s'%(a[0],b),'r');t=eval(f.read());f.close()
        for c in t['contents']:
            if c['type']not in ts:ts.append(c['type'])
print(ts)
