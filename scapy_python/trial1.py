from scapy.all import *
import time

s = conf.L3socket(iface='docker0')
s.send(ARP(pdst='172.17.0.2', 
		   psrc='172.17.0.1',  
		   op='is-at')
	  )
print 'sent packet';

