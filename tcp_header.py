import struct

class TCPHeader:
	
	def __init__(self,src_port,dst_port):
		self.src_port = src_port
		self.dst_port = dst_port
		
		
	def build(self):
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

		tcp_hdr = struct.pack("!HHLLBBH2sH", self.src_port, self.dst_port, seq_num, ack_num, tcp_hdr_len, tcp_flags, window_size, tcp_chksum, urg_ptr)
		
		return tcp_hdr
