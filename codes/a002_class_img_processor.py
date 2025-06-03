# --------------- basic info --------------- *
# auther: wegener 
# time & date: 2024/11/19, 10:02
# project: a002_编译.py, PyCharm, a004_class_img_processor 
iii = 0


# --------------- debug-func --------------- *
def aa():
    print("a try\n")


def bb():
    global iii
    print("try order %d \n" % (iii))
    iii = iii + 1


# --------------- information if it's copied--------------- *

# * website of the project: 
# * name of the original author(can be LLM):

# ------------------------------end predefine------------------------------

# start import --- *
import math
# end import ----- *
# start import --- *
import math
# end import ----- *
import socket
import cv2
import io
from PIL import Image
import numpy as np
import torch

import socket
import cv2
import io
from PIL import Image
import numpy as np
import torch


class YOLOv5Detector:
    def __init__(self, model_path, device='cpu'):
        self.fx = 1000
        self.fy = 1000
        self.cx = 960
        self.cy = 540
        self.model_path = model_path
        self.device = device
        self.model = self.load_model()
        self.socket = self.bind_socket()

    def load_model(self):
        print('yolov5 model loading')
        model = torch.hub.load(repo_or_dir=self.model_path,  # "'ultralytics/yolov5'",
                               model='yolov5s',
                               device=self.device,
                               source='local',  # changed
                               pretrained=True)
        print('yolov5 model loaded')
        return model

    def bind_socket(self):
        print('socket binding')
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
        s.bind(("0.0.0.0", 9090))
        print('socket binded')
        return s

    def classify(self, img):
        print('classifying')
        results = self.model(img)
        results.render()
        print(results)
        print('classified')
        return results

    def calculate_distance(self, x1, y1, x2, y2):
        w = x2 - x1  # 目标的宽度
        h = y2 - y1  # 目标的高度
        z = (self.fx * w) / (2 * (x2 - self.cx))  # 使用相机内参和目标在图像中的尺寸计算距离
        distance = z / 1000  # 将单位转换为米
        return distance

    def process_image(self, data):
        print('data receiving')
        bytes_stream = io.BytesIO(data)
        image = Image.open(bytes_stream)
        img = np.asarray(image)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # ESP32采集的是RGB格式，要转换为BGR（opencv的格式）
        print('data received')

        results = self.classify(img)
        boxes = results.xyxy[0].numpy()  # 提取边界框坐标
        confs = results.xyxy[0][:, 4].numpy()  # 提取置信度
        classes = results.xyxy[0][:, 5].numpy().astype(int)  # 提取类别，并转换为整数类型

        for i in range(len(boxes)):
            x1, y1, x2, y2 = boxes[i][0:4]  # 提取单个目标的边界框坐标
            conf = confs[i]  # 提取置信度
            cls = classes[i]  # 提取类别
            distance = self.calculate_distance(x1, y1, x2, y2)  # 计算目标到相机的距离

            print('distance=', distance)

            cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(img, f'{cls} {distance:.2f}m', (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA)

        cv2.imshow("ESP32 Capture Image", img)
        if cv2.waitKey(1) == ord("q"):
            cv2.destroyAllWindows()
            return False
        return img

    def run(self):
        while True:
            data, _ = self.socket.recvfrom(100000)
            self.process_image(data)
            if cv2.waitKey(1) == ord("q"):
                break



# 使用示例
if __name__ == "__main__":
    detector = YOLOv5Detector(model_path=r"C:\Users\wegener/.cache\torch\hub\ultralytics_yolov5_master")
    detector.run()
