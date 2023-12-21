import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8888))
s.listen(5)
while 1:
    try:
        client, addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        break
    else:
        result = client.recv(4096)
        print('Message: ', result.decode('utf-8'))
        print('Address', addr)

