#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: mimo_svd
# Author: priyanka
# GNU Radio version: 3.10.3.0

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt5 import Qt
from gnuradio import qtgui
import sip
from gnuradio import analog
from gnuradio import blocks
import numpy
from gnuradio import digital
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
from ofdm_pb import ofdm_pb  # grc-generated hier_block
from ofdmpbrx import ofdmpbrx  # grc-generated hier_block
import mimo_ofdm_pb_svd2 as svd2  # embedded python module
import mimo_ofdm_pb_svd_pb as svd_pb  # embedded python module



from gnuradio import qtgui

class mimo_ofdm_pb(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "mimo_svd", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("mimo_svd")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "mimo_ofdm_pb")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.noise_2 = noise_2 = 0
        self.noise_1 = noise_1 = 0

        ##################################################
        # Blocks
        ##################################################
        self._noise_2_range = Range(0, 1, .1, 0, 200)
        self._noise_2_win = RangeWidget(self._noise_2_range, self.set_noise_2, "'noise_2'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._noise_2_win)
        self._noise_1_range = Range(0, 1, .1, 0, 200)
        self._noise_1_win = RangeWidget(self._noise_1_range, self.set_noise_1, "'noise_1'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._noise_1_win)
        self.qtgui_const_sink_x_0_0_0_1 = qtgui.const_sink_c(
            1024, #size
            "Transmit", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0_0_0_1.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_0_1.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0_0_0_1.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_0_1.enable_autoscale(True)
        self.qtgui_const_sink_x_0_0_0_1.enable_grid(False)
        self.qtgui_const_sink_x_0_0_0_1.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_0_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_0_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_0_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_0_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_0_1_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_0_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_0_0_1_win)
        self.qtgui_const_sink_x_0_0_0 = qtgui.const_sink_c(
            1024, #size
            "Received", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0_0_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_0_0_win)
        self.ofdmpbrx_0_0 = ofdmpbrx()
        self.ofdmpbrx_0 = ofdmpbrx()
        self.ofdm_pb_0_0 = ofdm_pb(
            tap0=1,
        )
        self.ofdm_pb_0 = ofdm_pb(
            tap0=1,
        )
        self.interp_fir_filter_xxx_0_0_0_0 = filter.interp_fir_filter_ccc(1, ((-1,0)))
        self.interp_fir_filter_xxx_0_0_0_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0_0_0 = filter.interp_fir_filter_ccc(1, ((1,0)))
        self.interp_fir_filter_xxx_0_0_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0_0 = filter.interp_fir_filter_ccc(1, ((1,0)))
        self.interp_fir_filter_xxx_0_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_ccc(1, ((1,0)))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_bc(((1+1j,-1+1j,-1-1j,1-1j)), 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_matrix_xx_0_0 = blocks.multiply_matrix_cc(((-0.7071067811865472, -0.7071067811865475), (-0.7071067811865475, 0.7071067811865476)), gr.TPP_ALL_TO_ALL)
        self.blocks_multiply_matrix_xx_0 = blocks.multiply_matrix_cc(((-1,0),(0,-1)), gr.TPP_ALL_TO_ALL)
        self.blocks_deinterleave_0 = blocks.deinterleave(gr.sizeof_gr_complex*1, 1)
        self.blocks_add_xx_0_0 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_random_source_x_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 4, 10000))), True)
        self.analog_noise_source_x_0_0 = analog.noise_source_c(analog.GR_GAUSSIAN, noise_1, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, noise_2, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0_0, 2))
        self.connect((self.analog_noise_source_x_0_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.analog_random_source_x_0, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.ofdmpbrx_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.ofdmpbrx_0_0, 0))
        self.connect((self.blocks_deinterleave_0, 0), (self.blocks_multiply_matrix_xx_0, 0))
        self.connect((self.blocks_deinterleave_0, 1), (self.blocks_multiply_matrix_xx_0, 1))
        self.connect((self.blocks_deinterleave_0, 0), (self.qtgui_const_sink_x_0_0_0_1, 0))
        self.connect((self.blocks_deinterleave_0, 1), (self.qtgui_const_sink_x_0_0_0_1, 1))
        self.connect((self.blocks_multiply_matrix_xx_0, 0), (self.ofdm_pb_0, 0))
        self.connect((self.blocks_multiply_matrix_xx_0, 1), (self.ofdm_pb_0_0, 0))
        self.connect((self.blocks_multiply_matrix_xx_0_0, 0), (self.qtgui_const_sink_x_0_0_0, 0))
        self.connect((self.blocks_multiply_matrix_xx_0_0, 1), (self.qtgui_const_sink_x_0_0_0, 1))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_deinterleave_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.interp_fir_filter_xxx_0_0_0_0, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.ofdm_pb_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.ofdm_pb_0, 0), (self.interp_fir_filter_xxx_0_0, 0))
        self.connect((self.ofdm_pb_0_0, 0), (self.interp_fir_filter_xxx_0_0_0, 0))
        self.connect((self.ofdm_pb_0_0, 0), (self.interp_fir_filter_xxx_0_0_0_0, 0))
        self.connect((self.ofdmpbrx_0, 0), (self.blocks_multiply_matrix_xx_0_0, 0))
        self.connect((self.ofdmpbrx_0_0, 0), (self.blocks_multiply_matrix_xx_0_0, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "mimo_ofdm_pb")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_noise_2(self):
        return self.noise_2

    def set_noise_2(self, noise_2):
        self.noise_2 = noise_2
        self.analog_noise_source_x_0.set_amplitude(self.noise_2)

    def get_noise_1(self):
        return self.noise_1

    def set_noise_1(self, noise_1):
        self.noise_1 = noise_1
        self.analog_noise_source_x_0_0.set_amplitude(self.noise_1)




def main(top_block_cls=mimo_ofdm_pb, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
