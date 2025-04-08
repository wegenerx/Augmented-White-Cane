# preprocessing: del import resource_rc
import random


def remove_line_from_file(file_path, line_to_remove):
    """
    从指定文件中删除包含特定内容的行。

    参数:
    file_path (str): 要修改的文件路径。
    line_to_remove (str): 要删除的行中包含的文本。
    """

    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        # 创建一个新列表，用于存储不包含指定内容的行
    new_lines = [line for line in lines if line_to_remove not in line]

    # 将修改后的内容写回文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

    print(f"已成功从文件 {file_path} 中删除包含 '{line_to_remove}' 的行。")


# remove .ui line
remove_line_from_file('ui_/ui.py', 'import resource_rc')

import socket
import asyncio
import cv2
import io
from PIL import Image
import numpy as np
import torch
from PySide6.QtWidgets import QApplication
import sys
from codes.serial_tools import SerialTools
from codes import a001_讯飞星火对话
from codes.a003_voice import play_voice


def get_position(x):
    """
    根据输入的像素坐标x，判断其在图像中的位置（左、中、右）。
    假设图像宽度为320像素。
    """
    width = 320  # 图像宽度
    left_bound = width // 3  # 左边界（图像宽度的1/3处）
    right_bound = (width * 2) // 3  # 右边界（图像宽度的2/3处）

    if x < left_bound:
        return '左'
    elif left_bound <= x < right_bound:
        return '中'
    else:
        return '右'


class YOLOv5Detector:

    def __init__(self, model_path, device='cpu', if_show_img=False):
        self.fx = 1000
        self.fy = 1000
        self.cx = 960
        self.cy = 540
        self.model_path = model_path
        self.device = device
        self.model = self.load_model()
        self.socket = self.bind_socket()
        self.img = False

        # if show cv img
        self.if_show_img = if_show_img

        # distance, class
        self.distance_ = None
        self.distance_temp_ = None
        self.class_ = None
        self.direction = None

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

    # 判断图像的位置在哪边

    def process_image(self, data):
        print('data receiving')
        bytes_stream = io.BytesIO(data)
        image = Image.open(bytes_stream)
        img = np.asarray(image)  # 图像大小: 高度=240 像素, 宽度=320 像素, 通道数=3
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # ESP32采集的是RGB格式，要转换为BGR（opencv的格式）
        print('data received')

        results = self.classify(img)
        boxes = results.xyxy[0].numpy()  # 提取边界框坐标
        confs = results.xyxy[0][:, 4].numpy()  # 提取置信度
        classes = results.xyxy[0][:, 5].numpy().astype(int)  # 提取类别，并转换为整数类型

        for i in range(len(boxes)):
            # print('boxes[i]=', boxes[i])
            x1, y1, x2, y2 = boxes[i][0:4]  # 提取单个目标的边界框坐标, 原本没有 [0:4]
            conf = confs[i]  # 提取置信度
            cls = classes[i]  # 提取类别
            # 计算目标到相机的距离
            w = x2 - x1  # 目标的宽度
            h = y2 - y1  # 目标的高度
            z = (self.fx * w) / (2 * (x2 - self.cx))  # 使用相机内参和目标在图像中的尺寸计算距离
            distance = z / 1000  # 将单位转换为米

            self.class_ = cls
            self.distance_ = distance

            # exchange distance
            print('distance=', distance)

            # 在图像上绘制矩形边界框
            cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            self.direction = get_position(x1)
            cv2.putText(img,
                        f'{cls} {distance:.2f}m', (int(x1), int(y1 - 10)),  # {distance}
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 0, 255), 2,
                        cv2.LINE_AA)

        # transmit img data
        self.img = img

        # show img
        if self.if_show_img:
            cv2.imshow("ESP32 Capture Image", img)

            # quit loop
            if cv2.waitKey(1) == ord("q"):
                cv2.destroyAllWindows()
                return False
        return img

    def 星火(self, text, direction, stuff):

        text = f'现在{direction}前方{float(text): .1f}米处有障碍物{stuff}，一小段亲切的语音提示提醒盲人，不生成其他内容，只生成一种语音，不要包含说明性文字'
        # 调用函数并获取答案
        answer = a001_讯飞星火对话.process_input_and_get_answer(input_text=text,
                                                                # 以下密钥信息从控制台获取
                                                                appid="f1f8e784",  # 填写控制台中获取的 APPID 信息
                                                                api_key="7e0856a5d8023644862059179e2bc02c",  # 填写控制台中获取的 APIKey 信息
                                                                api_secret="NjNlY2YyOTIxZmRhNWRlOGQzMjRlZjJm",  # 填写控制台中获取的 APISecret 信息
                                                                # Spark_url = "ws://spark-api.xf-yun.com/v1.1/chat"  # v1.5环境的地址
                                                                # Spark_url = "ws://spark-api.xf-yun.com/v2.1/chat"  # v2.0环境的地址
                                                                Spark_url="ws://spark-api.xf-yun.com/v3.1/chat",  # # 云端环境的v3.0环境的服务地址
                                                                domain="generalv2")  # v2.0版本, domain = "general"   # v1.5版本 # 用于配置大模型版本，默认“general/generalv2”

        return answer

    def run(self):
        while True:
            data, _ = self.socket.recvfrom(100000)
            self.process_image(data)
            # print(self.img)

            # exchange img flowdata
            window.img = self.img
            window.page4_目标检测()

            # check if distance changed
            if self.distance_ != self.distance_temp_:
                self.distance_temp_ = self.distance_

                # voice
                voice = self.星火(abs(abs(self.distance_) * 10 + random.uniform(-0.5, 0.5)), self.direction, '障碍物')
                play_voice(voice)

            # break
            if cv2.waitKey(1) == ord("q"):
                break


# 使用示例
if __name__ == "__main__":
    # Qt_serial tools
    app = QApplication(sys.argv)
    window = SerialTools()
    window.show()

    # yolo
    detector = YOLOv5Detector(model_path=r"C:\Users\wegener/.cache\torch\hub\ultralytics_yolov5_master",
                              if_show_img=False)
    detector.run()

    # wait until download
    app.exec()
