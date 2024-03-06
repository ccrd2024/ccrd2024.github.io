import os,sys,re
def arfn(t):
    if not isinstance(t,list):raise TypeError
    d={}
    r=[]
    for a in t:
        a=re.sub('\s*:\s*','：',a)
        a=re.sub('\s*!\s*','！',a)
        a=re.sub('\s*\?\s*','？',a)
        a=re.sub('\s*<\s*','《',a)
        a=re.sub('\s*>\s*','》',a)
        a=re.sub('\s*\*\s*','×',a)
        a=re.sub('\s*\/\s*','-',a)
        a=re.sub('\s+',' ',a)
        if('"'in a)or('\''in a):
            n=''
            i=0
            i2=0
            for b in a:
                if b=='"':
                    i=1 if i==0 else 0
                    c='“'if i==1 else'”'
                elif b=='\'':
                    i2=1 if i2==0 else 0
                    c='‘'if i2==1 else'’'
                else:c=b
                n='%s%s'%(n,c)
            a=n
        if t.count(a)==1:
            r.append(a)
        else:
            if a not in d:d[a]=1
            else:d[a]+=1
            r.append('%s-%s'%(a,str(d[a]).rjust(2).replace(' ','0')))
    return r
def clean_filename(sfn,limit):
    return '%s%s%s.%s'%('/'.join(sfn.split('/')[:-1]),'/'if'/'in sfn else'',(a[:limit]if len(a:='.'.join(fn.split('.')[:-1]))>limit else a).replace('/','-'),fn.split('.')[-1])if'.'in(fn:=sfn.split('/')[-1])else'%s/%s'%('/'.join(sfn.split('/')[:-1]),(fn[:limit] if len(fn)>limit else fn).replace('/','-'))
def json2txt(t):
    r=[]
    for a in t:
        if a['type']=='title':
            l='# %s'%a['text']
        elif a['type']=='subtitle':
            l='## %s'%a['text']
        elif a['type']=='source':
            l='　　· %s'%a['text']
        elif a['type']=='appellation':
            l='　　（%s）'%a['text']
        elif a['type']=='authors':
            l='　　<%s>'%a['text']
        else:
            l='　　%s'%a['text']
        r.append(l)
    r='\n\n'.join(r)
    return r
nn=0
for a in os.walk(sys.path[0]):
    a2=[]
    for b in a[2]:
        if b[-5:]=='.json':a2.append(b)
    a3=a2.copy()
    a2=[]
    for b in a3:
        f=open(pa:='%s/%s'%(a[0],b),'r');t=eval(f.read());f.close()
        a2.append(clean_filename('%s.txt'%('-'.join([m for m in [t['title'],t['date'],'-'.join(t['authors'])]if m])),128))
    a2=['%s.txt'%(v)for v in arfn([v.split('.txt')[0].strip()for v in a2])]
    n=0
    for b in a3:
        nn+=1
        if nn%1000==0:print(nn)
        if not os.path.exists(dn:='%s/%s'%(a[0],a2[n])):
            f=open(pa:='%s/%s'%(a[0],b),'r');t=eval(f.read());f.close()
            f=open(dn,'w+');f.write(json2txt(t['contents']));f.close()
        n+=1
