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
