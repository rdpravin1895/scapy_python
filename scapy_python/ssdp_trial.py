from scapy.all import IP, UDP, send, sniff
payload = "M-SEARCH * HTTP/1.1\r\n" \
"HOST:239.255.255.250:1900\r\n" \
"ST:upnp:rootdevice\r\n" \
"MAN: \"ssdp:discover\"\r\n" \
"MX:2\r\n\r\n"

send(IP(dst="172.17.0.3") / UDP(sport=1900, dport= 1900) / payload)
