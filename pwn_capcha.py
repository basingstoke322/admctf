import socket
from art import *

# bm = Basemap()
s = socket.socket()
s.connect(('212.34.152.215', 50090))
s.settimeout(90000000)

alph = {}
for i in string.ascii_uppercase:
    alph[i] = text2art(i, font='cybermedium').split('\n')[:3]

while True:
    h = s.recv(1000)
    if h.find(b'solved') == -1:
        h = h + s.recv(1000)
    print(h.decode())
    a = h.decode().split('\r\n')[1:5]
    decoded = ''
    while len(a[0]) > 0:
        cand = []
        ln = 0
        for i in alph.items():
            ln = len(i[1][1])
            if a[0][-ln:] == i[1][0] and\
                a[1][-ln:] == i[1][1] and\
                a[2][-ln:] == i[1][2]:
                cand.append((i[0], ln))
        r = max(cand, key=lambda x: x[1])
        decoded = decoded + r[0]
        for i in range(3):
            a[i] = a[i][:-r[1]]
    v = decoded[::-1]
    s.send(v.encode()+b'\n')
