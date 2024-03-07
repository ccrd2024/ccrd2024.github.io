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

import os,json
from natsort import natsorted, ns
bn='''0.中国文化大革命文库 (8291篇)
    0.有关文化大革命的中共文件、指示和公报 (1958篇)
    1.毛泽东关于文化大革命的讲话、指示和文章 (558篇)
    2.林彪关于文化大革命的讲话、指示和文章 (143篇)
    3.中央首长关于文化大革命的讲话和指示 (3240篇)
    4.有关文化大革命的重要报刊社论文章 (668篇)
    5.文化大革命中红卫兵、群众运动重要文献 (386篇)
    6.文化大革命中的异端思潮和公民异议的重要文献 (241篇)
    7.文化大革命的各类大事记和辞典 (388篇)
    8.文革中的特殊档案：检查、交代、申诉书、请罪书、遗书等 (709篇)
1.中国反右运动数据库，1957- (11265篇)
    0.和反右运动有关的官方文件(892篇)
    1.毛泽东有关反右运动的讲话、指示和文章(383篇)
    2.中共党政领导和反右运动有关的讲话和指示(597篇)
    3.“鸣放”言论和反右前后的重要报刊社论、文章(1358篇)
    4.重要的右派言论和文章(3876篇)
    5.有关反右的重要批判文章和报道(2982篇)
    6.反右档案：个人处理结论、检查交代和平反通知等(1205篇)
2.中国大跃进-大饥荒数据库，1958-1962 (6459篇)
    0.中共中央和各级政府关于大跃进 -- 大饥荒的重要文件(1824篇)
    1.毛泽东有关大跃进 -- 大饥荒的讲话、指示和文稿(602篇)
    2.中共党政领导有关大跃进 -- 大饥荒讲话和指示(854篇)
    3.大跃进 -- 大饥荒时期的重要报刊社论、文章(352篇)
    4.大跃进 -- 大饥荒时期的其他重要文章和报道(851篇)
    5.中共党内和社会民间的不满、抵制、反抗以及相关的骚乱(433篇)
    6.内部档案：调查报告、指示统计等等(1160篇)
    7.特殊档案：检查交代和处理结论等等(383篇)
3.中国五十年代初中期的政治运动数据库：从土地改革到公私合营，1949-1956(9781篇)
    0.中共中央和各级政府的文件和指示(2913篇)
    1.毛泽东的讲话、指示和文稿(949篇)
    2.中共党政领导的讲话和指示(1562篇)
    3.各主要报刊的社论和重要文章(566篇)
    4.其他重要文章和报道(1618篇)
    5.中共党内和民间社会的不满、抵制、反抗以及相关的骚乱(417篇)
    6.内部档案：调查报告、指示统计等等(1107篇)
    7.特殊档案：检查交代和处理结论等等(649篇)'''
bn=bn.split('\n')
bnn={}
for a in bn:
    if a[0]!=' ':
        if a not in bnn:
            bnn[a]=[]
            ed=a
    if a[0]==' ':
        bnn[ed].append(a.strip())
print(bnn)
bnn2=[str(a)for a in bnn.keys()]
for a in os.walk('JSON'):
    print(a[0])
    a[2].remove('index.htm')
    if'names.txt'in a[2]:a[2].remove('names.txt')
    al=natsorted(list(a[2]))
    if len(a[2])==0:
        l=[]
        l2=a[0].split('/')
        if len(l2)==1:
            for v in range(len(bnn2)):
                l.append(bnn2[v])
        elif len(l2)==2:
            for v in range(len(bnn[bnn2[int(l2[1])]])):
                l.append(bnn[bnn2[int(l2[1])]][v])
        elif len(l2)==3:
            ol=os.listdir(a[0])
            ol.remove('index.htm')
            if'names.txt'in ol:ol.remove('names.txt')
            ol=natsorted(ol)
            for v in range(len(ol)):
                f=open('%s/%s/000000.json'%(a[0],ol[v]),'r');t=json.loads(f.read());f.close()
                l.append(t['date'].split('-')[0])
        print(l)
    else:
        l=[]
        for b in al:
            if b not in['index.htm','names.txt']:
                if b[-5:]=='.json':
                    f=open('%s/%s'%(a[0],b),'r');t=json.loads(f.read());f.close()
                    l.append(t['title'])
    l='\n'.join(l)
    f=open(('HTML/%s/names.txt'%a[0].split('JSON')[1]).replace('//','/'),'w+');f.write(l);f.close()
    f=open(('TXT/%s/names.txt'%a[0].split('JSON')[1]).replace('//','/'),'w+');f.write(l);f.close()
    f=open(('JSON/%s/names.txt'%a[0].split('JSON')[1]).replace('//','/'),'w+');f.write(l);f.close()
