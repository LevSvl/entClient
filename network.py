import sys
import socket
from ast import literal_eval as transform
from ctypes import c_int32
import struct

conf = {
    'hostName': '127.0.0.1',
    'port': 6780
}

assert conf.get('hostName')!=None, "Configure hostname parameter"
assert conf.get('port')!=None, "Configure port parameter"

class TCPClient:
    def __init__(self) -> None:
        self.hostAddr = conf.get('hostName')
        self.hostPort = conf.get('port')
        self.socket = self.configure_socket() 
    
    def __enter__(self):
        self.socket.connect((self.hostAddr,self.hostPort))
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def close_connection(self):
        self.socket.close()

    def configure_socket(self):
        clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        return clientSocket

    def validate_start_params(self,params):
        _s = self.socket
        # Сериализуем параметры
        _data = str(params).encode()
        # Отправляем на сервер
        _s.send(_data)
        print(_s.recv(30))
    
    def get_pos_info(self):
        return self.get_int()

    def send_pos_info(self,x:int):
        return self.send_int(x)
    
    def send_int(self,x:int):
        _s = self.socket
        _s.sendall(struct.pack('I',x))
        # _s.send(str(x).encode())
        return 0

    def get_int(self):
        _s = self.socket
        x = _s.recv(4)
        x = struct.unpack('I', x)[0]
        return x

    @staticmethod
    def transform_data(data:str):
        data = transform(data)
        return data
    
if __name__ == '__main__':
    a = 146
    conn = TCPClient()
    with conn:
        # conn.send_int(a)
        x = conn.get_int()
        print(x)