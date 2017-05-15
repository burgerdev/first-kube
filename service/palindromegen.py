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

    s = socketserver.TCPServer(("0.0.0.0", 6666), Handler)
    s.serve_forever()
