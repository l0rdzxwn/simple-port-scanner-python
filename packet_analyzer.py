import scapy.all as s

target_ip = '10.1.17.215'

packets = s.rdpcap(r"D:\pcaps\2025-01-22-traffic-analysis-exercise.pcap")
mac = ""
host = ""
acc = ""
for pkt in packets:
    if pkt.haslayer(s.IP) and pkt.haslayer(s.KRB_AS_REQ) and pkt[s.IP].src == target_ip:
        mac = pkt[s.Ether].src
        cname = pkt[s.KRB_AS_REQ].reqBody.cname.nameString[0].val.decode('utf-8', errors='ignore')

        if cname.endswith('$'):
            host = cname.rstrip('$').upper()
        else:
            acc = cname
 
        
        
         


print(f"\nTarget IP Address: {target_ip}")
print(f"Mac Address: {mac}")
print(f"Account Name: {acc}")
print(f"Host Name: {host}")
        