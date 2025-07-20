from scapy.all import sniff
def packet_callback(packet):
    if packet.haslayer('IP'):
        ip_layer = packet['IP']
        print(f"Source IP: {ip_layer.src} --> Destination IP: {ip_layer.dst}")
        print(f"Protocol: {ip_layer.proto}")
        print(f"Payload: {bytes(packet.payload)}")
        print("-" * 50)
sniff(prn=packet_callback, count=10)
