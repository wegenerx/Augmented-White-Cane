import binascii

from PySide6.QtGui import QIcon

import ui_.resource_rc

from PySide6.QtWidgets import QMainWindow, QFileDialog, QTextBrowser
from PySide6.QtSerialPort import QSerialPortInfo, QSerialPort
from PySide6.QtCore import Slot, Signal, QByteArray, QTimer
from PySide6.QtCore import Qt

import datetime
import binascii
import cv2
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap, QImage
import matplotlib.pyplot as plt
import tempfile
import os

from ui_.ui import Ui_SerialTools
from codes.serial_model import SerialModel
from codes import a001_讯飞星火对话
from codes import a002_class_img_processor


def read_file_as_str(filepath):
    # 使用with语句打开文件，确保文件会被正确关闭
    with open(filepath, 'r', encoding='utf-8') as file:
        # 读取文件内容到字符串
        file_content = file.read()
    # print(file_content)
    return file_content


class RadarExtension(QMainWindow, Ui_SerialTools):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.img = False

        # pages
        self.page2_针对雷达的扩展功能()
        self.page3_雷达助手手册()
        self.page4_目标检测()

        # radar_param_dict
        self.radar_param_dict = {'signal_power_left': [],
                                 'signal_power_middle': [],
                                 'signal_power_right': [],
                                 'signal_distance_left': [],
                                 'signal_distance_middle': [],
                                 'signal_distance_right': [],
                                 }  # 类成员变量

    def page2_针对雷达的扩展功能(self):
        # open this folder
        self.commandLinkButton_open_folder.clicked.connect(self.打开本文件夹)
        # self..setText('wow')

        # start pdf
        self.commandLinkButton_open_guide_pdf.clicked.connect(lambda: self.startfile文件(r'ui_\C-RKB1213应用手册V1.2.pdf'))

        # open stm32 keil project
        self.commandLinkButton_open_keil_project.clicked.connect(lambda: self.打开文件夹('a001_串口收发HEX数据包_许勤智发代码后'))

        # open upper computer and lower computer
        self.pushButton_upper_computer.clicked.connect(lambda: self.打开文件夹('a002_1231上位机'))  # upper
        self.pushButton_lower_computer.clicked.connect(lambda: self.打开文件夹(r'a003_1231下位机\SGR1231\projects\MDK_ARM'))  # lower
        self.pushButton_open_upper_computer.clicked.connect(lambda: self.run_py_file(r'a002_1231上位机\rawData\rawData.py'))
        #
        # D:\Libraries\projects\python\ownproject\a023_Big innovation college students\a003_PySide6_Serial_Tools_master\

        # lineEdit change
        self.lineEdit_9.textChanged.connect(self.lineEdit_change_method_1)
        self.lineEdit_2.textChanged.connect(self.lineEdit_change_method_2)
        self.lineEdit_4.textChanged.connect(self.lineEdit_change_method_3)
        self.lineEdit_5.textChanged.connect(self.lineEdit_change_method_4)
        self.lineEdit_8.textChanged.connect(self.lineEdit_change_method_5)

        # *************** hex - dec converter *************** #
        self.lineEdit_6.textChanged.connect(self.lineEdit_change_method_dec_to_hex)
        self.lineEdit_7.textChanged.connect(self.lineEdit_change_method_hex_to_dec)

        # *************** hex - dec converter *************** #
        self.pushButton_LLM.clicked.connect(lambda: self.llm_invoke(QlineEdit=self.lineEdit_LLM,
                                                                    QpushButton=self.pushButton_LLM,
                                                                    QtextBrowser=self.textBrowser_LLM)
                                            )

    def page3_雷达助手手册(self):

        # textBrowser
        test = read_file_as_str(r'ui_/guide.txt')
        test = test.split('\n')
        for _ in test:
            self.textBrowser.append(_)

    def page4_目标检测(self):

        # todo: 如果现在有图像（其实不知道这个东西怎么跑的）
        if type(self.img) != bool:
            h, w, ch = self.img.shape
            self.img = QImage(self.img.data, w, h, ch * w, QImage.Format_RGB888)
            self.label_video.setPixmap(QPixmap.fromImage(self.img))

    def run_py_file(self, file_path):
        import subprocess
        subprocess.run(['python', file_path])

    def lineEdit_change_method_dec_to_hex(self):
        def can_convert_to_decimal(s):
            try:
                float(s)  # 尝试将字符串转换为浮点数
                return True
            except ValueError:
                return False

        text = self.lineEdit_6.text()
        if can_convert_to_decimal(text):
            text_16 = self.dec_to_hex(text)
            self.lineEdit_7.setText(text_16)

    def lineEdit_change_method_hex_to_dec(self):
        def is_hex_number(s):
            """
            判断字符串s的内容是否可以转换成16进制数
            :param s: 要检查的字符串
            :return: 如果可以转换成16进制数，则返回True；否则返回False
            """
            try:
                # 尝试将字符串解释为16进制数
                int(s, 16)
                return True
            except ValueError:
                # 如果发生ValueError异常，说明字符串不能转换成16进制数
                return False

        text = self.lineEdit_7.text()
        if is_hex_number(text):
            text_10 = self.hex_to_dec(text)
            self.lineEdit_6.setText(text_10)

    def lineEdit_change_method_1(self):
        text = self.lineEdit_9.text()
        text = text.replace(' ', '')

        if len(text) == 26:
            # define sliced value (dec & hex)
            if_exist_left = text[6:8]
            if_exist_middle = text[12:14]
            if_exist_right = text[18:20]

            # define char in lineEdit
            strength_percentage_left = text[8:10] + ', 十进制' + self.hex_to_dec(text[8:10])
            distance_left = text[10:12] + ', 十进制' + self.hex_to_dec(text[10:12])
            strength_percentage_middle = text[14:16] + ', 十进制' + self.hex_to_dec(text[14:16])
            distance_middle = text[16:18] + ', 十进制' + self.hex_to_dec(text[16:18])
            strength_percentage_right = text[20:22] + ', 十进制' + self.hex_to_dec(text[20:22])
            distance_right = text[22:24] + ', 十进制' + self.hex_to_dec(text[22:24])

            # append to paint value
            self.radar_param_dict['signal_power_left'].append(self.hex_to_dec(text[8:10]))
            self.radar_param_dict['signal_distance_left'].append(self.hex_to_dec(text[10:12]))
            self.radar_param_dict['signal_power_middle'].append(self.hex_to_dec(text[14:16]))
            self.radar_param_dict['signal_distance_middle'].append(self.hex_to_dec(text[16:18]))
            self.radar_param_dict['signal_power_right'].append(self.hex_to_dec(text[20:22]))
            self.radar_param_dict['signal_distance_right'].append(self.hex_to_dec(text[22:24]))

            # repaint
            self.show_graph_label()

            # set text
            self.lineEdit_10.setText(if_exist_left)
            self.lineEdit_11.setText(strength_percentage_left)
            self.lineEdit_12.setText(distance_left)

            self.lineEdit_15.setText(if_exist_middle)
            self.lineEdit_13.setText(strength_percentage_middle)
            self.lineEdit_14.setText(distance_middle)

            self.lineEdit_16.setText(if_exist_right)
            self.lineEdit_17.setText(strength_percentage_right)
            self.lineEdit_18.setText(distance_right)

    def lineEdit_change_method_2(self):
        text = self.lineEdit_2.text()
        text = text.replace(' ', '')

        if len(text) == 10:
            # define sliced value
            threshold = text[4:8] + ', 十进制' + self.hex_to_dec(text[4:8])

            # set text

            self.lineEdit_19.setText(threshold)

    def lineEdit_change_method_3(self):
        text = self.lineEdit_4.text()
        text = text.replace(' ', '')

        if len(text) == 14:
            # define sliced value
            threshold = text[8:10] + ', 十进制' + self.hex_to_dec(text[6:10])

            # set text
            self.lineEdit_21.setText(threshold)

    def llm_invoke(self, QlineEdit, QpushButton, QtextBrowser) -> None:
        text = QlineEdit.text()
        QtextBrowser.clear()

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
        QtextBrowser.setText(answer)
        QlineEdit.clear()

    def lineEdit_change_method_4(self):
        text = self.lineEdit_5.text()
        text = text.replace(' ', '')

        if len(text) == 10:
            # define sliced value
            angle_range = text[4:6] + ', 十进制' + self.hex_to_dec(text[4:6])

            # set text

            self.lineEdit_22.setText(angle_range)

    def lineEdit_change_method_5(self):
        text = self.lineEdit_8.text()
        text = text.replace(' ', '')

        if len(text) == 22:
            # define sliced value
            angle_range = text[6:8] + ', 十进制' + self.hex_to_dec(text[6:8])

            # set text
            self.lineEdit_23.setText(angle_range)

    def 打开文件夹(self, way):
        import os

        def open_folder(path):
            if os.path.isdir(path):
                os.startfile(path)
            else:
                print(f"Error: '{path}' is not a valid directory.")

        # 使用您提供的路径
        open_folder(way)

    def 打开本文件夹(self):
        import os

        # 获取当前脚本的绝对路径
        script_path = os.path.abspath(__file__)
        # 获取脚本所在的文件夹路径
        folder_path = os.path.dirname(script_path)

        # 使用os.startfile打开该文件夹
        os.startfile(folder_path + r'')

    @staticmethod
    def hex_to_dec(hex_str: str) -> str:
        """
        将16进制字符串转换为10进制字符串
        :param hex_str: 16进制字符串
        :return: 10进制字符串
        """
        try:
            # 使用int函数将16进制字符串转换为10进制整数，然后使用str函数转换为字符串
            return str(int(hex_str, 16))
        except ValueError:
            # 如果输入的字符串不是有效的16进制数，返回错误信息
            return "无效的16进制字符串"

    @staticmethod
    def dec_to_hex(dec_str: str) -> str:
        """
        将10进制字符串转换为16进制字符串
        :param dec_str: 10进制字符串
        :return: 16进制字符串
        """
        try:
            # 使用int函数将10进制字符串转换为10进制整数，然后使用hex函数转换为16进制字符串
            # 使用[2:]去掉前缀'0x'
            return hex(int(dec_str))[2:]
        except ValueError:
            # 如果输入的字符串不是有效的10进制数，返回错误信息
            return "无效的10进制字符串"

    def startfile文件(self, file_path):
        import os
        # 检查文件是否存在
        if os.path.exists(file_path):
            # 使用os.startfile()打开该文件
            os.startfile(file_path)
        else:
            print(f"文件 {file_path} 不存在，请检查路径是否正确。")


class SerialTools(RadarExtension):

    # init param
    signal_open_serial = Signal(tuple)
    signal_close_serial = Signal()
    signal_send_msg = Signal(QByteArray)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("串口调试工具")

        self.open_icon = QIcon(":/image/opened.png")
        self.close_icon = QIcon(":/image/closed.png")
        self.open_close.setIcon(self.close_icon)

        self.rx_count = 0
        self.tx_count = 0

        # 初始化获取计算机串口资源，并显示
        self.slot_update_ports()
        self.refresh_ports.clicked.connect(self.slot_update_ports)

        # 初始化常用波特率并显示
        baud_rate_list = [110, 300, 600, 1200, 2400, 4800, 9600]  # , 14400, 19200, 38400, 43000, 57600, 76800, 115200,128000, 230400, 256000, 460800, 921600, 1000000, 2000000, 3000000]
        self.baud_rate.addItem("自定义", 0)
        for baud_rate in baud_rate_list:
            self.baud_rate.addItem(str(baud_rate), baud_rate)
        self.baud_rate.setCurrentText("9600")

        # 初始化停止位，并显示
        stop_bits_list = ["1", "1.5", "2"]
        q_stop_bits_list = [QSerialPort.StopBits.OneStop,
                            QSerialPort.StopBits.OneAndHalfStop,
                            QSerialPort.StopBits.TwoStop]
        for stop_bits, q_stop_bits in zip(stop_bits_list, q_stop_bits_list):
            self.stop_bits.addItem(stop_bits, q_stop_bits)
        self.stop_bits.setCurrentText("1")

        # 初始化数据位，并显示
        data_bits_list = ["8", "7", "6", "5"]
        q_data_bits_list = [QSerialPort.DataBits.Data8,
                            QSerialPort.DataBits.Data7,
                            QSerialPort.DataBits.Data6,
                            QSerialPort.DataBits.Data5]
        for data_bits, q_data_bits in zip(data_bits_list, q_data_bits_list):
            self.data_bits.addItem(data_bits, q_data_bits)
        self.data_bits.setCurrentText("8")

        # 初始化校验位，并显示
        parity_list = ["None", "Odd", "Even"]
        q_parity_list = [QSerialPort.Parity.NoParity,
                         QSerialPort.Parity.OddParity,
                         QSerialPort.Parity.EvenParity]
        for parity, q_parity in zip(parity_list, q_parity_list):
            self.parity.addItem(parity, q_parity)

        self.parity.setCurrentText("None")

        # 初始化流控，并显示
        flow_control_list = ["None", "RTS/CTS", "XON/XOFF"]
        q_flow_control_list = [QSerialPort.FlowControl.NoFlowControl,
                               QSerialPort.FlowControl.HardwareControl,
                               QSerialPort.FlowControl.SoftwareControl]
        for flow_control, q_flow_control in zip(flow_control_list, q_flow_control_list):
            self.flow_control.addItem(flow_control, q_flow_control)

        self.flow_control.setCurrentText("None")

        self.open_close.clicked.connect(self.slot_open_close_serial)  # 连接信号与槽，响应打开/关闭串口按钮动作
        self.recv_clear.clicked.connect(self.slot_clear_recv_text)  # 连接信号与槽，响应清除接收按钮动作

        # ********** 编辑部分 ********** #
        # ********** 编辑部分 ********** #
        # ********** 编辑部分 ********** #
        # ********** 编辑部分 ********** #
        # ********** 编辑部分 ********** #
        self.show_graph_label()

        self.recv_clear_2.clicked.connect(self.test)

        self.single_send_bt.clicked.connect(self.slot_single_send_msg)  # 连接信号与槽，响应单条发送按钮动作
        self.single_send_clear.clicked.connect(self.slot_clear_single_send_text)  # 连接信号与槽，响应清除单条发送按钮动作
        self.single_hex_send.toggled.connect(self.slot_single_hex_input)  # 连接信号与槽，响应单条Hex输入按钮动作
        self.single_ascii_send.toggled.connect(self.slot_single_ascii_input)  # 连接信号与槽，响应单条ASCII输入按钮动作

        # 初始化单条发送定时器
        self.single_timer = QTimer()
        self.single_timer.timeout.connect(self.slot_single_send_msg)
        self.single_send_timer_enable.toggled.connect(self.slot_enable_single_timer)  # 连接信号与槽，响应单条定时发送动作

        # QCheckbox
        self.multi_enable_list = [self.multi_1_enable, self.multi_2_enable, self.multi_3_enable,
                                  self.multi_4_enable, self.multi_5_enable, self.multi_6_enable,
                                  self.multi_7_enable, self.multi_8_enable, self.multi_9_enable,
                                  self.multi_10_enable]

        self.multi_text_list = [self.multi_1_send_text, self.multi_2_send_text, self.multi_3_send_text,
                                self.multi_4_send_text, self.multi_5_send_text, self.multi_6_send_text,
                                self.multi_7_send_text, self.multi_8_send_text, self.multi_9_send_text,
                                self.multi_10_send_text,
                                # radar extension
                                self.label_69,
                                self.lineEdit_2,
                                self.label_67,
                                self.lineEdit_5,
                                self.label_71,
                                self.label_77
                                ]

        # button
        self.multi_1_send_btn.clicked.connect(self.slot_multi_send_1)
        self.multi_2_send_btn.clicked.connect(self.slot_multi_send_2)
        self.multi_3_send_btn.clicked.connect(self.slot_multi_send_3)
        self.multi_4_send_btn.clicked.connect(self.slot_multi_send_4)
        self.multi_5_send_btn.clicked.connect(self.slot_multi_send_5)
        self.multi_6_send_btn.clicked.connect(self.slot_multi_send_6)
        self.multi_7_send_btn.clicked.connect(self.slot_multi_send_7)
        self.multi_8_send_btn.clicked.connect(self.slot_multi_send_8)
        self.multi_9_send_btn.clicked.connect(self.slot_multi_send_9)
        self.multi_10_send_btn.clicked.connect(self.slot_multi_send_10)

        # radar extension
        self.pushButton.clicked.connect(self.slot_multi_send_11)
        self.pushButton_2.clicked.connect(self.slot_multi_send_12)
        self.pushButton_3.clicked.connect(self.slot_multi_send_13)
        self.pushButton_5.clicked.connect(self.slot_multi_send_14)
        self.pushButton_6.clicked.connect(self.slot_multi_send_15)
        self.pushButton_8.clicked.connect(self.slot_multi_send_16)

        self.multi_hex_send.toggled.connect(self.slot_multi_hex_input)
        self.multi_export.clicked.connect(self.slot_multi_export)
        self.multi_import.clicked.connect(self.slot_multi_import)

        # 初始化多条发送定时器
        self.multi_timer = QTimer()
        self.multi_timer.timeout.connect(self.slot_multi_send_msg)
        self.multi_send_timer_enable.toggled.connect(self.slot_enable_multi_timer)  # 连接信号与槽，响应多条定时发送动作

        # 实例化、初始化串口通讯Model
        # the SerialModel is the class defined by former .py file
        self.serial_model = SerialModel(self)
        self.serial_model.start()
        self.serial_model.signal_open_result.connect(self.slot_open_result)  # 连接信号与槽，接收连接状态
        self.serial_model.signal_send_msg.connect(self.slot_recv_msg)  # 连接信号与槽，接收读取消息内容
        self.signal_open_serial.connect(self.serial_model.open_serial)  # 连接信号与槽，发送连接命令
        self.signal_close_serial.connect(self.serial_model.close_serial)  # 连接信号与槽，发送断开连接命令
        self.signal_send_msg.connect(self.serial_model.send_msg)  # 连接信号与槽，发送发送消息命令

    # show radar figure
    def show_graph_label(self):

        # 为了使得这部分易于维护，将其封装为函数
        def plot_to_label(power: list,
                          distance: list,
                          direction: str,
                          label: QLabel):
            # 创建一个matplotlib图像
            plt.figure()

            # 设置图像的x轴和y轴的范围
            plt.xlim(0, 100)  # x轴范围从0到4
            plt.ylim(0, 8)  # y轴范围从0到8

            # plot
            plt.plot(power, label=direction + ' power')
            plt.plot(distance, label=direction + ' distance')
            plt.title(direction + ' area')
            plt.legend()  # 调用legend函数来显示图例

            # 设置图像的长宽比为2:1，首先获取当前图像的尺寸
            fig = plt.gcf()
            fig.set_size_inches(10, 3)  # 设置图像的尺寸为6x3英寸，这将创建一个2:1的长宽比

            # 保存图像到临时文件
            temp_dir = tempfile.gettempdir()
            temp_file = os.path.join(temp_dir, "temp_image.png")
            plt.savefig(temp_file)

            # 使用OpenCV读取图像
            image = cv2.imread(temp_file)

            plt.close()

            # 将图像转换为QPixmap
            height, width, channel = image.shape
            bytesPerLine = 3 * width
            q_image = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)

            # 清理临时文件
            os.remove(temp_file)

            # 获取QLabel的大小
            label_size = label.size()
            # print(label_size)

            # 调整pixmap的大小以适应QLabel的大小
            # Qt.KeepAspectRatio 保持纵横比
            scaled_pixmap = pixmap  # .scaled(label_size) # , Qt.KeepAspectRatio, Qt.SmoothTransformation)

            # 设置图像
            label.setPixmap(scaled_pixmap)
            label.setScaledContents(True)

        # plot to label
        # left
        plot_to_label(power=self.radar_param_dict['signal_power_left'],
                      distance=self.radar_param_dict['signal_distance_left'],
                      direction='left',
                      label=self.label_graph_1)

        # middle
        plot_to_label(power=self.radar_param_dict['signal_power_middle'],
                      distance=self.radar_param_dict['signal_distance_middle'],
                      direction='middle',
                      label=self.label_graph_2)
        # right
        plot_to_label(power=self.radar_param_dict['signal_power_right'],
                      distance=self.radar_param_dict['signal_distance_right'],
                      direction='right',
                      label=self.label_graph_3)

    # write data to local file
    def test(self):
        import datetime

        plain_text = self.recv_text.toPlainText()

        # 获取当前系统时间
        now = datetime.datetime.now()

        # 格式化时间字符串，用于文件名（这里使用YYYY-MM-DD_HH-MM-SS的格式）
        time_str = now.strftime("%Y-%m-%d_%H-%M-%S")

        # 构造文件名（例如：2023-03-15_14-30-00.txt）
        filename = f"{time_str}.txt"

        # 打开文件以写入内容（如果文件不存在，则创建它）
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(plain_text)

        print(f"Text written to {filename}")

    # close serial port
    def closeEvent(self, event):
        if self.serial_model.isRunning() is True:
            self.serial_model.exit()
            self.serial_model.wait()

    @Slot()
    def slot_update_ports(self):
        ports = QSerialPortInfo.availablePorts()
        for port in ports:
            self.port_select.addItem(port.portName(), port)

    @Slot(bool)
    def slot_open_result(self, result):
        if result is True:
            self.open_close.setText("关闭串口")
            self.open_close.setIcon(self.open_icon)
        else:
            self.open_close.setText("打开串口")
            self.open_close.setIcon(self.close_icon)

    @Slot(bool)
    def slot_open_close_serial(self, checked):
        if checked is True:
            self.signal_open_serial.emit((self.port_select.currentData(),
                                          self.baud_rate.currentData(),
                                          self.stop_bits.currentData(),
                                          self.data_bits.currentData(),
                                          self.parity.currentData(),
                                          self.flow_control.currentData()))
        else:
            self.signal_close_serial.emit()

    # receive
    @Slot(QByteArray)
    def slot_recv_msg(self, msg):

        print(msg)
        # 更新接收字节计数
        self.rx_count += msg.count()
        self.rx_num.setText("RX: %d" % self.rx_count)

        # 判断是否显示时间戳
        if self.recv_time_stamp.isChecked():
            self.recv_text.append(
                "<font color=\"#00FFFF\", size=\"4\">[%s]</font>" % datetime.datetime.now().strftime('%F %T'))

        # 判断是否为Hex显示
        if self.recv_hex.isChecked() is True:
            # *************** deal qByteArray ********** #
            # print(msg) # b'\x01\x02'
            # print(type(msg)) # <class 'PySide6.QtCore.QByteArray'>
            # print(str(msg)) # b'\x01\x02'
            # str1 = str(msg, encoding='ansi')
            # str1 = msg.data().decode()
            # print(msg.data().decode('ASCII', errors='ignore')) # ansi 
            # print(msg.data().decode('ansi', errors='ignore'))
            # print(msg.data().decode('UTF-8', errors='ignore'))
            # print(msg.data().decode('UTF-16', errors='ignore'))
            # print(msg.data().decode('UTF-32', errors='ignore'))
            # print(msg.data().decode('GBK', errors='ignore'))

            # *************** deal <class 'bytes'> ********** #
            msg_str_eval = eval(str(msg))

            # print(msg_str_eval) # b'\x01\x02'
            # print(type(msg_str_eval)) # <class 'bytes'>
            # to hex string
            hex_string = binascii.hexlify(msg_str_eval).decode()
            # print(type(hex_string)) # <class 'str'>

            hex_string = 'CF' + hex_string + 'EF'
            print(hex_string)

            # define code head, mode, tail
            code_head = hex_string[0:2]
            code_mode = hex_string[2:4]
            code_tail = hex_string[-2:]

            if code_mode == '10':  # 读取目标返回值 CF100B 013A08 013406 013806 A701 EF3
                self.lineEdit_9.setText(hex_string)

            elif code_mode == '11':  # 设置门限返回值 ？
                self.lineEdit_20.setText(hex_string)

            elif code_mode == '15':  # 读取门限返回值 CF1502320554EF
                self.lineEdit_4.setText(hex_string)

            elif code_mode == '13':  # 设置中区角度返回值
                self.lineEdit_24.setText(hex_string)

            elif code_mode == '12':  # 读取中区角度范围返回值 CF120B32000000001E01FF##
                self.lineEdit_8.setText(hex_string)

            elif code_mode == '14':  # 写入flash返回值#
                self.lineEdit_25.setText(hex_string)

            # 原代码
            # msg = self.__ascii_to_hex(hex_string)

            # 没 change color code
            # self.recv_text.append("%s\n" % hex_string)
            self.recv_text.append("<font color=\"#A52A2A\", size=\"4\">%s</font>" % hex_string)

            return

        # 直接显示
        self.recv_text.append("%s\n" % bytes(msg.data()).decode('utf-8'))

    @Slot()
    def slot_clear_recv_text(self):
        self.recv_text.clear()

        self.rx_count = 0
        self.rx_num.setText("RX: %d" % self.rx_count)

    @Slot()
    def slot_single_send_msg(self):
        msg = self.single_send_text.toPlainText()
        if not msg:
            return

        # 如果为16进制发送，则先转为ASCII
        if self.single_hex_send.isChecked() is True:
            msg = self.__hex_to_ascii(msg)

        self.__send_msg(msg)

    @Slot()
    def slot_clear_single_send_text(self):
        self.single_send_text.clear()

    @Slot(bool)
    def slot_enable_single_timer(self, checked):
        if checked is True:
            self.single_send__timer_cycle.setDisabled(True)
            self.single_timer.start(self.single_send__timer_cycle.value())
        else:
            self.single_send__timer_cycle.setDisabled(False)
            self.single_timer.stop()

    @Slot(bool)
    def slot_single_ascii_input(self, checked):
        if checked is True:
            hex_str = self.single_send_text.toPlainText()
            if not hex_str:
                return

            self.single_send_text.setText(self.__hex_to_ascii(hex_str))

    @Slot(bool)
    def slot_single_hex_input(self, checked):
        if checked is True:
            ascii_str = self.single_send_text.toPlainText()
            if not ascii_str:
                return

            self.single_send_text.setText(self.__ascii_to_hex(ascii_str))

    def __hex_to_ascii(self, hex_str):

        # replace blanks
        hex_str_replace_blanks = hex_str.replace(' ', '')

        # 去除空格并转换为字节串
        byte_str = binascii.unhexlify(hex_str_replace_blanks)

        # 将字节串解码为 ASCII 字符串
        ascii_str = byte_str.decode('ascii')

        return ascii_str

    def __ascii_to_hex(self, ascii_str):
        # 将 ASCII 字符串转换为字节串
        byte_str = ascii_str.encode()

        # 将字节串转换为十六进制字符串
        hex_str = byte_str.hex()

        # 每两个字符用空格分隔
        hex_list = [hex_str[i:i + 2] for i in range(0, len(hex_str), 2)]
        hex_str = ' '.join(hex_list)

        # 每 4 个字节添加一个空格，形成美化输出
        hex_str = ' '.join([hex_str[i:i + 11] for i in range(0, len(hex_str), 11)])
        return hex_str

    def __send_msg(self, msg):
        if self.open_close.isChecked() is True:
            # 更新发送字节计数
            msg = QByteArray.fromStdString(msg)
            self.tx_count += msg.count()
            self.tx_num.setText("TX: %d" % self.tx_count)

            # 通知Model发送
            self.signal_send_msg.emit(msg)

    @Slot()
    def slot_multi_send_msg(self):
        hex_enable = self.multi_hex_send.isChecked()

        for multi_enable, multi_text in zip(self.multi_enable_list, self.multi_text_list):
            if multi_enable.isChecked() is True:
                msg = multi_text.text()
                if msg:
                    # 如果为16进制发送，则先转为ASCII
                    if hex_enable is True:
                        msg = self.__hex_to_ascii(msg)

                    self.__send_msg(msg)

    @Slot(bool)
    def slot_enable_multi_timer(self, checked):
        if checked is True:
            self.multi_send_timer_cycle.setDisabled(True)
            self.multi_timer.start(self.multi_send_timer_cycle.value())
        else:
            self.multi_send_timer_cycle.setDisabled(False)
            self.multi_timer.stop()

    @Slot(bool)
    def slot_multi_hex_input(self, checked):
        if checked is True:
            for multi_text in self.multi_text_list:
                text = multi_text.text()
                if text:
                    multi_text.setText(self.__ascii_to_hex(text))
        else:
            for multi_text in self.multi_text_list:
                text = multi_text.text()
                if text:
                    multi_text.setText(self.__hex_to_ascii(text))

    @Slot()
    def slot_multi_send_1(self):
        msg = self.multi_1_send_text.text()
        if not msg:
            return

        # 如果为16进制发送，则先转为ASCII
        if self.multi_hex_send.isChecked() is True:
            msg = self.__hex_to_ascii(msg)

        self.__send_msg(msg)

    @Slot()
    def slot_multi_send_2(self):
        msg = self.multi_2_send_text.text()
        if not msg:
            return

        # 如果为16进制发送，则先转为ASCII
        if self.multi_hex_send.isChecked() is True:
            msg = self.__hex_to_ascii(msg)

        self.__send_msg(msg)

    @Slot()
    def slot_multi_send_3(self):
        msg = self.multi_3_send_text.text()
        if not msg:
            return

        # 如果为16进制发送，则先转为ASCII
        if self.multi_hex_send.isChecked() is True:
            msg = self.__hex_to_ascii(msg)

        self.__send_msg(msg)

    @Slot()
    def slot_multi_send_4(self):
        msg = self.multi_4_send_text.text()
        if not msg:
            return

        # 如果为16进制发送，则先转为ASCII
        if self.multi_hex_send.isChecked() is True:
            msg = self.__hex_to_ascii(msg)

        self.__send_msg(msg)

    @Slot()
    def slot_multi_send_5(self):
        msg = self.multi_5_send_text.text()
        if not msg:
            return

        # 如果为16进制发送，则先转为ASCII
        if self.multi_hex_send.isChecked() is True:
            msg = self.__hex_to_ascii(msg)

        self.__send_msg(msg)

    @Slot()
    def slot_multi_send_6(self):
        msg = self.multi_6_send_text.text()
        if not msg:
            return

        # 如果为16进制发送，则先转为ASCII
        if self.multi_hex_send.isChecked() is True:
            msg = self.__hex_to_ascii(msg)

        self.__send_msg(msg)

    @Slot()
    def slot_multi_send_7(self):
        msg = self.multi_7_send_text.text()
        if not msg:
            return

        # 如果为16进制发送，则先转为ASCII
        if self.multi_hex_send.isChecked() is True:
            msg = self.__hex_to_ascii(msg)

        self.__send_msg(msg)

    @Slot()
    def slot_multi_send_8(self):
        msg = self.multi_8_send_text.text()
        if not msg:
            return

        # 如果为16进制发送，则先转为ASCII
        if self.multi_hex_send.isChecked() is True:
            msg = self.__hex_to_ascii(msg)

        self.__send_msg(msg)

    @Slot()
    def slot_multi_send_9(self):
        msg = self.multi_9_send_text.text()
        if not msg:
            return

        # 如果为16进制发送，则先转为ASCII
        if self.multi_hex_send.isChecked() is True:
            msg = self.__hex_to_ascii(msg)

        self.__send_msg(msg)

    @Slot()
    def slot_multi_send_10(self):

        msg = self.label_69.text()
        if not msg:
            return

        # 如果为16进制发送，则先转为ASCII
        if self.multi_hex_send.isChecked() is True:
            msg = self.__hex_to_ascii(msg)

        self.__send_msg(msg)

    # radar extension
    @Slot()
    def slot_multi_send_11(self):
        msg = self.label_69.text()
        if not msg:
            return

        # 如果为16进制发送，则先转为ASCII
        if self.multi_hex_send.isChecked() is True:
            msg = self.__hex_to_ascii(msg)

        self.__send_msg(msg)

    def slot_multi_send_12(self):
        msg = self.lineEdit_2.text()
        if not msg:
            return

        # 如果为16进制发送，则先转为ASCII
        if self.multi_hex_send.isChecked() is True:
            msg = self.__hex_to_ascii(msg)

        self.__send_msg(msg)

    def slot_multi_send_13(self):
        msg = self.label_67.text()
        if not msg:
            return

        # 如果为16进制发送，则先转为ASCII
        if self.multi_hex_send.isChecked() is True:
            msg = self.__hex_to_ascii(msg)

        self.__send_msg(msg)

    def slot_multi_send_14(self):
        msg = self.lineEdit_5.text()
        if not msg:
            return

        # 如果为16进制发送，则先转为ASCII
        if self.multi_hex_send.isChecked() is True:
            msg = self.__hex_to_ascii(msg)

        self.__send_msg(msg)

    def slot_multi_send_15(self):
        msg = self.label_71.text()
        if not msg:
            return

        # 如果为16进制发送，则先转为ASCII
        if self.multi_hex_send.isChecked() is True:
            msg = self.__hex_to_ascii(msg)

        self.__send_msg(msg)

    def slot_multi_send_16(self):
        msg = self.label_77.text()
        if not msg:
            return

        # 如果为16进制发送，则先转为ASCII
        if self.multi_hex_send.isChecked() is True:
            msg = self.__hex_to_ascii(msg)

        self.__send_msg(msg)

    # ------------------------------ end radar extension ------------------------------ #

    @Slot()
    def slot_multi_export(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'Text Files (*.txt)')
        if file_name:
            with open(file_name, 'w') as f:
                item_list = []
                for multi_enable, multi_text in zip(self.multi_enable_list, self.multi_text_list):
                    item_list.append(','.join([str(multi_enable.isChecked()), multi_text.text()]))

                f.write('\n'.join(item_list))

    @Slot()
    def slot_multi_import(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Save File', '', 'Text Files (*.txt)')
        if file_name:
            with open(file_name, 'r') as f:
                item_list = f.read()
                item_list = item_list.split('\n')
                for item, multi_enable, multi_text in zip(item_list, self.multi_enable_list, self.multi_text_list):
                    item = item.split(',')
                    print(item)
                    multi_enable.setChecked(True if (item[0] == 'True') else False)
                    multi_text.setText(item[1])
