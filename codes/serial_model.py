from PySide6.QtCore import QThread, QIODeviceBase, Slot, Signal, QByteArray
from PySide6.QtSerialPort import QSerialPort


# 定义了一个名为 SerialModel 的类，它继承自 QThread，使得 SerialModel 可以作为一个线程运
class SerialModel(QThread):
    signal_open_result = Signal(bool)       # if get data success
    signal_send_msg = Signal(QByteArray)    # bring serial rx data

    def __init__(self, caller):
        super().__init__()

        # init QSerialPort
        self.m_serial = QSerialPort()
        self.m_serial.readyRead.connect(self.read_msg)  # connect read_msg to QSerialPort instance

    # 对串口号等进行选择, para 是一个携带多个参数的列表
    @Slot(tuple)
    def open_serial(self, para):
        self.m_serial.setPort(para[0])      # which port
        self.m_serial.setBaudRate(para[1])  # baud
        self.m_serial.setStopBits(para[2])  # stopbits
        self.m_serial.setDataBits(para[3])  # num of data bit
        self.m_serial.setParity(para[4])    # 校验位
        self.m_serial.setFlowControl(para[5])   # type of flow

        # 通知界面连接结果, convey bool value
        self.signal_open_result.emit(self.m_serial.open(QIODeviceBase.ReadWrite))

    # 关闭串口
    @Slot()
    def close_serial(self):
        if self.m_serial.isOpen() is True:
            self.m_serial.close()
            self.signal_open_result.emit(False) # emit false signal

    # 发送信息 send message TX
    @Slot(QByteArray)
    def send_msg(self, msg: QByteArray):
        if self.m_serial.isOpen() is True:
            self.m_serial.write(msg)

    # RX **imp
    @Slot()
    def read_msg(self):
        text = self.m_serial.readAll()
        if text.isEmpty() is False:
            self.signal_send_msg.emit(text)
