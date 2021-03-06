
import socket
import struct


# Ether type of 0x0800 is of IP packet and more details available on
#  file in /usr/include/linux/if_ether.h

rawsocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))


rawsocket.bind(("enp0s3", socket.htons(0x0800)))

# Creating Ethernet Header first 14 bytes

source_mac = b"\x08\x00\x27\x80\xab\x30" # Converting  into byte object

source_ip = "10.5.217.100" # Change this to spoof the IP

dst_mac = b"\x08\x00\x27\x7e\xe3\x3b" # Converting  into byte object

dst_ip = "10.5.198.64" # This is the destination

protocol = 0x0800

eth_hdr = struct.pack("!6s6sH", dst_mac, source_mac, protocol)


# Creating IP Header next 

source = socket.inet_aton(source_ip)

dest = socket.inet_aton(dst_ip)

ver_ihl = b"E" #hex value of 45 4 is ip version and 5 is ihl

dscp_ecn = 0 # we dont want to set this

total_len = 46 # because in wireshark packet capture it said minimum length to be 46

identification = 1234 # just a random number set

flags_frag = 16384 # based on wireshark packet capture it is the value with DF set hex value of 0x4000

ttl = 64

prt = 6 # protcol 6 is for tcp protocol

hdr_chksum = b"0x14" # This is also a random value


ip_hdr = struct.pack("!1sBHHHBB2s4s4s", ver_ihl, dscp_ecn, total_len, identification, flags_frag, ttl, prt, hdr_chksum, source, dest)



# Creating TCP packet first 20 bytes, i am lazy to calculate the tcp checksum will update once i do it :P


src_port = 1337

dst_port = 80

seq_num = 0 

ack_num = 0

tcp_hdr_len = 80 # value set to 80 since in wireshark i was able to see the flags set and other data

# The flags set will always be pow(2, n) to unset give the value as 0

tcp_flags_reserved = 0 # let this be 0 

tcp_flags_nonce = 0 # To set give the value pow(2,8) that is 256

tcp_flags_cwr = 128 # To set give the value pow(2,7) that is 128

tcp_flags_ecn = 64 # To set give the value pow(2,6) that is 64

tcp_flags_urg = 32 # To set give the value pow(2,5) that is 32

tcp_flags_ack = 16 # To set give the value pow(2,4) that is 16

tcp_flags_psh = 8 # To set give the value pow(2,3) that is 8

tcp_flags_rst = 4 # To set give the value pow(2,2) that is 4

tcp_flags_syn = 2 # To set give the value pow(2,1) that is 2

tcp_flags_fin = 1 # To set give the value pow(2,0) that is 1


tcp_flags = tcp_flags_reserved + tcp_flags_nonce + tcp_flags_cwr + tcp_flags_ecn + tcp_flags_urg + tcp_flags_ack + tcp_flags_psh + tcp_flags_rst + tcp_flags_syn + tcp_flags_fin

window_size = 28800 # random value based on wireshark captures

tcp_chksum = b"0x0006" # random value, currently checksum is not calculated

urg_ptr = 0 # set it to 0

tcp_hdr = struct.pack("!HHLLBBH2sH", src_port, dst_port, seq_num, ack_num, tcp_hdr_len, tcp_flags, window_size, tcp_chksum, urg_ptr)

#combine Ether, IP, TCP

packet = eth_hdr + ip_hdr + tcp_hdr

rawsocket.send(packet)

print("[+] IP spoofed packet sent")
