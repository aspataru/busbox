import socket


class TimeboxMini:


    """Thanks to https://github.com/derHeinz/divoom-adapter"""


def __init__(self, addr):
    self.sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    self.addr = addr


def connect(self):
    self.sock.connect((self.addr, 4))


def disconnect(self):
    self.sock.close()


def send(self, package):
    self.sock.send(bytes(package))
