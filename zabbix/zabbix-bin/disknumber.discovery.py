#!/usr/bin/env python
import os
import json
t=os.popen("""  /etc/zabbix/bin/MegaCli/MegaCli64 -PDList -aALL  | egrep Slot[[:space:]]Number:[[:space:]] | awk -F : '{print $2}'  """)
ports = []
for port in  t.readlines():
        r = os.path.basename(port.strip())
        ports += [{'{#DISKNUM}':r}]
print json.dumps({'data':ports},sort_keys=True,indent=4,separators=(',',':'))
