#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket
import threading
localIP = socket.gethostbyname(socket.gethostname())
client_port = 1025
server_port=1024
buf_size = 128
client_addr = (localIP, client_port)
server_addr=('',server_port)
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(server_addr)
def clientfun():
	while True:
		#client_data为发送内容
	    udp_client.sendto(client_data, client_addr)    
	#udp_client.close()
def serverfun():
	while True:
		#server_data为收到内容
	    server_data, server_addr = udp_server.recvfrom(buf_size)
	#udp_server.close()
threading.Thread(target=clientfun).start()
threading.Thread(target=serverfun).start()
