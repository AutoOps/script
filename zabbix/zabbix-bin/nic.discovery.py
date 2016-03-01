#!/usr/bin/env python
import os
import json
t=os.popen(""" ip link |grep  state[[:space:]]UP |grep eth |awk -F: '{print $2}'|grep -v @  """)
ports = []
for port in  t.readlines():
        r = os.path.basename(port.strip())
        ports += [{'{#NICNAME}':r}]
print json.dumps({'data':ports},sort_keys=True,indent=4,separators=(',',':'))
