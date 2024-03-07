# /*
#  * Marxism-Leninism-Maoism CCRD And Arrangement Copyright (C) 2024 Marxist-Leninist-Maoist
#  *
#  * SPDX-License-Identifier: GPL-3.0-or-later
#  *
#  * This program is free software: you can redistribute it and/or modify it under
#  * the terms of the GNU General Public License as published by the Free Software
#  * Foundation, either version 3 of the License, or (at your option) any later
#  * version.
#  *
#  * This program is distributed in the hope that it will be useful, but WITHOUT
#  * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  * FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#  *
#  * You should have received a copy of the GNU General Public License along with
#  * this program. If not, see <https://www.gnu.org/licenses/>.
#  */

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
def json2html(t):
    r=[]
    for a in t:
        if a['type']=='title':
            l='<h1>%s</h1>'%a['text']
        elif a['type']=='subtitle':
            l='<h3>%s</h3>'%a['text']
        elif a['type']=='source':
            l='<strong>%s</strong>'%a['text']
        elif a['type']=='appellation':
            l='<h3><em>%s</em></h3>'%a['text']
        elif a['type']=='authors':
            l='<em>%s</em>'%a['text']
        else:
            l='<p>%s</p>'%a['text']
        r.append(l)
    r='\n'.join(r)
    return '<html>\n<body>\n%s\n</body>\n</html>'%r
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
    a2=['%s.htm'%(v)for v in arfn([v.split('.txt')[0].strip()for v in a2])]
    n=0
    for b in a3:
        nn+=1
        if nn%1000==0:print(nn)
        if not os.path.exists(dn:='%s/%s'%(a[0],a2[n])):
            f=open(pa:='%s/%s'%(a[0],b),'r');t=eval(f.read());f.close()
            f=open(dn,'w+');f.write(json2html(t['contents']));f.close()
        n+=1
