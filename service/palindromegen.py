#!/usr/bin/env python3

import socketserver
from functools import partial

class Handler(socketserver.StreamRequestHandler):

    def handle(self):
        print("new connection from {}".format(self.client_address[0]))
        in_str = self.rfile.readline().strip().decode("ASCII")
        out_str = "{}{}\n".format(in_str, in_str[::-1]).encode("ASCII")
        self.wfile.write(out_str)
        self.wfile.close()


if __name__ == "__main__":
    import os
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("-b", "--bind", type=str, default=None)
    parser.add_argument("-p", "--port", type=int, default=None)

    args = parser.parse_args()

    port = args.port or os.getenv("PG_PORT") or 6666
    host = args.bind or os.getenv("PG_HOST") or "0.0.0.0"

    s = socketserver.TCPServer((host, port), Handler)
    s.serve_forever()
