from __future__ import print_function
from scapy.all import *
import time
j=0

def http_packet():
	dest='172.17.0.3'
	syn =IP(dst=dest) / TCP(dport=80, flags='S')
	syn_ack = sr1(syn)
	getStr = 'GET / HTTP/1.1\r\nHost: 172.17.0.3\r\n\r\n'
	request = IP(dst=dest) / TCP(dport=80, sport=syn_ack[TCP].dport,
				 seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A') / getStr
	reply = sr1(request) 	
	
def dns_query():
	dest1='172.18.0.2'
	answer = sr1(IP(dst=dest1)/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname='www.thepacketgeek.com')), verbose=0)
	
	
exit()
