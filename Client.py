from socket import *
import threading
import time
import cv2
import struct
import pickle
import time
def send(sock):
    cap=cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
    
    encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
    while True:
        ret,frame=cap.read()
        result,frame=cv2.imencode('.jpg',frame,encode_param)
        data=pickle.dumps(frame,0)
        size=len(data)
        #print("Frame test : ",size)
        start=time.time()
        sock.sendall(struct.pack(">L",size)+data)
        #print("time :", time.time() - start)
    cap.release()
def receive(sock):
    while True:
        recvData = sock.recv(1024)
        if recvData.decode("utf-8")=="1":
            print("Red")
        elif recvData.decode("utf-8")=="2":
            print("Green")
        else:
            print("상대방 :", recvData.decode("utf-8"))

port = 50000
clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('165.229.125.142', port))

print('접속 완료')

sender = threading.Thread(target=send, args=(clientSock,))
receiver = threading.Thread(target=receive, args=(clientSock,))

sender.start()
receiver.start()
while True:
    time.sleep(1)
    pass

clientSock.close()