import os,sys
for a in os.walk(sys.path[0]):
    for b in a[2]:
        try:int('.'.join(b.split('.')[:-1]))
        except:os.remove('%s/%s'%(a[0],b))
