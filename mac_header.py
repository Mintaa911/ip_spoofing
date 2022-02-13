class EtherentHeader:

	def __init__(self,src_mac,dst_mac,protocol):
		self.src_mac = src_mac
		self.dst_mac = dst_mac
		self.protocol = protocol
		
	def build(self):
		source_mac = b"\x08\x00\x27\x80\xab\x30" # Converting  into byte object

		dst_mac = b"\x08\x00\x27\x7e\xe3\x3b" # Converting  into byte object

		dst_ip = "10.5.198.64" # This is the destination

		protocol = 0x0800

		eth_hdr = struct.pack("!6s6sH", dst_mac, source_mac, 					protocol)

		return eth_hdr
