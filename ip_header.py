import socket
import struct

class IPHeader:

	def __init__(self,source_ip,dst_ip,protocol):
		self.source_ip = source_ip
		self.dst_ip = dst_ip
		self.protocol = protocol
		
		
	def build(self):
		source = socket.inet_aton(self.source_ip)

		dest = socket.inet_aton(self.dst_ip)

		ver_ihl = b"E" #hex value of 45 4 is ip version and 5 is ihl

		dscp_ecn = 0 # we dont want to set this

		total_len = 46 # because in wireshark packet capture it said minimum length to be 46

		identification = 1234 # just a random number set

		flags_frag = 16384 # based on wireshark packet capture it is the value with DF set hex value of 0x4000

		ttl = 64

		prt = self.protocol # protcol 6 is for tcp protocol

		hdr_chksum = b"0x14" # This is also a random value


		ip_hdr = struct.pack("!1sBHHHBB2s4s4s", ver_ihl, dscp_ecn, total_len, identification, flags_frag, ttl, prt, hdr_chksum, source, dest)
		
		return ip_hdr
