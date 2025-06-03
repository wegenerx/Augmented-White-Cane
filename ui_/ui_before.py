# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QComboBox,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)
import ui_.resource_rc

class Ui_SerialTools(object):
    def setupUi(self, SerialTools):
        if not SerialTools.objectName():
            SerialTools.setObjectName(u"SerialTools")
        SerialTools.resize(900, 631)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SerialTools.sizePolicy().hasHeightForWidth())
        SerialTools.setSizePolicy(sizePolicy)
        SerialTools.setMinimumSize(QSize(900, 590))
        SerialTools.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(SerialTools)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout_2 = QFormLayout(self.centralwidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.serial_group = QGroupBox(self.centralwidget)
        self.serial_group.setObjectName(u"serial_group")
        sizePolicy.setHeightForWidth(self.serial_group.sizePolicy().hasHeightForWidth())
        self.serial_group.setSizePolicy(sizePolicy)
        self.serial_group.setMinimumSize(QSize(180, 233))
        self.gridLayout_2 = QGridLayout(self.serial_group)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.serial_group)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(50, 16))
        self.label.setMaximumSize(QSize(50, 16))

        self.horizontalLayout.addWidget(self.label)

        self.port_select = QComboBox(self.serial_group)
        self.port_select.setObjectName(u"port_select")
        sizePolicy.setHeightForWidth(self.port_select.sizePolicy().hasHeightForWidth())
        self.port_select.setSizePolicy(sizePolicy)
        self.port_select.setMinimumSize(QSize(100, 22))
        self.port_select.setMaximumSize(QSize(100, 22))

        self.horizontalLayout.addWidget(self.port_select)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.serial_group)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(50, 16))
        self.label_2.setMaximumSize(QSize(50, 16))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.baud_rate = QComboBox(self.serial_group)
        self.baud_rate.setObjectName(u"baud_rate")
        sizePolicy.setHeightForWidth(self.baud_rate.sizePolicy().hasHeightForWidth())
        self.baud_rate.setSizePolicy(sizePolicy)
        self.baud_rate.setMinimumSize(QSize(100, 22))
        self.baud_rate.setMaximumSize(QSize(100, 22))

        self.horizontalLayout_2.addWidget(self.baud_rate)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.serial_group)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(50, 16))
        self.label_3.setMaximumSize(QSize(50, 16))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.stop_bits = QComboBox(self.serial_group)
        self.stop_bits.setObjectName(u"stop_bits")
        sizePolicy.setHeightForWidth(self.stop_bits.sizePolicy().hasHeightForWidth())
        self.stop_bits.setSizePolicy(sizePolicy)
        self.stop_bits.setMinimumSize(QSize(100, 22))
        self.stop_bits.setMaximumSize(QSize(100, 22))

        self.horizontalLayout_3.addWidget(self.stop_bits)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.serial_group)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(50, 16))
        self.label_4.setMaximumSize(QSize(50, 16))

        self.horizontalLayout_4.addWidget(self.label_4)

        self.data_bits = QComboBox(self.serial_group)
        self.data_bits.setObjectName(u"data_bits")
        sizePolicy.setHeightForWidth(self.data_bits.sizePolicy().hasHeightForWidth())
        self.data_bits.setSizePolicy(sizePolicy)
        self.data_bits.setMinimumSize(QSize(100, 22))
        self.data_bits.setMaximumSize(QSize(100, 22))

        self.horizontalLayout_4.addWidget(self.data_bits)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.serial_group)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(50, 16))
        self.label_5.setMaximumSize(QSize(50, 16))

        self.horizontalLayout_5.addWidget(self.label_5)

        self.parity = QComboBox(self.serial_group)
        self.parity.setObjectName(u"parity")
        sizePolicy.setHeightForWidth(self.parity.sizePolicy().hasHeightForWidth())
        self.parity.setSizePolicy(sizePolicy)
        self.parity.setMinimumSize(QSize(100, 22))
        self.parity.setMaximumSize(QSize(100, 22))

        self.horizontalLayout_5.addWidget(self.parity)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_10 = QLabel(self.serial_group)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QSize(50, 16))
        self.label_10.setMaximumSize(QSize(50, 16))

        self.horizontalLayout_9.addWidget(self.label_10)

        self.flow_control = QComboBox(self.serial_group)
        self.flow_control.setObjectName(u"flow_control")
        sizePolicy.setHeightForWidth(self.flow_control.sizePolicy().hasHeightForWidth())
        self.flow_control.setSizePolicy(sizePolicy)
        self.flow_control.setMinimumSize(QSize(100, 22))
        self.flow_control.setMaximumSize(QSize(100, 22))

        self.horizontalLayout_9.addWidget(self.flow_control)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.open_close = QPushButton(self.serial_group)
        self.open_close.setObjectName(u"open_close")
        sizePolicy.setHeightForWidth(self.open_close.sizePolicy().hasHeightForWidth())
        self.open_close.setSizePolicy(sizePolicy)
        self.open_close.setMinimumSize(QSize(158, 24))
        self.open_close.setMaximumSize(QSize(158, 24))
        icon = QIcon()
        icon.addFile(u":/image/closed.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/image/opened.png", QSize(), QIcon.Normal, QIcon.On)
        self.open_close.setIcon(icon)
        self.open_close.setCheckable(True)
        self.open_close.setChecked(False)

        self.verticalLayout.addWidget(self.open_close)

        self.refresh_ports = QPushButton(self.serial_group)
        self.refresh_ports.setObjectName(u"refresh_ports")
        sizePolicy.setHeightForWidth(self.refresh_ports.sizePolicy().hasHeightForWidth())
        self.refresh_ports.setSizePolicy(sizePolicy)
        self.refresh_ports.setMinimumSize(QSize(158, 24))
        self.refresh_ports.setMaximumSize(QSize(158, 24))
        self.refresh_ports.setCheckable(True)
        self.refresh_ports.setChecked(False)

        self.verticalLayout.addWidget(self.refresh_ports)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.serial_group)

        self.group_send = QGroupBox(self.centralwidget)
        self.group_send.setObjectName(u"group_send")
        sizePolicy.setHeightForWidth(self.group_send.sizePolicy().hasHeightForWidth())
        self.group_send.setSizePolicy(sizePolicy)
        self.group_send.setMinimumSize(QSize(180, 87))
        self.verticalLayout_2 = QVBoxLayout(self.group_send)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.recv_ascii = QCheckBox(self.group_send)
        self.buttonGroup = QButtonGroup(SerialTools)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.recv_ascii)
        self.recv_ascii.setObjectName(u"recv_ascii")
        sizePolicy.setHeightForWidth(self.recv_ascii.sizePolicy().hasHeightForWidth())
        self.recv_ascii.setSizePolicy(sizePolicy)
        self.recv_ascii.setChecked(True)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.recv_ascii)

        self.recv_hex = QCheckBox(self.group_send)
        self.buttonGroup.addButton(self.recv_hex)
        self.recv_hex.setObjectName(u"recv_hex")
        sizePolicy.setHeightForWidth(self.recv_hex.sizePolicy().hasHeightForWidth())
        self.recv_hex.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.recv_hex)

        self.recv_time_stamp = QCheckBox(self.group_send)
        self.recv_time_stamp.setObjectName(u"recv_time_stamp")
        sizePolicy.setHeightForWidth(self.recv_time_stamp.sizePolicy().hasHeightForWidth())
        self.recv_time_stamp.setSizePolicy(sizePolicy)
        self.recv_time_stamp.setChecked(True)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.recv_time_stamp)

        self.recv_clear = QPushButton(self.group_send)
        self.recv_clear.setObjectName(u"recv_clear")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.recv_clear)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.verticalLayout_5.addWidget(self.group_send)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)


        self.formLayout_2.setLayout(0, QFormLayout.LabelRole, self.verticalLayout_5)

        self.recv_text = QTextEdit(self.centralwidget)
        self.recv_text.setObjectName(u"recv_text")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.recv_text.sizePolicy().hasHeightForWidth())
        self.recv_text.setSizePolicy(sizePolicy1)
        self.recv_text.setMinimumSize(QSize(690, 370))
        self.recv_text.setReadOnly(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.recv_text)

        self.tab = QTabWidget(self.centralwidget)
        self.tab.setObjectName(u"tab")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy2)
        self.tab.setMinimumSize(QSize(880, 180))
        self.tab.setMaximumSize(QSize(16777215, 180))
        self.tab_single = QWidget()
        self.tab_single.setObjectName(u"tab_single")
        self.horizontalLayout_22 = QHBoxLayout(self.tab_single)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.single_send_text = QTextEdit(self.tab_single)
        self.single_send_text.setObjectName(u"single_send_text")
        sizePolicy2.setHeightForWidth(self.single_send_text.sizePolicy().hasHeightForWidth())
        self.single_send_text.setSizePolicy(sizePolicy2)
        self.single_send_text.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_6.addWidget(self.single_send_text)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.single_send_bt = QPushButton(self.tab_single)
        self.single_send_bt.setObjectName(u"single_send_bt")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.single_send_bt.sizePolicy().hasHeightForWidth())
        self.single_send_bt.setSizePolicy(sizePolicy3)
        self.single_send_bt.setMinimumSize(QSize(0, 0))
        self.single_send_bt.setMouseTracking(False)
        self.single_send_bt.setLayoutDirection(Qt.LeftToRight)
        self.single_send_bt.setAutoFillBackground(False)

        self.verticalLayout_3.addWidget(self.single_send_bt)

        self.single_send_clear = QPushButton(self.tab_single)
        self.single_send_clear.setObjectName(u"single_send_clear")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.single_send_clear.sizePolicy().hasHeightForWidth())
        self.single_send_clear.setSizePolicy(sizePolicy4)
        self.single_send_clear.setMinimumSize(QSize(0, 0))

        self.verticalLayout_3.addWidget(self.single_send_clear)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.single_send_timer_enable = QCheckBox(self.tab_single)
        self.single_send_timer_enable.setObjectName(u"single_send_timer_enable")
        sizePolicy3.setHeightForWidth(self.single_send_timer_enable.sizePolicy().hasHeightForWidth())
        self.single_send_timer_enable.setSizePolicy(sizePolicy3)

        self.horizontalLayout_8.addWidget(self.single_send_timer_enable)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.tab_single)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.label_6)

        self.single_send__timer_cycle = QSpinBox(self.tab_single)
        self.single_send__timer_cycle.setObjectName(u"single_send__timer_cycle")
        sizePolicy3.setHeightForWidth(self.single_send__timer_cycle.sizePolicy().hasHeightForWidth())
        self.single_send__timer_cycle.setSizePolicy(sizePolicy3)
        self.single_send__timer_cycle.setMinimumSize(QSize(0, 0))
        self.single_send__timer_cycle.setMaximum(16777215)
        self.single_send__timer_cycle.setValue(1000)

        self.horizontalLayout_7.addWidget(self.single_send__timer_cycle)

        self.label_7 = QLabel(self.tab_single)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.label_7)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)

        self.line = QFrame(self.tab_single)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line)

        self.single_ascii_send = QCheckBox(self.tab_single)
        self.buttonGroup_2 = QButtonGroup(SerialTools)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.single_ascii_send)
        self.single_ascii_send.setObjectName(u"single_ascii_send")
        sizePolicy3.setHeightForWidth(self.single_ascii_send.sizePolicy().hasHeightForWidth())
        self.single_ascii_send.setSizePolicy(sizePolicy3)
        self.single_ascii_send.setChecked(True)

        self.horizontalLayout_8.addWidget(self.single_ascii_send)

        self.single_hex_send = QCheckBox(self.tab_single)
        self.buttonGroup_2.addButton(self.single_hex_send)
        self.single_hex_send.setObjectName(u"single_hex_send")
        sizePolicy3.setHeightForWidth(self.single_hex_send.sizePolicy().hasHeightForWidth())
        self.single_hex_send.setSizePolicy(sizePolicy3)

        self.horizontalLayout_8.addWidget(self.single_hex_send)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_22.addLayout(self.verticalLayout_4)

        self.tab.addTab(self.tab_single, "")
        self.tab_multi = QWidget()
        self.tab_multi.setObjectName(u"tab_multi")
        self.horizontalLayout_24 = QHBoxLayout(self.tab_multi)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.multi_1_enable = QCheckBox(self.tab_multi)
        self.multi_1_enable.setObjectName(u"multi_1_enable")

        self.horizontalLayout_10.addWidget(self.multi_1_enable)

        self.multi_1_send_text = QLineEdit(self.tab_multi)
        self.multi_1_send_text.setObjectName(u"multi_1_send_text")

        self.horizontalLayout_10.addWidget(self.multi_1_send_text)

        self.multi_1_send_btn = QPushButton(self.tab_multi)
        self.multi_1_send_btn.setObjectName(u"multi_1_send_btn")

        self.horizontalLayout_10.addWidget(self.multi_1_send_btn)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.multi_2_enable = QCheckBox(self.tab_multi)
        self.multi_2_enable.setObjectName(u"multi_2_enable")

        self.horizontalLayout_11.addWidget(self.multi_2_enable)

        self.multi_2_send_text = QLineEdit(self.tab_multi)
        self.multi_2_send_text.setObjectName(u"multi_2_send_text")

        self.horizontalLayout_11.addWidget(self.multi_2_send_text)

        self.multi_2_send_btn = QPushButton(self.tab_multi)
        self.multi_2_send_btn.setObjectName(u"multi_2_send_btn")

        self.horizontalLayout_11.addWidget(self.multi_2_send_btn)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.multi_3_enable = QCheckBox(self.tab_multi)
        self.multi_3_enable.setObjectName(u"multi_3_enable")

        self.horizontalLayout_12.addWidget(self.multi_3_enable)

        self.multi_3_send_text = QLineEdit(self.tab_multi)
        self.multi_3_send_text.setObjectName(u"multi_3_send_text")

        self.horizontalLayout_12.addWidget(self.multi_3_send_text)

        self.multi_3_send_btn = QPushButton(self.tab_multi)
        self.multi_3_send_btn.setObjectName(u"multi_3_send_btn")

        self.horizontalLayout_12.addWidget(self.multi_3_send_btn)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.multi_4_enable = QCheckBox(self.tab_multi)
        self.multi_4_enable.setObjectName(u"multi_4_enable")

        self.horizontalLayout_13.addWidget(self.multi_4_enable)

        self.multi_4_send_text = QLineEdit(self.tab_multi)
        self.multi_4_send_text.setObjectName(u"multi_4_send_text")

        self.horizontalLayout_13.addWidget(self.multi_4_send_text)

        self.multi_4_send_btn = QPushButton(self.tab_multi)
        self.multi_4_send_btn.setObjectName(u"multi_4_send_btn")

        self.horizontalLayout_13.addWidget(self.multi_4_send_btn)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.multi_5_enable = QCheckBox(self.tab_multi)
        self.multi_5_enable.setObjectName(u"multi_5_enable")

        self.horizontalLayout_14.addWidget(self.multi_5_enable)

        self.multi_5_send_text = QLineEdit(self.tab_multi)
        self.multi_5_send_text.setObjectName(u"multi_5_send_text")

        self.horizontalLayout_14.addWidget(self.multi_5_send_text)

        self.multi_5_send_btn = QPushButton(self.tab_multi)
        self.multi_5_send_btn.setObjectName(u"multi_5_send_btn")

        self.horizontalLayout_14.addWidget(self.multi_5_send_btn)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_20.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.multi_6_enable = QCheckBox(self.tab_multi)
        self.multi_6_enable.setObjectName(u"multi_6_enable")

        self.horizontalLayout_15.addWidget(self.multi_6_enable)

        self.multi_6_send_text = QLineEdit(self.tab_multi)
        self.multi_6_send_text.setObjectName(u"multi_6_send_text")

        self.horizontalLayout_15.addWidget(self.multi_6_send_text)

        self.multi_6_send_btn = QPushButton(self.tab_multi)
        self.multi_6_send_btn.setObjectName(u"multi_6_send_btn")

        self.horizontalLayout_15.addWidget(self.multi_6_send_btn)


        self.verticalLayout_7.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.multi_7_enable = QCheckBox(self.tab_multi)
        self.multi_7_enable.setObjectName(u"multi_7_enable")

        self.horizontalLayout_16.addWidget(self.multi_7_enable)

        self.multi_7_send_text = QLineEdit(self.tab_multi)
        self.multi_7_send_text.setObjectName(u"multi_7_send_text")

        self.horizontalLayout_16.addWidget(self.multi_7_send_text)

        self.multi_7_send_btn = QPushButton(self.tab_multi)
        self.multi_7_send_btn.setObjectName(u"multi_7_send_btn")

        self.horizontalLayout_16.addWidget(self.multi_7_send_btn)


        self.verticalLayout_7.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.multi_8_enable = QCheckBox(self.tab_multi)
        self.multi_8_enable.setObjectName(u"multi_8_enable")

        self.horizontalLayout_17.addWidget(self.multi_8_enable)

        self.multi_8_send_text = QLineEdit(self.tab_multi)
        self.multi_8_send_text.setObjectName(u"multi_8_send_text")

        self.horizontalLayout_17.addWidget(self.multi_8_send_text)

        self.multi_8_send_btn = QPushButton(self.tab_multi)
        self.multi_8_send_btn.setObjectName(u"multi_8_send_btn")

        self.horizontalLayout_17.addWidget(self.multi_8_send_btn)


        self.verticalLayout_7.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.multi_9_enable = QCheckBox(self.tab_multi)
        self.multi_9_enable.setObjectName(u"multi_9_enable")

        self.horizontalLayout_18.addWidget(self.multi_9_enable)

        self.multi_9_send_text = QLineEdit(self.tab_multi)
        self.multi_9_send_text.setObjectName(u"multi_9_send_text")

        self.horizontalLayout_18.addWidget(self.multi_9_send_text)

        self.multi_9_send_btn = QPushButton(self.tab_multi)
        self.multi_9_send_btn.setObjectName(u"multi_9_send_btn")

        self.horizontalLayout_18.addWidget(self.multi_9_send_btn)


        self.verticalLayout_7.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.multi_10_enable = QCheckBox(self.tab_multi)
        self.multi_10_enable.setObjectName(u"multi_10_enable")

        self.horizontalLayout_19.addWidget(self.multi_10_enable)

        self.multi_10_send_text = QLineEdit(self.tab_multi)
        self.multi_10_send_text.setObjectName(u"multi_10_send_text")

        self.horizontalLayout_19.addWidget(self.multi_10_send_text)

        self.multi_10_send_btn = QPushButton(self.tab_multi)
        self.multi_10_send_btn.setObjectName(u"multi_10_send_btn")

        self.horizontalLayout_19.addWidget(self.multi_10_send_btn)


        self.verticalLayout_7.addLayout(self.horizontalLayout_19)


        self.horizontalLayout_20.addLayout(self.verticalLayout_7)


        self.horizontalLayout_23.addLayout(self.horizontalLayout_20)

        self.line_2 = QFrame(self.tab_multi)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_23.addWidget(self.line_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.multi_hex_send = QCheckBox(self.tab_multi)
        self.multi_hex_send.setObjectName(u"multi_hex_send")
        sizePolicy3.setHeightForWidth(self.multi_hex_send.sizePolicy().hasHeightForWidth())
        self.multi_hex_send.setSizePolicy(sizePolicy3)

        self.verticalLayout_8.addWidget(self.multi_hex_send)

        self.multi_send_timer_enable = QCheckBox(self.tab_multi)
        self.multi_send_timer_enable.setObjectName(u"multi_send_timer_enable")
        sizePolicy3.setHeightForWidth(self.multi_send_timer_enable.sizePolicy().hasHeightForWidth())
        self.multi_send_timer_enable.setSizePolicy(sizePolicy3)

        self.verticalLayout_8.addWidget(self.multi_send_timer_enable)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_8 = QLabel(self.tab_multi)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)

        self.horizontalLayout_21.addWidget(self.label_8)

        self.multi_send_timer_cycle = QSpinBox(self.tab_multi)
        self.multi_send_timer_cycle.setObjectName(u"multi_send_timer_cycle")
        sizePolicy3.setHeightForWidth(self.multi_send_timer_cycle.sizePolicy().hasHeightForWidth())
        self.multi_send_timer_cycle.setSizePolicy(sizePolicy3)
        self.multi_send_timer_cycle.setMinimumSize(QSize(0, 0))
        self.multi_send_timer_cycle.setMaximum(16777215)
        self.multi_send_timer_cycle.setValue(1000)

        self.horizontalLayout_21.addWidget(self.multi_send_timer_cycle)

        self.label_9 = QLabel(self.tab_multi)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)

        self.horizontalLayout_21.addWidget(self.label_9)


        self.verticalLayout_8.addLayout(self.horizontalLayout_21)

        self.multi_export = QPushButton(self.tab_multi)
        self.multi_export.setObjectName(u"multi_export")

        self.verticalLayout_8.addWidget(self.multi_export)

        self.multi_import = QPushButton(self.tab_multi)
        self.multi_import.setObjectName(u"multi_import")

        self.verticalLayout_8.addWidget(self.multi_import)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)


        self.horizontalLayout_23.addLayout(self.verticalLayout_8)


        self.horizontalLayout_24.addLayout(self.horizontalLayout_23)

        self.tab.addTab(self.tab_multi, "")

        self.formLayout_2.setWidget(1, QFormLayout.SpanningRole, self.tab)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.tx_num = QLabel(self.centralwidget)
        self.tx_num.setObjectName(u"tx_num")
        sizePolicy.setHeightForWidth(self.tx_num.sizePolicy().hasHeightForWidth())
        self.tx_num.setSizePolicy(sizePolicy)
        self.tx_num.setMinimumSize(QSize(100, 0))
        self.tx_num.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_25.addWidget(self.tx_num)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_25.addWidget(self.line_3)

        self.rx_num = QLabel(self.centralwidget)
        self.rx_num.setObjectName(u"rx_num")
        sizePolicy.setHeightForWidth(self.rx_num.sizePolicy().hasHeightForWidth())
        self.rx_num.setSizePolicy(sizePolicy)
        self.rx_num.setMinimumSize(QSize(100, 0))
        self.rx_num.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_25.addWidget(self.rx_num)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_25.addWidget(self.line_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_2)


        self.formLayout_2.setLayout(2, QFormLayout.SpanningRole, self.horizontalLayout_25)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.formLayout_2.setWidget(3, QFormLayout.SpanningRole, self.line_5)

        SerialTools.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(SerialTools)
        self.statusBar.setObjectName(u"statusBar")
        SerialTools.setStatusBar(self.statusBar)

        self.retranslateUi(SerialTools)

        self.tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SerialTools)
    # setupUi

    def retranslateUi(self, SerialTools):
        SerialTools.setWindowTitle(QCoreApplication.translate("SerialTools", u"MainWindow", None))
        self.serial_group.setTitle(QCoreApplication.translate("SerialTools", u"\u4e32\u53e3\u914d\u7f6e", None))
        self.label.setText(QCoreApplication.translate("SerialTools", u"\u4e32\u53e3\u9009\u62e9", None))
#if QT_CONFIG(statustip)
        self.port_select.setStatusTip(QCoreApplication.translate("SerialTools", u"\u9009\u62e9\u4e32\u53e3\u53f7\u3002", None))
#endif // QT_CONFIG(statustip)
        self.label_2.setText(QCoreApplication.translate("SerialTools", u"\u6ce2\u7279\u7387", None))
#if QT_CONFIG(statustip)
        self.baud_rate.setStatusTip(QCoreApplication.translate("SerialTools", u"\u914d\u7f6e\u4e32\u53e3\u901a\u4fe1\u6ce2\u7279\u7387\u3002", None))
#endif // QT_CONFIG(statustip)
        self.label_3.setText(QCoreApplication.translate("SerialTools", u"\u505c\u6b62\u4f4d", None))
#if QT_CONFIG(statustip)
        self.stop_bits.setStatusTip(QCoreApplication.translate("SerialTools", u"\u914d\u7f6e\u4e32\u53e3\u901a\u4fe1\u505c\u6b62\u4f4d\u3002", None))
#endif // QT_CONFIG(statustip)
        self.label_4.setText(QCoreApplication.translate("SerialTools", u"\u6570\u636e\u4f4d", None))
#if QT_CONFIG(statustip)
        self.data_bits.setStatusTip(QCoreApplication.translate("SerialTools", u"\u914d\u7f6e\u4e32\u53e3\u901a\u4fe1\u6570\u636e\u4f4d\u3002", None))
#endif // QT_CONFIG(statustip)
        self.label_5.setText(QCoreApplication.translate("SerialTools", u"\u6821\u9a8c\u4f4d", None))
#if QT_CONFIG(statustip)
        self.parity.setStatusTip(QCoreApplication.translate("SerialTools", u"\u914d\u7f6e\u4e32\u53e3\u901a\u4fe1\u6821\u9a8c\u4f4d\u3002", None))
#endif // QT_CONFIG(statustip)
        self.label_10.setText(QCoreApplication.translate("SerialTools", u"\u6d41\u63a7", None))
#if QT_CONFIG(statustip)
        self.flow_control.setStatusTip(QCoreApplication.translate("SerialTools", u"\u914d\u7f6e\u4e32\u53e3\u901a\u4fe1\u6821\u9a8c\u4f4d\u3002", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.open_close.setStatusTip(QCoreApplication.translate("SerialTools", u"\u6253\u5f00/\u5173\u95ed\u4e32\u53e3\u8fde\u63a5\u3002", None))
#endif // QT_CONFIG(statustip)
        self.open_close.setText(QCoreApplication.translate("SerialTools", u"\u6253\u5f00\u4e32\u53e3", None))
#if QT_CONFIG(statustip)
        self.refresh_ports.setStatusTip(QCoreApplication.translate("SerialTools", u"\u6253\u5f00/\u5173\u95ed\u4e32\u53e3\u8fde\u63a5\u3002", None))
#endif // QT_CONFIG(statustip)
        self.refresh_ports.setText(QCoreApplication.translate("SerialTools", u"\u5237\u65b0\u4e32\u53e3", None))
        self.group_send.setTitle(QCoreApplication.translate("SerialTools", u"\u63a5\u6536\u914d\u7f6e", None))
#if QT_CONFIG(statustip)
        self.recv_ascii.setStatusTip(QCoreApplication.translate("SerialTools", u"\u4ee5ASCII\u663e\u793a\u63a5\u6536\u5185\u5bb9\u3002", None))
#endif // QT_CONFIG(statustip)
        self.recv_ascii.setText(QCoreApplication.translate("SerialTools", u"ASCII\u663e\u793a", None))
#if QT_CONFIG(statustip)
        self.recv_hex.setStatusTip(QCoreApplication.translate("SerialTools", u"\u4ee5Hex\u663e\u793a\u63a5\u6536\u5185\u5bb9\u3002", None))
#endif // QT_CONFIG(statustip)
        self.recv_hex.setText(QCoreApplication.translate("SerialTools", u"Hex\u663e\u793a", None))
#if QT_CONFIG(statustip)
        self.recv_time_stamp.setStatusTip(QCoreApplication.translate("SerialTools", u"\u63a5\u6536\u6d88\u606f\u662f\u5426\u663e\u793a\u65f6\u95f4\u6233\u3002", None))
#endif // QT_CONFIG(statustip)
        self.recv_time_stamp.setText(QCoreApplication.translate("SerialTools", u"\u65f6\u95f4\u6233", None))
#if QT_CONFIG(statustip)
        self.recv_clear.setStatusTip(QCoreApplication.translate("SerialTools", u"\u6e05\u7a7a\u5df2\u63a5\u6536\u6d88\u606f\u663e\u793a\u3002", None))
#endif // QT_CONFIG(statustip)
        self.recv_clear.setText(QCoreApplication.translate("SerialTools", u"\u6e05\u9664\u63a5\u6536", None))
#if QT_CONFIG(statustip)
        self.recv_text.setStatusTip(QCoreApplication.translate("SerialTools", u"\u6d88\u606f\u63a5\u6536\u663e\u793a\u3002", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.single_send_text.setStatusTip(QCoreApplication.translate("SerialTools", u"\u5355\u6311\u6d88\u606f\u53d1\u9001\uff0c\u6d88\u606f\u8f93\u5165\u6846\u3002", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.single_send_bt.setStatusTip(QCoreApplication.translate("SerialTools", u"\u5355\u6761\u6d88\u606f\u53d1\u9001\uff0c\u53d1\u9001\u6309\u94ae\u3002\u70b9\u51fb\u4e00\u6b21\uff0c\u53d1\u9001\u4e00\u6b21\u3002", None))
#endif // QT_CONFIG(statustip)
        self.single_send_bt.setText(QCoreApplication.translate("SerialTools", u"\u53d1\u9001", None))
#if QT_CONFIG(statustip)
        self.single_send_clear.setStatusTip(QCoreApplication.translate("SerialTools", u"\u6e05\u7a7a\u5355\u6761\u6d88\u606f\u8f93\u5165\u6846\u3002", None))
#endif // QT_CONFIG(statustip)
        self.single_send_clear.setText(QCoreApplication.translate("SerialTools", u"\u6e05\u9664\u53d1\u9001", None))
#if QT_CONFIG(statustip)
        self.single_send_timer_enable.setStatusTip(QCoreApplication.translate("SerialTools", u"\u5355\u6761\u6d88\u606f\uff0c\u662f\u5426\u542f\u7528\u5b9a\u65f6\u53d1\u9001\u3002", None))
#endif // QT_CONFIG(statustip)
        self.single_send_timer_enable.setText(QCoreApplication.translate("SerialTools", u"\u5b9a\u65f6\u53d1\u9001", None))
        self.label_6.setText(QCoreApplication.translate("SerialTools", u"\u5468\u671f\uff1a", None))
#if QT_CONFIG(statustip)
        self.single_send__timer_cycle.setStatusTip(QCoreApplication.translate("SerialTools", u"\u5355\u6761\u6d88\u606f\uff0c\u5b9a\u65f6\u53d1\u9001\u95f4\u9694\u65f6\u95f4\uff0c\u5355\u4f4dms\u3002", None))
#endif // QT_CONFIG(statustip)
        self.label_7.setText(QCoreApplication.translate("SerialTools", u"ms", None))
#if QT_CONFIG(statustip)
        self.single_ascii_send.setStatusTip(QCoreApplication.translate("SerialTools", u"\u5355\u6761\u6d88\u606f\uff0c\u4ee5ASCII\u53d1\u9001\u3002", None))
#endif // QT_CONFIG(statustip)
        self.single_ascii_send.setText(QCoreApplication.translate("SerialTools", u"ASCII\u53d1\u9001", None))
#if QT_CONFIG(statustip)
        self.single_hex_send.setStatusTip(QCoreApplication.translate("SerialTools", u"\u5355\u6761\u6d88\u606f\uff0c\u4ee5Hex\u53d1\u9001\u3002", None))
#endif // QT_CONFIG(statustip)
        self.single_hex_send.setText(QCoreApplication.translate("SerialTools", u"Hex\u53d1\u9001", None))
        self.tab.setTabText(self.tab.indexOf(self.tab_single), QCoreApplication.translate("SerialTools", u"\u5355\u6761\u53d1\u9001", None))
#if QT_CONFIG(statustip)
        self.multi_1_enable.setStatusTip(QCoreApplication.translate("SerialTools", u"\u52fe\u9009\uff0c\u5b9a\u65f6\u53d1\u9001\u65f6\u7b2c1\u4f4d\u53d1\u9001\u3002", None))
#endif // QT_CONFIG(statustip)
        self.multi_1_enable.setText("")
#if QT_CONFIG(statustip)
        self.multi_1_send_text.setStatusTip(QCoreApplication.translate("SerialTools", u"\u53d1\u9001\u6d88\u606f\u8f93\u5165\u3002", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.multi_1_send_btn.setStatusTip(QCoreApplication.translate("SerialTools", u"\u70b9\u51fb\uff0c\u53d1\u9001\u5de6\u4fa7\u6d88\u606f\u3002", None))
#endif // QT_CONFIG(statustip)
        self.multi_1_send_btn.setText(QCoreApplication.translate("SerialTools", u"\u53d1\u9001", None))
#if QT_CONFIG(statustip)
        self.multi_2_enable.setStatusTip(QCoreApplication.translate("SerialTools", u"\u52fe\u9009\uff0c\u5b9a\u65f6\u53d1\u9001\u65f6\u7b2c2\u4f4d\u53d1\u9001\u3002", None))
#endif // QT_CONFIG(statustip)
        self.multi_2_enable.setText("")
#if QT_CONFIG(statustip)
        self.multi_2_send_text.setStatusTip(QCoreApplication.translate("SerialTools", u"\u53d1\u9001\u6d88\u606f\u8f93\u5165\u3002", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.multi_2_send_btn.setStatusTip(QCoreApplication.translate("SerialTools", u"\u70b9\u51fb\uff0c\u53d1\u9001\u5de6\u4fa7\u6d88\u606f\u3002", None))
#endif // QT_CONFIG(statustip)
        self.multi_2_send_btn.setText(QCoreApplication.translate("SerialTools", u"\u53d1\u9001", None))
#if QT_CONFIG(statustip)
        self.multi_3_enable.setStatusTip(QCoreApplication.translate("SerialTools", u"\u52fe\u9009\uff0c\u5b9a\u65f6\u53d1\u9001\u65f6\u7b2c3\u4f4d\u53d1\u9001\u3002", None))
#endif // QT_CONFIG(statustip)
        self.multi_3_enable.setText("")
#if QT_CONFIG(statustip)
        self.multi_3_send_text.setStatusTip(QCoreApplication.translate("SerialTools", u"\u53d1\u9001\u6d88\u606f\u8f93\u5165\u3002", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.multi_3_send_btn.setStatusTip(QCoreApplication.translate("SerialTools", u"\u70b9\u51fb\uff0c\u53d1\u9001\u5de6\u4fa7\u6d88\u606f\u3002", None))
#endif // QT_CONFIG(statustip)
        self.multi_3_send_btn.setText(QCoreApplication.translate("SerialTools", u"\u53d1\u9001", None))
#if QT_CONFIG(statustip)
        self.multi_4_enable.setStatusTip(QCoreApplication.translate("SerialTools", u"\u52fe\u9009\uff0c\u5b9a\u65f6\u53d1\u9001\u65f6\u7b2c4\u4f4d\u53d1\u9001\u3002", None))
#endif // QT_CONFIG(statustip)
        self.multi_4_enable.setText("")
#if QT_CONFIG(statustip)
        self.multi_4_send_text.setStatusTip(QCoreApplication.translate("SerialTools", u"\u53d1\u9001\u6d88\u606f\u8f93\u5165\u3002", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.multi_4_send_btn.setStatusTip(QCoreApplication.translate("SerialTools", u"\u70b9\u51fb\uff0c\u53d1\u9001\u5de6\u4fa7\u6d88\u606f\u3002", None))
#endif // QT_CONFIG(statustip)
        self.multi_4_send_btn.setText(QCoreApplication.translate("SerialTools", u"\u53d1\u9001", None))
#if QT_CONFIG(statustip)
        self.multi_5_enable.setStatusTip(QCoreApplication.translate("SerialTools", u"\u52fe\u9009\uff0c\u5b9a\u65f6\u53d1\u9001\u65f6\u7b2c5\u4f4d\u53d1\u9001\u3002", None))
#endif // QT_CONFIG(statustip)
        self.multi_5_enable.setText("")
#if QT_CONFIG(statustip)
        self.multi_5_send_text.setStatusTip(QCoreApplication.translate("SerialTools", u"\u53d1\u9001\u6d88\u606f\u8f93\u5165\u3002", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.multi_5_send_btn.setStatusTip(QCoreApplication.translate("SerialTools", u"\u70b9\u51fb\uff0c\u53d1\u9001\u5de6\u4fa7\u6d88\u606f\u3002", None))
#endif // QT_CONFIG(statustip)
        self.multi_5_send_btn.setText(QCoreApplication.translate("SerialTools", u"\u53d1\u9001", None))
#if QT_CONFIG(statustip)
        self.multi_6_enable.setStatusTip(QCoreApplication.translate("SerialTools", u"\u52fe\u9009\uff0c\u5b9a\u65f6\u53d1\u9001\u65f6\u7b2c6\u4f4d\u53d1\u9001\u3002", None))
#endif // QT_CONFIG(statustip)
        self.multi_6_enable.setText("")
#if QT_CONFIG(statustip)
        self.multi_6_send_text.setStatusTip(QCoreApplication.translate("SerialTools", u"\u53d1\u9001\u6d88\u606f\u8f93\u5165\u3002", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.multi_6_send_btn.setStatusTip(QCoreApplication.translate("SerialTools", u"\u70b9\u51fb\uff0c\u53d1\u9001\u5de6\u4fa7\u6d88\u606f\u3002", None))
#endif // QT_CONFIG(statustip)
        self.multi_6_send_btn.setText(QCoreApplication.translate("SerialTools", u"\u53d1\u9001", None))
#if QT_CONFIG(statustip)
        self.multi_7_enable.setStatusTip(QCoreApplication.translate("SerialTools", u"\u52fe\u9009\uff0c\u5b9a\u65f6\u53d1\u9001\u65f6\u7b2c7\u4f4d\u53d1\u9001\u3002", None))
#endif // QT_CONFIG(statustip)
        self.multi_7_enable.setText("")
#if QT_CONFIG(statustip)
        self.multi_7_send_text.setStatusTip(QCoreApplication.translate("SerialTools", u"\u53d1\u9001\u6d88\u606f\u8f93\u5165\u3002", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.multi_7_send_btn.setStatusTip(QCoreApplication.translate("SerialTools", u"\u70b9\u51fb\uff0c\u53d1\u9001\u5de6\u4fa7\u6d88\u606f\u3002", None))
#endif // QT_CONFIG(statustip)
        self.multi_7_send_btn.setText(QCoreApplication.translate("SerialTools", u"\u53d1\u9001", None))
#if QT_CONFIG(statustip)
        self.multi_8_enable.setStatusTip(QCoreApplication.translate("SerialTools", u"\u52fe\u9009\uff0c\u5b9a\u65f6\u53d1\u9001\u65f6\u7b2c8\u4f4d\u53d1\u9001\u3002", None))
#endif // QT_CONFIG(statustip)
        self.multi_8_enable.setText("")
#if QT_CONFIG(statustip)
        self.multi_8_send_text.setStatusTip(QCoreApplication.translate("SerialTools", u"\u53d1\u9001\u6d88\u606f\u8f93\u5165\u3002", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.multi_8_send_btn.setStatusTip(QCoreApplication.translate("SerialTools", u"\u70b9\u51fb\uff0c\u53d1\u9001\u5de6\u4fa7\u6d88\u606f\u3002", None))
#endif // QT_CONFIG(statustip)
        self.multi_8_send_btn.setText(QCoreApplication.translate("SerialTools", u"\u53d1\u9001", None))
#if QT_CONFIG(statustip)
        self.multi_9_enable.setStatusTip(QCoreApplication.translate("SerialTools", u"\u52fe\u9009\uff0c\u5b9a\u65f6\u53d1\u9001\u65f6\u7b2c9\u4f4d\u53d1\u9001\u3002", None))
#endif // QT_CONFIG(statustip)
        self.multi_9_enable.setText("")
#if QT_CONFIG(statustip)
        self.multi_9_send_text.setStatusTip(QCoreApplication.translate("SerialTools", u"\u53d1\u9001\u6d88\u606f\u8f93\u5165\u3002", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.multi_9_send_btn.setStatusTip(QCoreApplication.translate("SerialTools", u"\u70b9\u51fb\uff0c\u53d1\u9001\u5de6\u4fa7\u6d88\u606f\u3002", None))
#endif // QT_CONFIG(statustip)
        self.multi_9_send_btn.setText(QCoreApplication.translate("SerialTools", u"\u53d1\u9001", None))
#if QT_CONFIG(statustip)
        self.multi_10_enable.setStatusTip(QCoreApplication.translate("SerialTools", u"\u52fe\u9009\uff0c\u5b9a\u65f6\u53d1\u9001\u65f6\u7b2c10\u4f4d\u53d1\u9001\u3002", None))
#endif // QT_CONFIG(statustip)
        self.multi_10_enable.setText("")
#if QT_CONFIG(statustip)
        self.multi_10_send_text.setStatusTip(QCoreApplication.translate("SerialTools", u"\u53d1\u9001\u6d88\u606f\u8f93\u5165\u3002", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.multi_10_send_btn.setStatusTip(QCoreApplication.translate("SerialTools", u"\u70b9\u51fb\uff0c\u53d1\u9001\u5de6\u4fa7\u6d88\u606f\u3002", None))
#endif // QT_CONFIG(statustip)
        self.multi_10_send_btn.setText(QCoreApplication.translate("SerialTools", u"\u53d1\u9001", None))
#if QT_CONFIG(statustip)
        self.multi_hex_send.setStatusTip(QCoreApplication.translate("SerialTools", u"\u4ee5\u5341\u516d\u8fdb\u5236\u53d1\u9001\u3002", None))
#endif // QT_CONFIG(statustip)
        self.multi_hex_send.setText(QCoreApplication.translate("SerialTools", u"Hex\u53d1\u9001", None))
#if QT_CONFIG(statustip)
        self.multi_send_timer_enable.setStatusTip(QCoreApplication.translate("SerialTools", u"\u542f\u7528/\u7981\u7528\u5b9a\u65f6\u53d1\u9001\u3002", None))
#endif // QT_CONFIG(statustip)
        self.multi_send_timer_enable.setText(QCoreApplication.translate("SerialTools", u"\u5b9a\u65f6\u53d1\u9001", None))
        self.label_8.setText(QCoreApplication.translate("SerialTools", u"\u5468\u671f\uff1a", None))
#if QT_CONFIG(statustip)
        self.multi_send_timer_cycle.setStatusTip(QCoreApplication.translate("SerialTools", u"\u5b9a\u65f6\u53d1\u9001\u95f4\u9694\u65f6\u95f4\u3002", None))
#endif // QT_CONFIG(statustip)
        self.label_9.setText(QCoreApplication.translate("SerialTools", u"ms", None))
#if QT_CONFIG(statustip)
        self.multi_export.setStatusTip(QCoreApplication.translate("SerialTools", u"\u5bfc\u51fa\u591a\u6761\u6d88\u606f\u3002", None))
#endif // QT_CONFIG(statustip)
        self.multi_export.setText(QCoreApplication.translate("SerialTools", u"\u5bfc\u51fa", None))
#if QT_CONFIG(statustip)
        self.multi_import.setStatusTip(QCoreApplication.translate("SerialTools", u"\u5bfc\u5165\u591a\u6761\u6d88\u606f\u3002", None))
#endif // QT_CONFIG(statustip)
        self.multi_import.setText(QCoreApplication.translate("SerialTools", u"\u5bfc\u5165", None))
        self.tab.setTabText(self.tab.indexOf(self.tab_multi), QCoreApplication.translate("SerialTools", u"\u591a\u6761\u53d1\u9001", None))
        self.tx_num.setText(QCoreApplication.translate("SerialTools", u"TX: 0", None))
        self.rx_num.setText(QCoreApplication.translate("SerialTools", u"RX: 0", None))
    # retranslateUi

