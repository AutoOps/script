#!/usr/bin/env python
import os
import json
t=os.popen(""" lsblk  |grep disk |awk '{print $1}'  """)
ports = []
for port in  t.readlines():
        r = os.path.basename(port.strip())
        ports += [{'{#DISKNAME}':r}]
print json.dumps({'data':ports},sort_keys=True,indent=4,separators=(',',':'))
