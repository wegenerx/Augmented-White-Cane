# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
    QCommandLinkButton, QFormLayout, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QTabWidget, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_SerialTools(object):
    def setupUi(self, SerialTools):
        if not SerialTools.objectName():
            SerialTools.setObjectName(u"SerialTools")
        SerialTools.resize(1094, 709)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SerialTools.sizePolicy().hasHeightForWidth())
        SerialTools.setSizePolicy(sizePolicy)
        SerialTools.setMinimumSize(QSize(900, 590))
        SerialTools.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(SerialTools)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_26 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.formLayout_2 = QFormLayout(self.tab_4)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.serial_group = QGroupBox(self.tab_4)
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

        self.group_send = QGroupBox(self.tab_4)
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
        self.recv_ascii.setChecked(False)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.recv_ascii)

        self.recv_hex = QCheckBox(self.group_send)
        self.buttonGroup.addButton(self.recv_hex)
        self.recv_hex.setObjectName(u"recv_hex")
        sizePolicy.setHeightForWidth(self.recv_hex.sizePolicy().hasHeightForWidth())
        self.recv_hex.setSizePolicy(sizePolicy)
        self.recv_hex.setChecked(True)

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

        self.recv_clear_2 = QPushButton(self.group_send)
        self.recv_clear_2.setObjectName(u"recv_clear_2")

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.recv_clear_2)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.verticalLayout_5.addWidget(self.group_send)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)


        self.formLayout_2.setLayout(0, QFormLayout.LabelRole, self.verticalLayout_5)

        self.recv_text = QTextEdit(self.tab_4)
        self.recv_text.setObjectName(u"recv_text")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.recv_text.sizePolicy().hasHeightForWidth())
        self.recv_text.setSizePolicy(sizePolicy1)
        self.recv_text.setMinimumSize(QSize(690, 370))
        self.recv_text.setReadOnly(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.recv_text)

        self.tab = QTabWidget(self.tab_4)
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
        self.multi_hex_send.setChecked(True)

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
        self.tx_num = QLabel(self.tab_4)
        self.tx_num.setObjectName(u"tx_num")
        sizePolicy.setHeightForWidth(self.tx_num.sizePolicy().hasHeightForWidth())
        self.tx_num.setSizePolicy(sizePolicy)
        self.tx_num.setMinimumSize(QSize(100, 0))
        self.tx_num.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_25.addWidget(self.tx_num)

        self.line_3 = QFrame(self.tab_4)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_25.addWidget(self.line_3)

        self.rx_num = QLabel(self.tab_4)
        self.rx_num.setObjectName(u"rx_num")
        sizePolicy.setHeightForWidth(self.rx_num.sizePolicy().hasHeightForWidth())
        self.rx_num.setSizePolicy(sizePolicy)
        self.rx_num.setMinimumSize(QSize(100, 0))
        self.rx_num.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_25.addWidget(self.rx_num)

        self.line_4 = QFrame(self.tab_4)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_25.addWidget(self.line_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_2)


        self.formLayout_2.setLayout(2, QFormLayout.SpanningRole, self.horizontalLayout_25)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_4 = QGridLayout(self.tab_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_6 = QGroupBox(self.tab_5)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_11 = QGridLayout(self.groupBox_6)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.verticalSpacer_4 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.groupBox_6)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_29 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_79 = QLabel(self.groupBox_4)
        self.label_79.setObjectName(u"label_79")
        font = QFont()
        font.setPointSize(9)
        self.label_79.setFont(font)
        self.label_79.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_79, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.label_80 = QLabel(self.groupBox_4)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_80, 0, 2, 1, 1)

        self.lineEdit_6 = QLineEdit(self.groupBox_4)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_9.addWidget(self.lineEdit_6, 1, 0, 1, 1)

        self.label_81 = QLabel(self.groupBox_4)
        self.label_81.setObjectName(u"label_81")
        font1 = QFont()
        font1.setPointSize(20)
        self.label_81.setFont(font1)
        self.label_81.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_81, 1, 1, 1, 1)

        self.lineEdit_7 = QLineEdit(self.groupBox_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_9.addWidget(self.lineEdit_7, 1, 2, 1, 1)


        self.horizontalLayout_29.addLayout(self.gridLayout_9)


        self.gridLayout_11.addWidget(self.groupBox_4, 1, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_5, 1, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 26, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_5, 2, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_6, 1, 1, 1, 1)

        self.groupBox = QGroupBox(self.tab_5)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_54 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_82 = QLabel(self.groupBox)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_82, 13, 1, 1, 1)

        self.label_78 = QLabel(self.groupBox)
        self.label_78.setObjectName(u"label_78")

        self.gridLayout.addWidget(self.label_78, 18, 6, 1, 1)

        self.label_38 = QLabel(self.groupBox)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_38, 16, 1, 1, 1)

        self.line_16 = QFrame(self.groupBox)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_16, 8, 3, 1, 4)

        self.line_6 = QFrame(self.groupBox)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_6, 1, 0, 1, 7)

        self.line_14 = QFrame(self.groupBox)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_14, 11, 3, 1, 4)

        self.lineEdit_20 = QLineEdit(self.groupBox)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.gridLayout.addWidget(self.lineEdit_20, 7, 3, 1, 2)

        self.label_46 = QLabel(self.groupBox)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout.addWidget(self.label_46, 0, 3, 1, 2)

        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 12, 0, 1, 1)

        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 16, 0, 1, 1)

        self.label_69 = QLabel(self.groupBox)
        self.label_69.setObjectName(u"label_69")

        self.gridLayout.addWidget(self.label_69, 2, 3, 1, 2)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_63 = QLabel(self.groupBox)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_5.addWidget(self.label_63, 0, 0, 1, 1)

        self.lineEdit_19 = QLineEdit(self.groupBox)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.gridLayout_5.addWidget(self.lineEdit_19, 0, 1, 1, 1)

        self.label_64 = QLabel(self.groupBox)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_5.addWidget(self.label_64, 0, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_5, 6, 6, 1, 1)

        self.line_9 = QFrame(self.groupBox)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_9, 17, 3, 1, 4)

        self.label_65 = QLabel(self.groupBox)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_65, 7, 1, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_72 = QLabel(self.groupBox)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_7.addWidget(self.label_72, 0, 0, 1, 1)

        self.lineEdit_22 = QLineEdit(self.groupBox)
        self.lineEdit_22.setObjectName(u"lineEdit_22")

        self.gridLayout_7.addWidget(self.lineEdit_22, 0, 1, 1, 1)

        self.label_73 = QLabel(self.groupBox)
        self.label_73.setObjectName(u"label_73")

        self.gridLayout_7.addWidget(self.label_73, 0, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_7, 12, 6, 1, 1)

        self.label_67 = QLabel(self.groupBox)
        self.label_67.setObjectName(u"label_67")

        self.gridLayout.addWidget(self.label_67, 9, 3, 1, 2)

        self.label_47 = QLabel(self.groupBox)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout.addWidget(self.label_47, 0, 5, 1, 1)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 10, 3, 1, 2)

        self.line_15 = QFrame(self.groupBox)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_15, 8, 0, 1, 2)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_75 = QLabel(self.groupBox)
        self.label_75.setObjectName(u"label_75")

        self.gridLayout_8.addWidget(self.label_75, 0, 0, 1, 1)

        self.lineEdit_23 = QLineEdit(self.groupBox)
        self.lineEdit_23.setObjectName(u"lineEdit_23")

        self.gridLayout_8.addWidget(self.lineEdit_23, 0, 1, 1, 1)

        self.label_76 = QLabel(self.groupBox)
        self.label_76.setObjectName(u"label_76")

        self.gridLayout_8.addWidget(self.label_76, 0, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_8, 16, 6, 1, 1)

        self.line_12 = QFrame(self.groupBox)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_12, 14, 3, 1, 4)

        self.label_50 = QLabel(self.groupBox)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout.addWidget(self.label_50, 2, 6, 1, 1)

        self.label_71 = QLabel(self.groupBox)
        self.label_71.setObjectName(u"label_71")

        self.gridLayout.addWidget(self.label_71, 15, 3, 1, 2)

        self.label_45 = QLabel(self.groupBox)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout.addWidget(self.label_45, 0, 1, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lineEdit_21 = QLineEdit(self.groupBox)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.gridLayout_6.addWidget(self.lineEdit_21, 0, 1, 1, 1)

        self.label_70 = QLabel(self.groupBox)
        self.label_70.setObjectName(u"label_70")

        self.gridLayout_6.addWidget(self.label_70, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_6, 10, 6, 1, 1)

        self.label_48 = QLabel(self.groupBox)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout.addWidget(self.label_48, 0, 6, 1, 1)

        self.line_13 = QFrame(self.groupBox)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_13, 11, 0, 1, 2)

        self.lineEdit_8 = QLineEdit(self.groupBox)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout.addWidget(self.lineEdit_8, 16, 3, 1, 2)

        self.line_8 = QFrame(self.groupBox)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_8, 0, 2, 1, 1)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 9, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.groupBox)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_6, 15, 5, 1, 1)

        self.label_43 = QLabel(self.groupBox)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout.addWidget(self.label_43, 12, 1, 1, 1)

        self.label_41 = QLabel(self.groupBox)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout.addWidget(self.label_41, 9, 1, 1, 1)

        self.label_74 = QLabel(self.groupBox)
        self.label_74.setObjectName(u"label_74")

        self.gridLayout.addWidget(self.label_74, 15, 6, 1, 1)

        self.pushButton_5 = QPushButton(self.groupBox)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_5, 12, 5, 1, 1)

        self.line_18 = QFrame(self.groupBox)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.HLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_18, 5, 3, 1, 4)

        self.line_11 = QFrame(self.groupBox)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_11, 14, 0, 1, 2)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_2, 6, 5, 1, 1)

        self.line_10 = QFrame(self.groupBox)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_10, 17, 0, 1, 2)

        self.label_66 = QLabel(self.groupBox)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout.addWidget(self.label_66, 7, 6, 1, 1)

        self.label_77 = QLabel(self.groupBox)
        self.label_77.setObjectName(u"label_77")

        self.gridLayout.addWidget(self.label_77, 18, 3, 1, 2)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton, 2, 5, 1, 1)

        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 18, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)

        self.label_42 = QLabel(self.groupBox)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout.addWidget(self.label_42, 15, 1, 1, 1)

        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 15, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 10, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 12, 3, 1, 2)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 6, 3, 1, 2)

        self.label_68 = QLabel(self.groupBox)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout.addWidget(self.label_68, 9, 6, 1, 1)

        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_3, 9, 5, 1, 1)

        self.line_17 = QFrame(self.groupBox)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_17, 5, 0, 1, 2)

        self.label_40 = QLabel(self.groupBox)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_40, 10, 1, 1, 1)

        self.label_39 = QLabel(self.groupBox)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout.addWidget(self.label_39, 6, 1, 1, 1)

        self.label_44 = QLabel(self.groupBox)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout.addWidget(self.label_44, 2, 1, 1, 1)

        self.pushButton_8 = QPushButton(self.groupBox)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_8, 18, 5, 1, 1)

        self.label_37 = QLabel(self.groupBox)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout.addWidget(self.label_37, 18, 1, 1, 1)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 6, 0, 1, 1)

        self.lineEdit_24 = QLineEdit(self.groupBox)
        self.lineEdit_24.setObjectName(u"lineEdit_24")

        self.gridLayout.addWidget(self.lineEdit_24, 13, 3, 1, 1)

        self.lineEdit_25 = QLineEdit(self.groupBox)
        self.lineEdit_25.setObjectName(u"lineEdit_25")

        self.gridLayout.addWidget(self.lineEdit_25, 19, 3, 1, 1)

        self.line_7 = QFrame(self.groupBox)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_7, 2, 2, 18, 1)

        self.label_83 = QLabel(self.groupBox)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_83, 19, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_53 = QLabel(self.groupBox)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_3.addWidget(self.label_53, 0, 4, 1, 1)

        self.lineEdit_18 = QLineEdit(self.groupBox)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.gridLayout_3.addWidget(self.lineEdit_18, 2, 5, 1, 1)

        self.lineEdit_17 = QLineEdit(self.groupBox)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.gridLayout_3.addWidget(self.lineEdit_17, 2, 3, 1, 1)

        self.lineEdit_11 = QLineEdit(self.groupBox)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout_3.addWidget(self.lineEdit_11, 0, 3, 1, 1)

        self.label_60 = QLabel(self.groupBox)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_3.addWidget(self.label_60, 2, 4, 1, 1)

        self.label_54 = QLabel(self.groupBox)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_3.addWidget(self.label_54, 0, 6, 1, 1)

        self.label_62 = QLabel(self.groupBox)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_3.addWidget(self.label_62, 2, 2, 1, 1)

        self.label_56 = QLabel(self.groupBox)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_3.addWidget(self.label_56, 1, 2, 1, 1)

        self.label_57 = QLabel(self.groupBox)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_3.addWidget(self.label_57, 1, 0, 1, 1)

        self.label_59 = QLabel(self.groupBox)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_3.addWidget(self.label_59, 2, 0, 1, 1)

        self.label_51 = QLabel(self.groupBox)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_3.addWidget(self.label_51, 0, 0, 1, 1)

        self.label_61 = QLabel(self.groupBox)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_3.addWidget(self.label_61, 2, 6, 1, 1)

        self.label_55 = QLabel(self.groupBox)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_3.addWidget(self.label_55, 1, 6, 1, 1)

        self.label_52 = QLabel(self.groupBox)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_3.addWidget(self.label_52, 0, 2, 1, 1)

        self.label_58 = QLabel(self.groupBox)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_3.addWidget(self.label_58, 1, 4, 1, 1)

        self.lineEdit_12 = QLineEdit(self.groupBox)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout_3.addWidget(self.lineEdit_12, 0, 5, 1, 1)

        self.lineEdit_14 = QLineEdit(self.groupBox)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.gridLayout_3.addWidget(self.lineEdit_14, 1, 5, 1, 1)

        self.lineEdit_13 = QLineEdit(self.groupBox)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.gridLayout_3.addWidget(self.lineEdit_13, 1, 3, 1, 1)

        self.lineEdit_16 = QLineEdit(self.groupBox)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.gridLayout_3.addWidget(self.lineEdit_16, 2, 1, 1, 1)

        self.lineEdit_15 = QLineEdit(self.groupBox)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.gridLayout_3.addWidget(self.lineEdit_15, 1, 1, 1, 1)

        self.lineEdit_10 = QLineEdit(self.groupBox)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_3.addWidget(self.lineEdit_10, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 3, 6, 2, 1)

        self.lineEdit_9 = QLineEdit(self.groupBox)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout.addWidget(self.lineEdit_9, 3, 3, 2, 2)

        self.label_49 = QLabel(self.groupBox)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_49, 3, 1, 2, 1)


        self.horizontalLayout_54.addLayout(self.gridLayout)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 3)

        self.groupBox_3 = QGroupBox(self.tab_5)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_30 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.lineEdit_LLM = QLineEdit(self.groupBox_3)
        self.lineEdit_LLM.setObjectName(u"lineEdit_LLM")

        self.gridLayout_10.addWidget(self.lineEdit_LLM, 0, 0, 1, 1)

        self.pushButton_LLM = QPushButton(self.groupBox_3)
        self.pushButton_LLM.setObjectName(u"pushButton_LLM")
        self.pushButton_LLM.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_10.addWidget(self.pushButton_LLM, 0, 1, 1, 1)

        self.textBrowser_LLM = QTextBrowser(self.groupBox_3)
        self.textBrowser_LLM.setObjectName(u"textBrowser_LLM")

        self.gridLayout_10.addWidget(self.textBrowser_LLM, 1, 0, 1, 2)


        self.horizontalLayout_30.addLayout(self.gridLayout_10)


        self.gridLayout_4.addWidget(self.groupBox_3, 1, 2, 2, 1)

        self.groupBox_2 = QGroupBox(self.tab_5)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.pushButton_upper_computer = QPushButton(self.groupBox_2)
        self.pushButton_upper_computer.setObjectName(u"pushButton_upper_computer")
        self.pushButton_upper_computer.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_28.addWidget(self.pushButton_upper_computer)

        self.pushButton_open_upper_computer = QPushButton(self.groupBox_2)
        self.pushButton_open_upper_computer.setObjectName(u"pushButton_open_upper_computer")
        self.pushButton_open_upper_computer.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_28.addWidget(self.pushButton_open_upper_computer)

        self.pushButton_lower_computer = QPushButton(self.groupBox_2)
        self.pushButton_lower_computer.setObjectName(u"pushButton_lower_computer")
        self.pushButton_lower_computer.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_28.addWidget(self.pushButton_lower_computer)


        self.verticalLayout_9.addLayout(self.horizontalLayout_28)

        self.commandLinkButton_open_keil_project = QCommandLinkButton(self.groupBox_2)
        self.commandLinkButton_open_keil_project.setObjectName(u"commandLinkButton_open_keil_project")
        self.commandLinkButton_open_keil_project.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.commandLinkButton_open_keil_project)

        self.commandLinkButton_open_guide_pdf = QCommandLinkButton(self.groupBox_2)
        self.commandLinkButton_open_guide_pdf.setObjectName(u"commandLinkButton_open_guide_pdf")
        self.commandLinkButton_open_guide_pdf.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.commandLinkButton_open_guide_pdf)

        self.commandLinkButton_open_folder = QCommandLinkButton(self.groupBox_2)
        self.commandLinkButton_open_folder.setObjectName(u"commandLinkButton_open_folder")
        self.commandLinkButton_open_folder.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.commandLinkButton_open_folder)


        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_34 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.groupBox_9 = QGroupBox(self.tab_3)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_12 = QGridLayout(self.groupBox_9)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.groupBox_5 = QGroupBox(self.groupBox_9)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_31 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_graph_1 = QLabel(self.groupBox_5)
        self.label_graph_1.setObjectName(u"label_graph_1")

        self.horizontalLayout_31.addWidget(self.label_graph_1)


        self.verticalLayout_10.addWidget(self.groupBox_5)

        self.groupBox_7 = QGroupBox(self.groupBox_9)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.horizontalLayout_32 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_graph_2 = QLabel(self.groupBox_7)
        self.label_graph_2.setObjectName(u"label_graph_2")

        self.horizontalLayout_32.addWidget(self.label_graph_2)


        self.verticalLayout_10.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.groupBox_9)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.horizontalLayout_33 = QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_graph_3 = QLabel(self.groupBox_8)
        self.label_graph_3.setObjectName(u"label_graph_3")

        self.horizontalLayout_33.addWidget(self.label_graph_3)


        self.verticalLayout_10.addWidget(self.groupBox_8)


        self.gridLayout_12.addLayout(self.verticalLayout_10, 0, 0, 1, 1)


        self.horizontalLayout_34.addWidget(self.groupBox_9)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.horizontalLayout_35 = QHBoxLayout(self.tab_6)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.groupBox_10 = QGroupBox(self.tab_6)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.horizontalLayout_36 = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_video = QLabel(self.groupBox_10)
        self.label_video.setObjectName(u"label_video")

        self.horizontalLayout_36.addWidget(self.label_video)


        self.horizontalLayout_35.addWidget(self.groupBox_10)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_27 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.textBrowser = QTextBrowser(self.tab_2)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout_27.addWidget(self.textBrowser)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_26.addWidget(self.tabWidget)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_26.addWidget(self.line_5)

        SerialTools.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(SerialTools)
        self.statusBar.setObjectName(u"statusBar")
        SerialTools.setStatusBar(self.statusBar)

        self.retranslateUi(SerialTools)

        self.tabWidget.setCurrentIndex(3)
        self.tab.setCurrentIndex(1)


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
        self.recv_clear_2.setStatusTip(QCoreApplication.translate("SerialTools", u"\u6e05\u7a7a\u5df2\u63a5\u6536\u6d88\u606f\u663e\u793a\u3002", None))
#endif // QT_CONFIG(statustip)
        self.recv_clear_2.setText(QCoreApplication.translate("SerialTools", u"\u4fdd\u5b58recv_clear_2", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("SerialTools", u"\u539f\u59cb\u529f\u80fd", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("SerialTools", u"16\u8fdb\u5236 - 10\u8fdb\u5236\u8f6c\u6362\u5668", None))
        self.groupBox_4.setTitle("")
        self.label_79.setText(QCoreApplication.translate("SerialTools", u"\u5341\u8fdb\u5236 dec", None))
        self.label_80.setText(QCoreApplication.translate("SerialTools", u"\u5341\u516d\u8fdb\u5236 hex", None))
        self.label_81.setText(QCoreApplication.translate("SerialTools", u"\u2194", None))
        self.groupBox.setTitle(QCoreApplication.translate("SerialTools", u"\u96f7\u8fbe\u53d1\u9001\u4e0e\u63a5\u6536\u4fe1\u53f7", None))
        self.label_82.setText(QCoreApplication.translate("SerialTools", u"\u8fd4\u56de\u503c", None))
        self.label_78.setText(QCoreApplication.translate("SerialTools", u"\u5199\u5165flash", None))
        self.label_38.setText(QCoreApplication.translate("SerialTools", u"\u8fd4\u56de\u503c", None))
        self.lineEdit_20.setText("")
        self.label_46.setText(QCoreApplication.translate("SerialTools", u"\u542b\u4e49", None))
        self.label_18.setText(QCoreApplication.translate("SerialTools", u"4", None))
        self.label_17.setText("")
        self.label_69.setText(QCoreApplication.translate("SerialTools", u"DF1002F1EF", None))
        self.label_63.setText(QCoreApplication.translate("SerialTools", u"\u8bbe\u7f6e\u68c0\u6d4b\u95e8\u9650\u4e3a", None))
        self.label_64.setText(QCoreApplication.translate("SerialTools", u"\uff08\u6700\u59270xFFFF, 65536\uff09", None))
        self.label_65.setText(QCoreApplication.translate("SerialTools", u"\u8fd4\u56de\u503c", None))
        self.label_72.setText(QCoreApplication.translate("SerialTools", u"1\u5b57\u8282\u6570\u636e\uff0c\u8bbe\u7f6e\u4e2d\u533a\u89d2\u5ea6\u8303\u56f4\u503c\uff0c\u5355\u4f4d\u00b0\uff0c\u503c\u4e3a", None))
        self.label_73.setText(QCoreApplication.translate("SerialTools", u"\uff08\u6700\u59270xFF, 256\uff09", None))
        self.label_67.setText(QCoreApplication.translate("SerialTools", u"DF150000EF", None))
        self.label_47.setText(QCoreApplication.translate("SerialTools", u"\u53d1\u9001", None))
        self.lineEdit_4.setText(QCoreApplication.translate("SerialTools", u"CF1502320554EF", None))
        self.label_75.setText(QCoreApplication.translate("SerialTools", u"\u89d2\u5ea6\u8303\u56f4\u503c\u4e3a", None))
        self.label_76.setText(QCoreApplication.translate("SerialTools", u"\uff08\u6700\u59270xFF, 256\uff09", None))
        self.label_50.setText(QCoreApplication.translate("SerialTools", u"\u8bfb\u53d6\u76ee\u6807", None))
        self.label_71.setText(QCoreApplication.translate("SerialTools", u"DF120000EF", None))
        self.label_45.setText(QCoreApplication.translate("SerialTools", u"\u64cd\u4f5c", None))
        self.label_70.setText(QCoreApplication.translate("SerialTools", u"\u68c0\u6d4b\u95e8\u9650\u9608\u503c\u4e3a", None))
        self.label_48.setText(QCoreApplication.translate("SerialTools", u"\u542b\u4e49", None))
        self.lineEdit_8.setText(QCoreApplication.translate("SerialTools", u"CF120B32000000001E01FF", None))
        self.label_13.setText(QCoreApplication.translate("SerialTools", u"3", None))
        self.pushButton_6.setText(QCoreApplication.translate("SerialTools", u"\u53d1\u9001", None))
        self.label_43.setText(QCoreApplication.translate("SerialTools", u"\u8bbe\u7f6e\u4e2d\u533a\u89d2\u5ea6\u8303\u56f4", None))
        self.label_41.setText(QCoreApplication.translate("SerialTools", u"\u8bfb\u53d6\u95e8\u9650", None))
        self.label_74.setText(QCoreApplication.translate("SerialTools", u"\u8bfb\u53d6\u4e2d\u533a\u89d2\u5ea6\u8303\u56f4", None))
        self.pushButton_5.setText(QCoreApplication.translate("SerialTools", u"\u53d1\u9001", None))
        self.pushButton_2.setText(QCoreApplication.translate("SerialTools", u"\u53d1\u9001", None))
        self.label_66.setText(QCoreApplication.translate("SerialTools", u"\u7801\u5934+\u6a21\u5f0f+\u5e27\u957f+\u95e8\u9650", None))
        self.label_77.setText(QCoreApplication.translate("SerialTools", u"DF140000EF", None))
        self.pushButton.setText(QCoreApplication.translate("SerialTools", u"\u53d1\u9001", None))
        self.label_15.setText(QCoreApplication.translate("SerialTools", u"6", None))
        self.label_11.setText(QCoreApplication.translate("SerialTools", u"1", None))
        self.label_42.setText(QCoreApplication.translate("SerialTools", u"\u8bfb\u53d6\u4e2d\u533a\u89d2\u5ea6\u8303\u56f4", None))
        self.label_16.setText(QCoreApplication.translate("SerialTools", u"5", None))
        self.label_14.setText("")
        self.lineEdit_5.setText(QCoreApplication.translate("SerialTools", u"DF133200EF", None))
        self.lineEdit_2.setText(QCoreApplication.translate("SerialTools", u"DF11 F000 EF", None))
        self.label_68.setText(QCoreApplication.translate("SerialTools", u"\u8bfb\u53d6\u95e8\u9650", None))
        self.pushButton_3.setText(QCoreApplication.translate("SerialTools", u"\u53d1\u9001", None))
        self.label_40.setText(QCoreApplication.translate("SerialTools", u"\u8fd4\u56de\u503c", None))
        self.label_39.setText(QCoreApplication.translate("SerialTools", u"\u8bbe\u7f6e\u95e8\u9650", None))
        self.label_44.setText(QCoreApplication.translate("SerialTools", u"\u8bfb\u53d6\u76ee\u6807", None))
        self.pushButton_8.setText(QCoreApplication.translate("SerialTools", u"\u53d1\u9001", None))
        self.label_37.setText(QCoreApplication.translate("SerialTools", u"\u5199\u5165flash", None))
        self.label_12.setText(QCoreApplication.translate("SerialTools", u"2", None))
        self.lineEdit_24.setText(QCoreApplication.translate("SerialTools", u"\uff1f", None))
        self.lineEdit_25.setText(QCoreApplication.translate("SerialTools", u"\uff1f", None))
        self.label_83.setText(QCoreApplication.translate("SerialTools", u"\u8fd4\u56de\u503c", None))
        self.label_53.setText(QCoreApplication.translate("SerialTools", u"\uff0c\u8ddd\u79bb", None))
        self.label_60.setText(QCoreApplication.translate("SerialTools", u"\uff0c\u8ddd\u79bb", None))
        self.label_54.setText(QCoreApplication.translate("SerialTools", u"\u5206\u7c73", None))
        self.label_62.setText(QCoreApplication.translate("SerialTools", u"\u76ee\u6807\uff0c\u5f3a\u5ea6\u4e3a", None))
        self.label_56.setText(QCoreApplication.translate("SerialTools", u"\u76ee\u6807\uff0c\u5f3a\u5ea6\u4e3a", None))
        self.label_57.setText(QCoreApplication.translate("SerialTools", u"\u4e2d\u533a", None))
        self.label_59.setText(QCoreApplication.translate("SerialTools", u"\u53f3\u533a", None))
        self.label_51.setText(QCoreApplication.translate("SerialTools", u"\u5de6\u533a", None))
        self.label_61.setText(QCoreApplication.translate("SerialTools", u"\u5206\u7c73", None))
        self.label_55.setText(QCoreApplication.translate("SerialTools", u"\u5206\u7c73", None))
        self.label_52.setText(QCoreApplication.translate("SerialTools", u"\u76ee\u6807\uff0c\u5f3a\u5ea6\u4e3a", None))
        self.label_58.setText(QCoreApplication.translate("SerialTools", u"\uff0c\u8ddd\u79bb", None))
        self.lineEdit_9.setText(QCoreApplication.translate("SerialTools", u"CF100B 013A08 013406 013806 A701 EF", None))
        self.label_49.setText(QCoreApplication.translate("SerialTools", u"\u8fd4\u56de\u503c", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("SerialTools", u"\u5927\u6a21\u578b\u8c03\u7528\u5668", None))
        self.pushButton_LLM.setText(QCoreApplication.translate("SerialTools", u"\u53d1\u9001", None))
        self.groupBox_2.setTitle("")
        self.pushButton_upper_computer.setText(QCoreApplication.translate("SerialTools", u"\u4e0a\u4f4d\u673a\u6587\u4ef6\u5939", None))
        self.pushButton_open_upper_computer.setText(QCoreApplication.translate("SerialTools", u"\u6253\u5f00\u4e0a\u4f4d\u673a", None))
        self.pushButton_lower_computer.setText(QCoreApplication.translate("SerialTools", u"\u96f7\u8fbe\u677f\u5b50keil\u6587\u4ef6\u5939", None))
        self.commandLinkButton_open_keil_project.setText(QCoreApplication.translate("SerialTools", u"\u6253\u5f00stm32keil\u5de5\u7a0b\u6587\u4ef6\u5939", None))
        self.commandLinkButton_open_guide_pdf.setText(QCoreApplication.translate("SerialTools", u"\u6253\u5f00\u96f7\u8fbe\u624b\u518c", None))
        self.commandLinkButton_open_folder.setText(QCoreApplication.translate("SerialTools", u"\u6253\u5f00\u4e32\u53e3\u52a9\u624b\u5de5\u7a0b\u6240\u5728\u6587\u4ef6\u5939", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("SerialTools", u"\u9488\u5bf9\u96f7\u8fbe\u7684\u6269\u5c55\u529f\u80fd", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("SerialTools", u"\u96f7\u8fbe\u56fe\u7a97", None))
        self.groupBox_5.setTitle("")
        self.label_graph_1.setText(QCoreApplication.translate("SerialTools", u"TextLabel1", None))
        self.groupBox_7.setTitle("")
        self.label_graph_2.setText(QCoreApplication.translate("SerialTools", u"TextLabel2", None))
        self.groupBox_8.setTitle("")
        self.label_graph_3.setText(QCoreApplication.translate("SerialTools", u"TextLabel3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("SerialTools", u"\u96f7\u8fbe\u4fe1\u53f7\u56fe\u7a97", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("SerialTools", u"\u56fe\u50cf\u533a\u57df", None))
        self.label_video.setText(QCoreApplication.translate("SerialTools", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("SerialTools", u"\u76ee\u6807\u68c0\u6d4b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("SerialTools", u"\u96f7\u8fbe\u52a9\u624b\u624b\u518c", None))
    # retranslateUi

