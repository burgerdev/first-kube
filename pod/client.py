#!/usr/bin/env python3

import socket
import time
from functools import reduce
from itertools import count


def connect(bind, msg, buf_size=4096):
    # create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Listen for incoming connections
    sock.connect(bind)
    sock.sendall(msg.encode("ASCII"))
    ans = sock.recv(buf_size)
    sock.close()
    return ans.decode("ASCII")

if __name__ == "__main__":
    def f(acc, i):
        msg = "{:09d}\n".format(i)
        ans = connect(("127.0.0.1", 6666), msg)
        print("sent [{}], received [{}]".format(msg.strip(), ans.strip()))
        time.sleep(2)

    reduce(f, count(0))
