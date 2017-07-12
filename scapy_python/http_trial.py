from scapy.all import *

dest='172.17.0.2'
syn = IP(dst=dest) / TCP(dport=80, flags='S')
syn_ack = sr1(syn)

getStr = 'GET / HTTP/1.1\r\nHost: 172.17.0.2\r\n\r\n'
request = IP(dst=dest) / TCP(dport=80, sport=syn_ack[TCP].dport,
			 seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A') / getStr
reply = sr1(request)
