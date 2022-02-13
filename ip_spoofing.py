
import socket
import struct
import sys
from ip_header import IPHeader
from tcp_header import TCPHeader


def main(src_ip,src_port,dst_ip,dst_port):
	ip_packet = IPHeader(src_ip,dst_ip,6)
	tcp_packet = TCPHeader(src_port,dst_port)
	
	packet = ip_packet.build() + tcp_packet.build()
	
	rawsocket = socket.socket(socket.AF_INET, 		socket.SOCK_RAW, socket.IPPROTO_TCP)
	rawsocket.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)		
							   

	rawsocket.sendto(packet,(dst_ip,0))
	

if __name__ == "__main__":
	
	src_ip = sys.argv[1]
	src_port = int(sys.argv[2])
	dst_ip = sys.argv[3]
	dst_port = int(sys.argv[4])

	main(src_ip,src_port,dst_ip,dst_port)

	print("[+] IP spoofed packet sent")
