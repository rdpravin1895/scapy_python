from __future__ import print_function
from collections import deque 
from scapy.all import *
import time
from random import randint

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
	print("DNS query")
	
def ssdp():
	payload = "M-SEARCH * HTTP/1.1\r\n" \
	"HOST:239.255.255.250:1900\r\n" \
	"ST:upnp:rootdevice\r\n" \
	"MAN: \"ssdp:discover\"\r\n" \
	"MX:2\r\n\r\n"
	send(IP(dst="172.19.0.3") / UDP(sport=1900, dport= 1900) / payload)
	
queue=deque([http_packet(),dns_query(),ssdp()])

queue.append(http_packet())
queue.append(http_packet())
queue.append(dns_query())
queue.append(ssdp())
queue.append(dns_query())
queue.append(ssdp())

for i in range(0,11):
	if queue:
		a=randint(0, 9)
		print(a)
		pkt=queue.popleft()
		if(a<=3):
			pkt
		elif(a>3 and a<6):
			pkt
		else:
			pkt
	else:
		print("No more packets available")
		break
exit()
