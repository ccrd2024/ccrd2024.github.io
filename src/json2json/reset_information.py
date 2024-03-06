import os,sys
for a in os.walk(sys.path[0]):
    for b in a[2]:
        if b[-5:]=='.json':
            f=open(pa:='%s/%s'%(a[0],b),'r');t=eval(f.read());f.close()
            c='/'.join(pa.split('/')[:-1])
            if int(c.split('/')[-1])<1000:
                os.rename(c,'%s/%s'%('/'.join(c.split('/')[:-1]),t['date'].split('-')[0]))
                break
