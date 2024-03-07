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

import os,re,json
from bs4 import BeautifulSoup as bs
def clean(a):
    return a if len(a)<61 else '%s...'%a[:61]
def clean2(a):
    return a if len(a)<13 else '%s...'%a[:13]
def rehtml(a):
    s=bs(a,'html.parser')
    l=s.find('link')
    l['href']='../Emblem_of_the_PCP-Shining_Path.svg.ico'
    l=s.select("img[src*='GFDL']")[0]
    l['src']='../GFDL-logo-small.png'
    return s.prettify()
ks=['江青','云鹤','文元','洪文','春桥']
if not os.path.exists(p1:='中央文革CCRD数据库全集（标题提及）'):
    os.mkdir(p1)
if not os.path.exists(p2:='中央文革CCRD数据库全集（内容提及）'):
    os.mkdir(p2)
for a in os.walk('HTML'):
    a[2].sort()
    lf=[b for b in a[2]if re.search(r'\d{6}',b)]
    for b in lf:
        f=open('%s/%s'%(a[0],b),'r');t=f.read();f.close()
        t=rehtml(t)
        f=open('%s/%s.json'%(a[0].replace('HTML','JSON'),'.'.join(b.split('.')[:-1])),'r');js=json.loads(f.read());f.close()
        k=0
        for c in ks:
            if js['title'].find(c)!=-1:
                k=1
        for c in ks:
            if k==0 and t.find(c)!=-1:
                k=2
        ti='%s-%s%s-%s-%s.htm'%(js['date'].replace('/','-'),
                             clean(js['title']).replace('/','-'),
                             clean2('-%s'%','.join(js['authors'])if js['authors']else'').replace('/','-'),
                             '-'.join(a[0].split('/')[1:]),
                             '.'.join(b.split('.')[:-1]))
        if k==1:
            f=open(dst:='%s/%s'%(p1,ti),'w+');f.write(t);f.close()
            print(dst)
        elif k==2:
            f=open(dst:='%s/%s'%(p2,ti),'w+');f.write(t);f.close()
            print(dst)

ks=['远新']
if not os.path.exists(p1:='毛远新CCRD数据库全集（标题提及）'):
    os.mkdir(p1)
if not os.path.exists(p2:='毛远新CCRD数据库全集（内容提及）'):
    os.mkdir(p2)
for a in os.walk('HTML'):
    a[2].sort()
    lf=[b for b in a[2]if re.search(r'\d{6}',b)]
    for b in lf:
        f=open('%s/%s'%(a[0],b),'r');t=f.read();f.close()
        t=rehtml(t)
        f=open('%s/%s.json'%(a[0].replace('HTML','JSON'),'.'.join(b.split('.')[:-1])),'r');js=json.loads(f.read());f.close()
        k=0
        for c in ks:
            if js['title'].find(c)!=-1:
                k=1
        for c in ks:
            if k==0 and t.find(c)!=-1:
                k=2
        ti='%s-%s%s-%s-%s.htm'%(js['date'].replace('/','-'),
                             clean(js['title']).replace('/','-'),
                             clean2('-%s'%','.join(js['authors'])if js['authors']else'').replace('/','-'),
                             '-'.join(a[0].split('/')[1:]),
                             '.'.join(b.split('.')[:-1]))
        if k==1:
            f=open(dst:='%s/%s'%(p1,ti),'w+');f.write(t);f.close()
            print(dst)
        elif k==2:
            f=open(dst:='%s/%s'%(p2,ti),'w+');f.write(t);f.close()
            print(dst)
