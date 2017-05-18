#!/usr/bin/env python3

import socket
import time
from functools import reduce
from itertools import count


def connect(bind, msg, buf_size=4096):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(bind)
    sock.sendall(msg.encode("ASCII"))
    ans = sock.recv(buf_size)
    sock.close()
    return ans.decode("ASCII")

if __name__ == "__main__":
    import os
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("-c", "--connect", type=str, default=None)

    args = parser.parse_args()

    conn_str = args.connect or os.getenv("PG_CONN") or "localhost:6666"

    host, port = conn_str.split(":")
    port = int(port)

    def f(acc, i):
        msg = "{:09d}\n".format(i)
        try:
            ans = connect((host, port), msg)
        except Exception as e:
            print("Could not connect: {}".format(e))
        else:
            print("sent [{}], received [{}]".format(msg.strip(), ans.strip()))
        time.sleep(2)

    reduce(f, count(0))
