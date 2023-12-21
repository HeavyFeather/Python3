import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8888))
while 1:
    try:
        message = input('Your message: ')
        s.send(message.encode())
    except KeyboardInterrupt:
        s.close()
        break
