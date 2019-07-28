import socket

from threading import Thread




soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soc.bind(('localhost',8001))

soc.listen(5)


'''

room 1 : 'qwertyuiop'
room 2 : 'asdfghjkl'
room3 : 'zxcvbnm'


'''


class Room:


    def __init__(self, key, num ):
        self.num = num
        self.key = key
        self.client = []



def comm(s, num, room):

    while 1:

        data = s.recv(1024).decode('utf-8')
        print('Client {} : {}'.format(num, data))
        # s.sendall(data.upper().encode('utf-8'))

        for c in room.client:
            c.sendall(data.upper().encode('utf-8'))

        print('Server: {}'.format(data.upper()))





    s.close()



print('Waiting for connection...')


conn_list = []

n = 0


while True:
    conn, addr = soc.accept()
    # print(addr)

    n += 1

    room1 = Room('qwertyuiop',1)
    room2 = Room('asdfghjkl',2)
    room3 = Room('zxcvbnm',3)

    key = conn.recv(1024).decode('utf-8')
    if key == 'qwertyuiop':
        conn.sendall(b'OK')
        room1.client.append(conn)
        soc_thread = Thread(target = comm, args=(conn, n, room1 ))



    elif key == 'asdfghjkl':
        conn.sendall(b'PK')
        room2.client.append(conn)
        soc_thread = Thread(target = comm, args=(conn, n, room2 ))


    elif key == 'zxcvbnm':
        conn.sendall(b'OK')
        room3.client.append(conn)
        soc_thread = Thread(target = comm, args=(conn, n, room3 ))

    else:
        conn.sendall(b'False')





    soc_thread.start()
    conn_list.append(soc_thread)



    # data = conn.recv(1024).decode('utf-8')
    # print('Client: {}'.format(data))
    # conn.sendall(data.upper().encode('utf-8'))
    # print('Server: {}'.format(data.upper()))



