#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: ofdm_final
# Author: Priyanka
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

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
import numpy
from gnuradio import digital
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore



from gnuradio import qtgui

class ofdm_final(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "ofdm_final", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("ofdm_final")
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

        self.settings = Qt.QSettings("GNU Radio", "ofdm_final")

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
        self.samp_rate = samp_rate = 32000*2
        self.noise = noise = 0
        self.delay_val = delay_val = 0

        ##################################################
        # Blocks
        ##################################################
        self._noise_range = Range(0, 1, 0.1, 0, 200)
        self._noise_win = RangeWidget(self._noise_range, self.set_noise, "'noise'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._noise_win)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=4,
                decimation=1,
                taps=firdes.root_raised_cosine(4,1,0.25,0.35,100),
                fractional_bw=0)
        self.qtgui_sink_x_0_0 = qtgui.sink_c(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "transmit", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_0_win)
        self.qtgui_const_sink_x_1 = qtgui.const_sink_c(
            1024, #size
            "Received", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_1.set_update_time(0.10)
        self.qtgui_const_sink_x_1.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_1.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1.enable_autoscale(True)
        self.qtgui_const_sink_x_1.enable_grid(False)
        self.qtgui_const_sink_x_1.enable_axis_labels(True)


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

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_1_win = sip.wrapinstance(self.qtgui_const_sink_x_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_1_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            1024, #size
            "Transmit", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


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

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_ccc(1, ((1,0,0)))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.fft_vxx_0_0_0 = fft.fft_vcc(4, False, window.rectangular(4), True, 1)
        self.fft_vxx_0_0 = fft.fft_vcc(4, True, window.rectangular(4), True, 1)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_ic(((0.707+0.707j,-0.707+0.707j,-0.707-0.707j,0.707-0.707j)), 1)
        self._delay_val_range = Range(0, 10, 1, 0, 200)
        self._delay_val_win = RangeWidget(self._delay_val_range, self.set_delay_val, "'delay_val'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._delay_val_win)
        self.blocks_vector_to_stream_2 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, 4)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, 4)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 4)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 4)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_interleave_0_0 = blocks.interleave(gr.sizeof_gr_complex*1, 1)
        self.blocks_interleave_0 = blocks.interleave(gr.sizeof_gr_complex*1, 1)
        self.blocks_deinterleave_0_0_0 = blocks.deinterleave(gr.sizeof_gr_complex*1, 1)
        self.blocks_deinterleave_0_0 = blocks.deinterleave(gr.sizeof_gr_complex*1, 1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_random_source_x_0 = blocks.vector_source_i(list(map(int, numpy.random.randint(0, 4, 1000))), True)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, noise, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_random_source_x_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_deinterleave_0_0, 0))
        self.connect((self.blocks_deinterleave_0_0, 2), (self.blocks_interleave_0_0, 0))
        self.connect((self.blocks_deinterleave_0_0, 3), (self.blocks_interleave_0_0, 1))
        self.connect((self.blocks_deinterleave_0_0, 4), (self.blocks_interleave_0_0, 2))
        self.connect((self.blocks_deinterleave_0_0, 5), (self.blocks_interleave_0_0, 3))
        self.connect((self.blocks_deinterleave_0_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_deinterleave_0_0, 1), (self.blocks_null_sink_0, 1))
        self.connect((self.blocks_deinterleave_0_0_0, 2), (self.blocks_interleave_0, 0))
        self.connect((self.blocks_deinterleave_0_0_0, 0), (self.blocks_interleave_0, 2))
        self.connect((self.blocks_deinterleave_0_0_0, 3), (self.blocks_interleave_0, 1))
        self.connect((self.blocks_deinterleave_0_0_0, 1), (self.blocks_interleave_0, 3))
        self.connect((self.blocks_deinterleave_0_0_0, 3), (self.blocks_interleave_0, 5))
        self.connect((self.blocks_deinterleave_0_0_0, 2), (self.blocks_interleave_0, 4))
        self.connect((self.blocks_interleave_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.blocks_interleave_0_0, 0), (self.blocks_stream_to_vector_0_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0_0_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.fft_vxx_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.qtgui_const_sink_x_1, 0))
        self.connect((self.blocks_vector_to_stream_2, 0), (self.blocks_deinterleave_0_0_0, 0))
        self.connect((self.blocks_vector_to_stream_2, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.fft_vxx_0_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.fft_vxx_0_0_0, 0), (self.blocks_vector_to_stream_2, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_sink_x_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ofdm_final")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_sink_x_0_0.set_frequency_range(0, self.samp_rate)

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self.analog_noise_source_x_0.set_amplitude(self.noise)

    def get_delay_val(self):
        return self.delay_val

    def set_delay_val(self, delay_val):
        self.delay_val = delay_val




def main(top_block_cls=ofdm_final, options=None):

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
