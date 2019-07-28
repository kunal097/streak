import socket




soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soc.connect(('localhost',8001))

key = input('Enter room key: ')
soc.sendall(key.encode('utf-8'))
data = soc.recv(1024).decode('utf-8')
while 1:
    if data == 'False':
            key = input('Not Auhorised \nEnter room key: ')
    else:
        break

while True:

    msg = input('Client : ')

    # msg = '+='.join([key,msg])
    soc.sendall(msg.encode('utf-8'))

    data = soc.recv(1024).decode('utf-8')




    print('Server : {}'.format(data))


soc.close()
