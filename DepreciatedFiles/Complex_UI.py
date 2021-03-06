# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Complex_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(529, 705)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 531, 691))
        self.tabWidget.setObjectName("tabWidget")
        self.currentMeasurements = QtWidgets.QWidget()
        self.currentMeasurements.setObjectName("currentMeasurements")
        self.groupBox_25 = QtWidgets.QGroupBox(self.currentMeasurements)
        self.groupBox_25.setGeometry(QtCore.QRect(270, 20, 211, 201))
        self.groupBox_25.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_25.setObjectName("groupBox_25")
        self.s2_measurement_output = QtWidgets.QTextEdit(self.groupBox_25)
        self.s2_measurement_output.setGeometry(QtCore.QRect(0, 30, 211, 171))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.s2_measurement_output.setFont(font)
        self.s2_measurement_output.setReadOnly(True)
        self.s2_measurement_output.setObjectName("s2_measurement_output")
        self.groupBox_26 = QtWidgets.QGroupBox(self.currentMeasurements)
        self.groupBox_26.setGeometry(QtCore.QRect(270, 230, 211, 201))
        self.groupBox_26.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_26.setObjectName("groupBox_26")
        self.s4_measurement_output = QtWidgets.QTextEdit(self.groupBox_26)
        self.s4_measurement_output.setGeometry(QtCore.QRect(0, 30, 211, 171))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.s4_measurement_output.setFont(font)
        self.s4_measurement_output.setReadOnly(True)
        self.s4_measurement_output.setObjectName("s4_measurement_output")
        self.groupBox_27 = QtWidgets.QGroupBox(self.currentMeasurements)
        self.groupBox_27.setGeometry(QtCore.QRect(270, 440, 211, 201))
        self.groupBox_27.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_27.setObjectName("groupBox_27")
        self.s6_measurement_output = QtWidgets.QTextEdit(self.groupBox_27)
        self.s6_measurement_output.setGeometry(QtCore.QRect(0, 30, 211, 171))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.s6_measurement_output.setFont(font)
        self.s6_measurement_output.setReadOnly(True)
        self.s6_measurement_output.setObjectName("s6_measurement_output")
        self.groupBox_28 = QtWidgets.QGroupBox(self.currentMeasurements)
        self.groupBox_28.setGeometry(QtCore.QRect(30, 20, 211, 201))
        self.groupBox_28.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_28.setObjectName("groupBox_28")
        self.s1_measurement_output = QtWidgets.QTextEdit(self.groupBox_28)
        self.s1_measurement_output.setGeometry(QtCore.QRect(0, 30, 211, 171))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.s1_measurement_output.setFont(font)
        self.s1_measurement_output.setReadOnly(True)
        self.s1_measurement_output.setObjectName("s1_measurement_output")
        self.groupBox_29 = QtWidgets.QGroupBox(self.currentMeasurements)
        self.groupBox_29.setGeometry(QtCore.QRect(30, 230, 211, 201))
        self.groupBox_29.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_29.setObjectName("groupBox_29")
        self.s3_measurement_output = QtWidgets.QTextEdit(self.groupBox_29)
        self.s3_measurement_output.setGeometry(QtCore.QRect(0, 30, 211, 171))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.s3_measurement_output.setFont(font)
        self.s3_measurement_output.setReadOnly(True)
        self.s3_measurement_output.setObjectName("s3_measurement_output")
        self.groupBox_30 = QtWidgets.QGroupBox(self.currentMeasurements)
        self.groupBox_30.setGeometry(QtCore.QRect(30, 440, 211, 201))
        self.groupBox_30.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_30.setObjectName("groupBox_30")
        self.s5_measurement_output = QtWidgets.QTextEdit(self.groupBox_30)
        self.s5_measurement_output.setGeometry(QtCore.QRect(0, 30, 211, 171))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.s5_measurement_output.setFont(font)
        self.s5_measurement_output.setReadOnly(True)
        self.s5_measurement_output.setObjectName("s5_measurement_output")
        self.tabWidget.addTab(self.currentMeasurements, "")
        self.Alarms = QtWidgets.QWidget()
        self.Alarms.setObjectName("Alarms")
        self.groupBox_18 = QtWidgets.QGroupBox(self.Alarms)
        self.groupBox_18.setGeometry(QtCore.QRect(50, 440, 191, 181))
        self.groupBox_18.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_18.setObjectName("groupBox_18")
        self.groupBox_22 = QtWidgets.QGroupBox(self.groupBox_18)
        self.groupBox_22.setGeometry(QtCore.QRect(40, 20, 151, 80))
        self.groupBox_22.setObjectName("groupBox_22")
        self.s5_T_alarm = QtWidgets.QSpinBox(self.groupBox_22)
        self.s5_T_alarm.setGeometry(QtCore.QRect(10, 20, 91, 51))
        self.s5_T_alarm.setProperty("value", 50)
        self.s5_T_alarm.setObjectName("s5_T_alarm")
        self.label_5 = QtWidgets.QLabel(self.groupBox_22)
        self.label_5.setGeometry(QtCore.QRect(110, 20, 31, 16))
        self.label_5.setObjectName("label_5")
        self.s5_Talarm_cnt_out = QtWidgets.QTextBrowser(self.groupBox_22)
        self.s5_Talarm_cnt_out.setGeometry(QtCore.QRect(110, 40, 31, 31))
        self.s5_Talarm_cnt_out.setObjectName("s5_Talarm_cnt_out")
        self.groupBox_21 = QtWidgets.QGroupBox(self.groupBox_18)
        self.groupBox_21.setGeometry(QtCore.QRect(40, 100, 151, 80))
        self.groupBox_21.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_21.setObjectName("groupBox_21")
        self.s5_H_alarm = QtWidgets.QSpinBox(self.groupBox_21)
        self.s5_H_alarm.setGeometry(QtCore.QRect(10, 20, 91, 51))
        self.s5_H_alarm.setProperty("value", 50)
        self.s5_H_alarm.setObjectName("s5_H_alarm")
        self.s5_Halarm_cnt_out = QtWidgets.QTextBrowser(self.groupBox_21)
        self.s5_Halarm_cnt_out.setGeometry(QtCore.QRect(110, 40, 31, 31))
        self.s5_Halarm_cnt_out.setObjectName("s5_Halarm_cnt_out")
        self.label_8 = QtWidgets.QLabel(self.groupBox_21)
        self.label_8.setGeometry(QtCore.QRect(110, 20, 31, 16))
        self.label_8.setObjectName("label_8")
        self.groupBox_13 = QtWidgets.QGroupBox(self.Alarms)
        self.groupBox_13.setGeometry(QtCore.QRect(50, 20, 201, 191))
        self.groupBox_13.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_13.setCheckable(False)
        self.groupBox_13.setObjectName("groupBox_13")
        self.gb_99 = QtWidgets.QGroupBox(self.groupBox_13)
        self.gb_99.setGeometry(QtCore.QRect(30, 20, 151, 80))
        self.gb_99.setObjectName("gb_99")
        self.s1_T_alarm = QtWidgets.QSpinBox(self.gb_99)
        self.s1_T_alarm.setGeometry(QtCore.QRect(10, 20, 91, 51))
        self.s1_T_alarm.setProperty("value", 50)
        self.s1_T_alarm.setObjectName("s1_T_alarm")
        self.s1_Talarm_cnt_out = QtWidgets.QTextBrowser(self.gb_99)
        self.s1_Talarm_cnt_out.setGeometry(QtCore.QRect(110, 40, 31, 31))
        self.s1_Talarm_cnt_out.setObjectName("s1_Talarm_cnt_out")
        self.label = QtWidgets.QLabel(self.gb_99)
        self.label.setGeometry(QtCore.QRect(110, 20, 31, 16))
        self.label.setObjectName("label")
        self.gb_98 = QtWidgets.QGroupBox(self.groupBox_13)
        self.gb_98.setGeometry(QtCore.QRect(30, 100, 151, 80))
        self.gb_98.setAlignment(QtCore.Qt.AlignCenter)
        self.gb_98.setObjectName("gb_98")
        self.s1_H_alarm = QtWidgets.QSpinBox(self.gb_98)
        self.s1_H_alarm.setGeometry(QtCore.QRect(10, 20, 91, 51))
        self.s1_H_alarm.setProperty("value", 50)
        self.s1_H_alarm.setObjectName("s1_H_alarm")
        self.label_2 = QtWidgets.QLabel(self.gb_98)
        self.label_2.setGeometry(QtCore.QRect(110, 20, 31, 16))
        self.label_2.setObjectName("label_2")
        self.s1_Halarm_cnt_out = QtWidgets.QTextBrowser(self.gb_98)
        self.s1_Halarm_cnt_out.setGeometry(QtCore.QRect(110, 40, 31, 31))
        self.s1_Halarm_cnt_out.setObjectName("s1_Halarm_cnt_out")
        self.groupBox_16 = QtWidgets.QGroupBox(self.Alarms)
        self.groupBox_16.setGeometry(QtCore.QRect(290, 20, 191, 181))
        self.groupBox_16.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_16.setObjectName("groupBox_16")
        self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox_16)
        self.groupBox_10.setGeometry(QtCore.QRect(40, 20, 151, 80))
        self.groupBox_10.setObjectName("groupBox_10")
        self.s2_T_alarm = QtWidgets.QSpinBox(self.groupBox_10)
        self.s2_T_alarm.setGeometry(QtCore.QRect(10, 20, 91, 51))
        self.s2_T_alarm.setProperty("value", 50)
        self.s2_T_alarm.setObjectName("s2_T_alarm")
        self.s2_Talarm_cnt_out = QtWidgets.QTextBrowser(self.groupBox_10)
        self.s2_Talarm_cnt_out.setGeometry(QtCore.QRect(110, 40, 31, 31))
        self.s2_Talarm_cnt_out.setObjectName("s2_Talarm_cnt_out")
        self.label_14 = QtWidgets.QLabel(self.groupBox_10)
        self.label_14.setGeometry(QtCore.QRect(110, 20, 31, 16))
        self.label_14.setObjectName("label_14")
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_16)
        self.groupBox_9.setGeometry(QtCore.QRect(40, 100, 151, 80))
        self.groupBox_9.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_9.setObjectName("groupBox_9")
        self.s2_H_alarm = QtWidgets.QSpinBox(self.groupBox_9)
        self.s2_H_alarm.setGeometry(QtCore.QRect(10, 20, 91, 51))
        self.s2_H_alarm.setProperty("value", 50)
        self.s2_H_alarm.setObjectName("s2_H_alarm")
        self.s2_Halarm_cnt_out = QtWidgets.QTextBrowser(self.groupBox_9)
        self.s2_Halarm_cnt_out.setGeometry(QtCore.QRect(110, 40, 31, 31))
        self.s2_Halarm_cnt_out.setObjectName("s2_Halarm_cnt_out")
        self.label_13 = QtWidgets.QLabel(self.groupBox_9)
        self.label_13.setGeometry(QtCore.QRect(110, 20, 31, 16))
        self.label_13.setObjectName("label_13")
        self.groupBox_17 = QtWidgets.QGroupBox(self.Alarms)
        self.groupBox_17.setGeometry(QtCore.QRect(50, 230, 191, 181))
        self.groupBox_17.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_17.setObjectName("groupBox_17")
        self.groupBox_12 = QtWidgets.QGroupBox(self.groupBox_17)
        self.groupBox_12.setGeometry(QtCore.QRect(30, 20, 161, 80))
        self.groupBox_12.setObjectName("groupBox_12")
        self.s3_T_alarm = QtWidgets.QSpinBox(self.groupBox_12)
        self.s3_T_alarm.setGeometry(QtCore.QRect(10, 20, 91, 51))
        self.s3_T_alarm.setProperty("value", 50)
        self.s3_T_alarm.setObjectName("s3_T_alarm")
        self.label_6 = QtWidgets.QLabel(self.groupBox_12)
        self.label_6.setGeometry(QtCore.QRect(110, 20, 31, 16))
        self.label_6.setObjectName("label_6")
        self.s3_Talarm_cnt_out = QtWidgets.QTextBrowser(self.groupBox_12)
        self.s3_Talarm_cnt_out.setGeometry(QtCore.QRect(110, 40, 31, 31))
        self.s3_Talarm_cnt_out.setObjectName("s3_Talarm_cnt_out")
        self.groupBox_11 = QtWidgets.QGroupBox(self.groupBox_17)
        self.groupBox_11.setGeometry(QtCore.QRect(30, 100, 161, 80))
        self.groupBox_11.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_11.setObjectName("groupBox_11")
        self.s3_H_alarm = QtWidgets.QSpinBox(self.groupBox_11)
        self.s3_H_alarm.setGeometry(QtCore.QRect(10, 20, 91, 51))
        self.s3_H_alarm.setProperty("value", 50)
        self.s3_H_alarm.setObjectName("s3_H_alarm")
        self.label_7 = QtWidgets.QLabel(self.groupBox_11)
        self.label_7.setGeometry(QtCore.QRect(110, 20, 31, 16))
        self.label_7.setObjectName("label_7")
        self.s3_Halarm_cnt_out = QtWidgets.QTextBrowser(self.groupBox_11)
        self.s3_Halarm_cnt_out.setGeometry(QtCore.QRect(110, 40, 31, 31))
        self.s3_Halarm_cnt_out.setObjectName("s3_Halarm_cnt_out")
        self.groupBox_14 = QtWidgets.QGroupBox(self.Alarms)
        self.groupBox_14.setGeometry(QtCore.QRect(290, 230, 191, 181))
        self.groupBox_14.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_14.setObjectName("groupBox_14")
        self.groupBox_20 = QtWidgets.QGroupBox(self.groupBox_14)
        self.groupBox_20.setGeometry(QtCore.QRect(30, 20, 161, 80))
        self.groupBox_20.setObjectName("groupBox_20")
        self.s4_T_alarm = QtWidgets.QSpinBox(self.groupBox_20)
        self.s4_T_alarm.setGeometry(QtCore.QRect(10, 20, 91, 51))
        self.s4_T_alarm.setProperty("value", 50)
        self.s4_T_alarm.setObjectName("s4_T_alarm")
        self.s4_Talarm_cnt_out = QtWidgets.QTextBrowser(self.groupBox_20)
        self.s4_Talarm_cnt_out.setGeometry(QtCore.QRect(110, 40, 31, 31))
        self.s4_Talarm_cnt_out.setObjectName("s4_Talarm_cnt_out")
        self.label_12 = QtWidgets.QLabel(self.groupBox_20)
        self.label_12.setGeometry(QtCore.QRect(110, 20, 31, 16))
        self.label_12.setObjectName("label_12")
        self.groupBox_19 = QtWidgets.QGroupBox(self.groupBox_14)
        self.groupBox_19.setGeometry(QtCore.QRect(30, 100, 161, 80))
        self.groupBox_19.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_19.setObjectName("groupBox_19")
        self.s4_H_alarm = QtWidgets.QSpinBox(self.groupBox_19)
        self.s4_H_alarm.setGeometry(QtCore.QRect(10, 20, 91, 51))
        self.s4_H_alarm.setProperty("value", 50)
        self.s4_H_alarm.setObjectName("s4_H_alarm")
        self.s4_Halarm_cnt_out = QtWidgets.QTextBrowser(self.groupBox_19)
        self.s4_Halarm_cnt_out.setGeometry(QtCore.QRect(110, 40, 31, 31))
        self.s4_Halarm_cnt_out.setObjectName("s4_Halarm_cnt_out")
        self.label_11 = QtWidgets.QLabel(self.groupBox_19)
        self.label_11.setGeometry(QtCore.QRect(110, 20, 31, 16))
        self.label_11.setObjectName("label_11")
        self.groupBox_15 = QtWidgets.QGroupBox(self.Alarms)
        self.groupBox_15.setGeometry(QtCore.QRect(290, 440, 191, 181))
        self.groupBox_15.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_15.setObjectName("groupBox_15")
        self.groupBox_24 = QtWidgets.QGroupBox(self.groupBox_15)
        self.groupBox_24.setGeometry(QtCore.QRect(40, 20, 151, 80))
        self.groupBox_24.setObjectName("groupBox_24")
        self.s6_T_alarm = QtWidgets.QSpinBox(self.groupBox_24)
        self.s6_T_alarm.setGeometry(QtCore.QRect(10, 20, 91, 51))
        self.s6_T_alarm.setProperty("value", 50)
        self.s6_T_alarm.setObjectName("s6_T_alarm")
        self.s6_Talarm_cnt_out = QtWidgets.QTextBrowser(self.groupBox_24)
        self.s6_Talarm_cnt_out.setGeometry(QtCore.QRect(110, 40, 31, 31))
        self.s6_Talarm_cnt_out.setObjectName("s6_Talarm_cnt_out")
        self.label_10 = QtWidgets.QLabel(self.groupBox_24)
        self.label_10.setGeometry(QtCore.QRect(110, 20, 31, 16))
        self.label_10.setObjectName("label_10")
        self.groupBox_23 = QtWidgets.QGroupBox(self.groupBox_15)
        self.groupBox_23.setGeometry(QtCore.QRect(40, 100, 151, 80))
        self.groupBox_23.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_23.setObjectName("groupBox_23")
        self.s6_H_alarm = QtWidgets.QSpinBox(self.groupBox_23)
        self.s6_H_alarm.setGeometry(QtCore.QRect(10, 20, 91, 51))
        self.s6_H_alarm.setProperty("value", 50)
        self.s6_H_alarm.setObjectName("s6_H_alarm")
        self.s6_Halarm_cnt_out = QtWidgets.QTextBrowser(self.groupBox_23)
        self.s6_Halarm_cnt_out.setGeometry(QtCore.QRect(110, 40, 31, 31))
        self.s6_Halarm_cnt_out.setObjectName("s6_Halarm_cnt_out")
        self.label_9 = QtWidgets.QLabel(self.groupBox_23)
        self.label_9.setGeometry(QtCore.QRect(110, 20, 31, 16))
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.Alarms, "")
        self.Errors = QtWidgets.QWidget()
        self.Errors.setObjectName("Errors")
        self.groupBox = QtWidgets.QGroupBox(self.Errors)
        self.groupBox.setGeometry(QtCore.QRect(50, 20, 191, 181))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.s1_error_output = QtWidgets.QTextEdit(self.groupBox)
        self.s1_error_output.setGeometry(QtCore.QRect(0, 30, 191, 151))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.s1_error_output.setFont(font)
        self.s1_error_output.setReadOnly(True)
        self.s1_error_output.setObjectName("s1_error_output")
        self.groupBox_2 = QtWidgets.QGroupBox(self.Errors)
        self.groupBox_2.setGeometry(QtCore.QRect(290, 20, 191, 181))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.s2_error_output = QtWidgets.QTextEdit(self.groupBox_2)
        self.s2_error_output.setGeometry(QtCore.QRect(0, 30, 191, 151))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.s2_error_output.setFont(font)
        self.s2_error_output.setReadOnly(True)
        self.s2_error_output.setObjectName("s2_error_output")
        self.groupBox_3 = QtWidgets.QGroupBox(self.Errors)
        self.groupBox_3.setGeometry(QtCore.QRect(50, 230, 191, 181))
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.s3_error_output = QtWidgets.QTextEdit(self.groupBox_3)
        self.s3_error_output.setGeometry(QtCore.QRect(0, 30, 191, 151))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.s3_error_output.setFont(font)
        self.s3_error_output.setReadOnly(True)
        self.s3_error_output.setObjectName("s3_error_output")
        self.groupBox_4 = QtWidgets.QGroupBox(self.Errors)
        self.groupBox_4.setGeometry(QtCore.QRect(290, 230, 191, 181))
        self.groupBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.s4_error_output = QtWidgets.QTextEdit(self.groupBox_4)
        self.s4_error_output.setGeometry(QtCore.QRect(0, 30, 191, 151))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.s4_error_output.setFont(font)
        self.s4_error_output.setReadOnly(True)
        self.s4_error_output.setObjectName("s4_error_output")
        self.groupBox_5 = QtWidgets.QGroupBox(self.Errors)
        self.groupBox_5.setGeometry(QtCore.QRect(50, 440, 191, 181))
        self.groupBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_5.setObjectName("groupBox_5")
        self.s5_error_output = QtWidgets.QTextEdit(self.groupBox_5)
        self.s5_error_output.setGeometry(QtCore.QRect(0, 30, 191, 151))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.s5_error_output.setFont(font)
        self.s5_error_output.setReadOnly(True)
        self.s5_error_output.setObjectName("s5_error_output")
        self.groupBox_6 = QtWidgets.QGroupBox(self.Errors)
        self.groupBox_6.setGeometry(QtCore.QRect(290, 440, 191, 181))
        self.groupBox_6.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_6.setObjectName("groupBox_6")
        self.s6_error_output = QtWidgets.QTextEdit(self.groupBox_6)
        self.s6_error_output.setGeometry(QtCore.QRect(0, 30, 191, 151))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.s6_error_output.setFont(font)
        self.s6_error_output.setReadOnly(True)
        self.s6_error_output.setObjectName("s6_error_output")
        self.tabWidget.addTab(self.Errors, "")
        self.Graphs = QtWidgets.QWidget()
        self.Graphs.setObjectName("Graphs")
        self.plotWidget = MplWidget(self.Graphs)
        self.plotWidget.setGeometry(QtCore.QRect(0, 0, 531, 601))
        self.plotWidget.setObjectName("plotWidget")
        self.tabWidget.addTab(self.Graphs, "")
        self.Settings = QtWidgets.QWidget()
        self.Settings.setObjectName("Settings")
        self.groupBox_57 = QtWidgets.QGroupBox(self.Settings)
        self.groupBox_57.setGeometry(QtCore.QRect(20, 30, 401, 80))
        self.groupBox_57.setObjectName("groupBox_57")
        self.slider_F_C = QtWidgets.QScrollBar(self.groupBox_57)
        self.slider_F_C.setGeometry(QtCore.QRect(10, 30, 371, 16))
        self.slider_F_C.setMaximum(10)
        self.slider_F_C.setSingleStep(10)
        self.slider_F_C.setOrientation(QtCore.Qt.Horizontal)
        self.slider_F_C.setObjectName("slider_F_C")
        self.label_15 = QtWidgets.QLabel(self.groupBox_57)
        self.label_15.setGeometry(QtCore.QRect(70, 50, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_57)
        self.label_16.setGeometry(QtCore.QRect(260, 50, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.tabWidget.addTab(self.Settings, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 529, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_25.setTitle(_translate("MainWindow", "Sensor 2"))
        self.s2_measurement_output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">72</span><span style=\" font-size:24pt; vertical-align:super;\">o</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">62% RH</span></p></body></html>"))
        self.groupBox_26.setTitle(_translate("MainWindow", "Sensor 4"))
        self.s4_measurement_output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">74</span><span style=\" font-size:24pt; vertical-align:super;\">o</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">64% RH</span></p></body></html>"))
        self.groupBox_27.setTitle(_translate("MainWindow", "Sensor 6"))
        self.s6_measurement_output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">76</span><span style=\" font-size:24pt; vertical-align:super;\">o</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">66% RH</span></p></body></html>"))
        self.groupBox_28.setTitle(_translate("MainWindow", "Sensor 1"))
        self.s1_measurement_output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">71</span><span style=\" font-size:24pt; vertical-align:super;\">o</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">61% RH</span></p></body></html>"))
        self.groupBox_29.setTitle(_translate("MainWindow", "Sensor 3"))
        self.s3_measurement_output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">73</span><span style=\" font-size:24pt; vertical-align:super;\">o</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">63% RH</span></p></body></html>"))
        self.groupBox_30.setTitle(_translate("MainWindow", "Sensor 5"))
        self.s5_measurement_output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">75</span><span style=\" font-size:24pt; vertical-align:super;\">o</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">65% RH</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.currentMeasurements), _translate("MainWindow", "Current"))
        self.groupBox_18.setTitle(_translate("MainWindow", "Sensor 5"))
        self.groupBox_22.setTitle(_translate("MainWindow", "Temperature"))
        self.label_5.setText(_translate("MainWindow", "Count"))
        self.groupBox_21.setTitle(_translate("MainWindow", "Humidity"))
        self.label_8.setText(_translate("MainWindow", "Count"))
        self.groupBox_13.setTitle(_translate("MainWindow", "Sensor 1"))
        self.gb_99.setTitle(_translate("MainWindow", "Temperature"))
        self.label.setText(_translate("MainWindow", "Count"))
        self.gb_98.setTitle(_translate("MainWindow", "Humidity"))
        self.label_2.setText(_translate("MainWindow", "Count"))
        self.groupBox_16.setTitle(_translate("MainWindow", "Sensor 2"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Temperature"))
        self.label_14.setText(_translate("MainWindow", "Count"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Humidity"))
        self.label_13.setText(_translate("MainWindow", "Count"))
        self.groupBox_17.setTitle(_translate("MainWindow", "Sensor 3"))
        self.groupBox_12.setTitle(_translate("MainWindow", "Temperature"))
        self.label_6.setText(_translate("MainWindow", "Count"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Humidity"))
        self.label_7.setText(_translate("MainWindow", "Count"))
        self.groupBox_14.setTitle(_translate("MainWindow", "Sensor 4"))
        self.groupBox_20.setTitle(_translate("MainWindow", "Temperature"))
        self.label_12.setText(_translate("MainWindow", "Count"))
        self.groupBox_19.setTitle(_translate("MainWindow", "Humidity"))
        self.label_11.setText(_translate("MainWindow", "Count"))
        self.groupBox_15.setTitle(_translate("MainWindow", "Sensor 6"))
        self.groupBox_24.setTitle(_translate("MainWindow", "Temperature"))
        self.label_10.setText(_translate("MainWindow", "Count"))
        self.groupBox_23.setTitle(_translate("MainWindow", "Humidity"))
        self.label_9.setText(_translate("MainWindow", "Count"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Alarms), _translate("MainWindow", "Alarms"))
        self.groupBox.setTitle(_translate("MainWindow", "Sensor 1"))
        self.s1_error_output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:32pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Error</span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Sensor 2"))
        self.s2_error_output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:32pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Errors</span></p></body></html>"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Sensor 3"))
        self.s3_error_output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:32pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Errors</span></p></body></html>"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Sensor 4"))
        self.s4_error_output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:32pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">4</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Errors</span></p></body></html>"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Sensor 5"))
        self.s5_error_output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:32pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">5</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Errors</span></p></body></html>"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Sensor 6"))
        self.s6_error_output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:32pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">6</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Errors</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Errors), _translate("MainWindow", "Errors"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Graphs), _translate("MainWindow", "Graphs"))
        self.groupBox_57.setTitle(_translate("MainWindow", "Display Temperature Setting"))
        self.label_15.setText(_translate("MainWindow", "Fahrenheit"))
        self.label_16.setText(_translate("MainWindow", "Celcius"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Settings), _translate("MainWindow", "Settings"))
from mplwidget import MplWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
