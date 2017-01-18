#!/usr/bin/python
# -*- coding: UTF-8 -*-
from scapy.all import *
try:
    # This import works from the project directory
    import scapy_http.http
except ImportError:
    # If you installed this package via pip, you just need to execute this
    from scapy.layers import http
packets = scapy.rdpcap('C:\\Users\Administrator.PC-201603070155\Desktop\dsploit-sniff-1484639588892.pcap')
for p in packets:
    print '=' * 78

for f in p.payload.fields_desc:
        if f.name == 'src' or f.name == 'dst':
            ct = scapy.conf.color_theme
            vcol = ct.field_value
            fvalue = p.payload.getfieldval(f.name)
            reprval = f.i2repr(p.payload,fvalue)
            print "%s : %s" % (f.name, reprval)

for f in p.payload.payload.fields_desc:
        if f.name == 'load':
            ct = scapy.conf.color_theme
            vcol = ct.field_value
            fvalue = p.payload.getfieldval(f.name)
            reprval = f.i2repr(p.payload,fvalue)
            print "%s : %s" % (f.name, reprval)