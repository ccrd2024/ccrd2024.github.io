import os,sys
for a in os.walk(sys.path[0]):
    for b in a[2]:
        try:
            if int('.'.join(b.split('.')[:-1]))<1000:
                os.remove('%s/%s'%(a[0],b))
        except:pass
