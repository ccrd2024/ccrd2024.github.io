import os,re,json
from bs4 import BeautifulSoup as bs
def clean(a):
    return a if len(a)<61 else '%s...'%a[:61]
def clean2(a):
    return a if len(a)<13 else '%s...'%a[:13]
for a in os.walk('HTML Old'):
    a[2].sort()
    lpas=len(a[0].split('/'))
    for b in a[2]:
        if re.search(r'\d{6}',b):
            f=open('%s/%s'%(a[0],b),'r');t=f.read();f.close()
            f=open('%s/%s.json'%(a[0].replace('HTML Old','JSON'),'.'.join(b.split('.')[:-1])),'r');js=json.loads(f.read());f.close()
            s=bs(t,'html.parser')
            bd=s.find('body')
            #
            ti='%s%s - %s - CCRD 中国当代政治运动史数据库'%(clean(js['title']),
                                                            clean2(' - %s'%','.join(js['authors'])if js['authors']else''),
                                                            js['date'])
            nhe=s.new_tag('head')
            nti=s.new_tag('title')
            nti.string=ti
            nic=s.new_tag('link')
            nic['rel']='icon'
            nic['type']='image/x-icon'
            nic['href']='%sEmblem_of_the_PCP-Shining_Path.svg.ico'%'%s/'%'/'.join(['..'for z in range(lpas)])
            nhe.append(nti)
            nhe.append(nic)
            bd.insert_before(nhe)
            ti=s.find('h1')
            np=s.new_tag('p')
            na=s.new_tag('a')
            na['href']='index.htm'
            na.string='[返回索引页面]'
            np.append(na)
            slj=s.new_tag('script')
            metati=s.new_tag('meta')
            metada=s.new_tag('meta')
            metaau=s.new_tag('meta')
            slj['type']='application/ld+json'
            metati['property']='title'
            metada['property']='date'
            metaau['property']='authors'
            slj.string=json.dumps(js)
            metati['content']=js['title']
            metada['content']=js['date']
            metaau['content']=','.join(js['authors'])
            ti.insert_before(metati)
            ti.insert_before(metada)
            ti.insert_before(metaau)
            ti.insert_before(slj)
            ti.insert_before(np)
            np2=s.new_tag('p')
            na2=s.new_tag('a')
            na2['href']='index.htm'
            na2.string='[返回索引页面]'
            np2.append(na2)
            bd.append(np2)
            if not os.path.exists(pa2:='/'.join((pa:='%s/%s'%(a[0].replace('HTML Old','HTML'),b)).split('/')[:-1])):os.makedirs(pa2)
            lpas=len(pa2.split('/'))
            aft='''<hr/>
<p><img src="<!--GFDL PATH-->"/><br>
Copyright (C)  2024  Marxist-Leninist-Maoist.<br>
Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. A copy of the license is included in the section entitled "GNU Free Documentation License".</p>'''
            aft=aft.replace('<!--GFDL PATH-->','%sGFDL-logo-small.png'%'%s/'%'/'.join(['..'for z in range(lpas)]))
            aft=bs(aft,'html.parser')
            bd.append(aft)
            print(pa)
            f=open(pa,'w+');f.write(s.prettify());f.close()
