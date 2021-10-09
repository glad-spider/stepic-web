import socket 
import os 
s = socket.socket() 
s.bind(('0.0.0.0', 2222)) 
s.listen(5) 
for i in range(10): 
	child = os.fork() 
	if child == 0: 
		while True: 
			conn, addr = s.accept() 
			data = conn.recv(1024) 
			conn.send(data) 
			conn.close()