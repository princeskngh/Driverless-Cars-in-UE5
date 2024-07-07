import sys
import socket
from ultralytics import YOLO
import numpy as np
import cv2
import pyautogui
from PIL import Image
from asyncio.windows_events import NULL

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 6001))
model = YOLO("yolov5xu.pt")

server.listen()

while True:
    try:
        client, address = server.accept()
        print('Connected')
        val = client.recv(1024).decode('utf-8')
        print(val)
        if val == 'click':
            while True:
                try:
                    frame = pyautogui.screenshot()  # Live screenshots of the game/app
                    frame = np.array(frame)

                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Converting BGR format to RGB format (image)
                    val = model(frame)

                    str_arr = ""
                    for r in val:
                        boxes = r.boxes.cpu().numpy()
                        coord = boxes.xywhn  # (x,y) values of bounding box
                        conf = boxes.conf  # Confidence value
                        cls = boxes.cls  # (class = Car)

                    for i in coord:
                        for j in i:
                            str_arr += str(j) + " "
                    print(str_arr)

                    client.send(str_arr.encode('utf-8'))
                except Exception as e:
                    print(f"Error during processing: {e}")
                    break
    except Exception as e:
        print(f"Connection error: {e}")
    finally:
        client.close()
        print('Connection closed')
