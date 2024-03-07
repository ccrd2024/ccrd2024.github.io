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

from xml.dom import minidom
import os,re
from datetime import datetime
from datetime import timezone, timedelta
from bs4 import BeautifulSoup as bs
import xml.etree.ElementTree as ET

print('Start to generate sitemap.xml...')

def simplifyPath(path):
    """
    :type path: str
    :rtype: str
    """

    s_list = path.split("/")
    temp_str = "|".join(s_list)
    s_list = temp_str.split('|')

    new_list = []

    for item in s_list:
        if item == ".":
            continue

        elif item == "..":
            if new_list:
                new_list.pop(-1)

        else:
            new_list.append(item)

    new_str = "/" + "/".join(new_list)

    return re.sub(r'\/{2,}','/',new_str)

link='https://ccrd2024.github.io'
pa='/media/a/Maoism/ccrd2024.github.io'

#ls=['%s/'%link]
li=['%s/index.htm'%pa]
n=0
while True:
    if n>=len(li):break
    if not os.path.exists(li[n]):
        li[n]=None
        n+=1
        continue
    if'/pages/'in li[n]:
        n+=1
        continue
    print(li[n])
    if li[n][-4:]=='.pdf':
        n+=1
        continue
    if li[n].find('原件版 CCRD 中国当代政治运动史数据库（在线阅读html版）')!=-1:
        n+=1
        continue
    f=open(li[n],'r');t=f.read();f.close()
    s=bs(t,'html.parser')
    li2=[a.get('href').split('#')[0]for a in s.find_all('a')if a.get('href')]
    li3=[]
    for b in li2:
        if b not in li3:
            if(b[-4:]=='.htm' or b[-5:]=='.html' or b[-4:]=='.pdf')and('原件版 CCRD 中国当代政治运动史数据库（在线阅读html版）'not in b):
                li3.append(b)
    ad=[]
    for b in ([simplifyPath('%s/%s'%('/'.join(li[n].split('/')[:-1]),a))for a in li3 if a[:4]!='http'and a[:6]!='mailto']):
        if b not in li:
            li.append(b)
            ad.append(b)
    n+=1
li=[[a,os.path.getmtime(a)] for a in li if a]
ls=[[a[0].replace(pa,link),a[1],a[0]]for a in li]
#print(ls)

root = minidom.Document()

xml = root.createElement('urlset')
root.appendChild(xml)
xml.setAttribute('xmlns','http://www.sitemaps.org/schemas/sitemap/0.9')
xml.setAttribute('xmlns:xsi','http://www.w3.org/2001/XMLSchema-instance')
xml.setAttribute('xsi:schemaLocation','''http://www.sitemaps.org/schemas/sitemap/0.9
            http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd''')
co=root.createComment('created with Marxism-Leninism-Maoism Website Sitemap Generator')
xml.appendChild(co)

n=0
for a in ls:
    pc1=root.createElement('url')
    pc2=root.createElement('loc')
    pc3=root.createElement('lastmod')
    pc4=root.createElement('priority')
    pc2.appendChild(root.createTextNode(a[0]))
    pc3.appendChild(root.createTextNode(str(datetime.fromtimestamp(int(a[1]),tz=timezone(timedelta(hours=0)))).replace(' ','T')))
    f=a[0].split('.')[-1]
    pc4.appendChild(root.createTextNode(str((0.8 if f in['htm','html']else 0.64 if f in['pdf']else'new file')if n!=0 else 1.0)))
    pc1.appendChild(pc2)
    pc1.appendChild(pc3)
    pc1.appendChild(pc4)
    if a[2][-4:]=='.htm'or a[2][-5:]=='.html':
        f=open(a[2],'r');ps=f.read();f.close()
        s=bs(ps,'html.parser')
        if(ss:=s.find('title')):
            ti=ss.get_text()
            pc5=root.createElement('title')
            pc5.appendChild(root.createTextNode(ti))
            pc1.appendChild(pc5)
    xml.appendChild(pc1)
    n+=1
xml_str = root.toprettyxml(indent="    ", encoding="utf-8")

f=open('%s/sitemap.xml'%pa,'wb+');f.write(xml_str);f.close()

print('Finish to generate sitemap.xml...')
