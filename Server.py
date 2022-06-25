from socket import *
import threading
import time
import cv2
import struct
import pickle
import time
def send(sock):
    while True:
        sendData = input(">>>")
        sock.send(sendData.encode("utf-8"))


def receive(sock):
    data=b""
    payload_size=struct.calcsize(">L")

    while True:
        end=time.time()
        while len(data) < payload_size:
            data+=sock.recv(4096)
        #print("time : " ,time.time()-end)
        packed_msg_size=data[:payload_size]
        data=data[payload_size:]
        msg_size=struct.unpack(">L",packed_msg_size)[0]

        while len(data)<msg_size:
            data+=sock.recv(4096)
        frame_data=data[:msg_size]
        data=data[msg_size:]
        #print("frame test :{}",format(msg_size))
        frame=pickle.loads(frame_data,fix_imports=True,encoding="bytes")
        frame=cv2.imdecode(frame,cv2.IMREAD_COLOR)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1)==ord('q'):
            break

port = 50000

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('127.0.0.1', port))
serverSock.listen(1)

print('%d번 포트로 접속 대기중...'%port)

connectionSock, addr = serverSock.accept()

print(str(addr), '에서 접속되었습니다.')

sender = threading.Thread(target=send, args=(connectionSock,))
receiver = threading.Thread(target=receive,args=(connectionSock,))

sender.start()
receiver.start()


while True:
    time.sleep(1)
    pass
serverSock.close()