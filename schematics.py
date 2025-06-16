#!/usr/bin/python

import math
import inkscapeMadeEasy.inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy.inkscapeMadeEasy_Draw as inkDraw

from opts import Opts

from draw_rlc import DrawRLC
from draw_tran import DrawTran


class Schematics(DrawRLC, DrawTran):
    def __init__(self):
        inkBase.inkscapeMadeEasy.__init__(self)

        self.arg_parser.add_argument("--action", dest="action")
        self.arg_parser.add_argument("--rlc_type", dest="rlc_type")
        self.arg_parser.add_argument("--rlc_do_variable", type=self.bool, dest="rlc_do_variable")
        self.arg_parser.add_argument("--rlc_draw_opts", dest="rlc_draw_opts")
        self.arg_parser.add_argument("--rlc_do_value", type=self.bool, dest="rlc_do_value")
        self.arg_parser.add_argument("--rlc_value", dest="rlc_value")
        self.arg_parser.add_argument("--rlc_do_unit", type=self.bool, dest="rlc_do_unit")
        self.arg_parser.add_argument("--rlc_do_latex_value", type=self.bool, dest="rlc_do_latex_value")

        self.arg_parser.add_argument("--tran_type", dest="tran_type")

        self.arg_parser.add_argument("--bjt_type", dest="bjt_type")
        self.arg_parser.add_argument("--bjt_igbt", type=self.bool, dest="bjt_igbt")
        self.arg_parser.add_argument("--bjt_photo", type=self.bool, dest="bjt_photo")
        self.arg_parser.add_argument("--bjt_switch", type=self.bool, dest="bjt_switch")

        self.arg_parser.add_argument("--fet_type", dest="fet_type")
        self.arg_parser.add_argument("--fet_symbol", dest="fet_symbol")
        self.arg_parser.add_argument("--fet_channel", dest="fet_channel")
        self.arg_parser.add_argument("--fet_switch", type=self.bool, dest="fet_switch")

        self.arg_parser.add_argument("--tran_orientation", dest="tran_orientation")
        self.arg_parser.add_argument("--tran_do_envelope", type=self.bool, dest="tran_do_envelope")
        self.arg_parser.add_argument("--tran_do_extra", type=self.bool, dest="tran_do_extra")
        self.arg_parser.add_argument("--tran_extra", dest="tran_extra")

        self.arg_parser.add_argument("--diode_type", dest="diode_type")
        self.arg_parser.add_argument("--diode_draw_opts", dest="diode_draw_opts")

        self.arg_parser.add_argument("--do_designator", type=self.bool, dest="do_designator")
        self.arg_parser.add_argument("--designator", dest="designator")
        self.arg_parser.add_argument("--do_latex_math", type=self.bool, dest="do_latex_math")

    def effect(self):
        opts = Opts(self.options)

        root_layer = self.document.getroot()
       
        position = [self.svg.namedview.center[0], self.svg.namedview.center[1]]
        position[0] = int(math.ceil(position[0] / 10.0)) * 10
        position[1] = int(math.ceil(position[1] / 10.0)) * 10

        if opts.do_latex_math:
            opts.designator = '$' + opts.designator + '$'

        if opts.action == "rlc":
            opts.rlc.value = self.parse_value(opts)
            if opts.rlc.type == "res":
                self.draw_resistor(root_layer, position, opts)
            elif opts.rlc.type == "cap":
                self.draw_capacitor(root_layer, position, opts)
            elif opts.rlc.type == "polcap":
                self.draw_polcapacitor(root_layer, position, opts)
            elif opts.rlc.type == "ind":
                self.draw_inductor(root_layer, position, opts)
            elif opts.rlc.type == "pot":
                self.draw_potentiometer(root_layer, position, opts)

        elif opts.action == "tran":
            if opts.tran.type == "bjt":
                if opts.tran.bjt.igbt:
                    self.draw_igbt(root_layer, position, opts)
                else:
                    self.draw_bjt(root_layer, position, opts)
            elif opts.tran.type == "fet":
                if opts.tran.fet.type == "mos_e" or opts.tran.fet.type == "mos_d":
                    self.draw_mosfet(root_layer, position, opts)
                elif opts.tran.fet.type == "jfet":
                    self.draw_jfet(root_layer, position, opts)
                elif opts.tran.fet.type == "cmos_e" or opts.tran.fet.type == "cmos_d":
                    self.draw_cmos(root_layer, position, opts)

        elif opts.action == "diode":
            pass


# class TextOpts:
#     def __init__(self) -> None:
#         self.font_size = 5
#         self.font_size_small = 4
#         self.text_offset = self.font_size / 1.5
#         self.text_offset_small = self.font_size_small / 2


if __name__ == '__main__':
    ext = Schematics()
    ext.run()
