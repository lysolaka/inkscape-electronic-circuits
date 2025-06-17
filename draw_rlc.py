import numpy as np

import inkscapeMadeEasy.inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy.inkscapeMadeEasy_Draw as inkDraw

from opts import Opts

RLC_UNIT = {
    "res": r"\si\ohm",
    "cap": r"\si\farad",
    "polcap": r"\si\farad",
    "ind": r"\si\henry",
    "pot": r"\si\ohm"
}

RLC_MUL = {
    "f": r"\text{f}",
    "p": r"\text{p}",
    "n": r"\text{n}",
    "u": r"\mu",
    "m": r"\text{m}",
    "k": r"\text{k}",
    "M": r"\text{M}",
    "G": r"\text{G}"
}


class DrawRLC(inkBase.inkscapeMadeEasy):
    def add(self, vector, delta):
        return vector + np.array(delta)

    def parse_value(self, opts: Opts) -> str:
        value = opts.rlc.value
        if opts.rlc.do_latex_value:
            if value[-1] in RLC_MUL:
                value = value[:-1] + RLC_MUL[value[-1]]
            if opts.rlc.do_unit:
                value += RLC_UNIT[opts.rlc.type]
            value = "$" + value + "$"

        return value

    def draw_label_rlc(
        self,
        group,
        position: list[int],
        opts: Opts,
        size: float,
        hor_off: float,
    ):
        if opts.rlc.do_variable:
            upper_pos = self.add(position, [0, -(size + 2)])
            lower_pos = self.add(position, [0, size + 2])
        else:
            upper_pos = self.add(position, [0, -size])
            lower_pos = self.add(position, [0, size])

        side_pos = self.add(position, [size, 0])
        upper_side_pos = self.add(position, [size, -hor_off])
        lower_side_pos = self.add(position, [size, hor_off])

        if opts.rlc.do_value and opts.do_designator:
            if opts.rlc.draw_opts == "vertical":
                inkDraw.text.latex(
                    self,
                    group,
                    opts.designator,
                    upper_side_pos,
                    fontSize=5,
                    refPoint="bl",
                )
                inkDraw.text.latex(
                    self,
                    group,
                    opts.rlc.value,
                    lower_side_pos,
                    fontSize=5,
                    refPoint="tl",
                )
            elif opts.rlc.draw_opts == "horizontal":
                inkDraw.text.latex(
                    self,
                    group,
                    opts.designator,
                    upper_pos,
                    fontSize=5,
                    refPoint="bc",
                )
                inkDraw.text.latex(
                    self, group, opts.rlc.value, lower_pos, fontSize=5, refPoint="tc"
                )
        elif opts.rlc.do_value:
            if opts.rlc.draw_opts == "vertical":
                inkDraw.text.latex(
                    self, group, opts.rlc.value, side_pos, fontSize=5, refPoint="cl"
                )
            elif opts.rlc.draw_opts == "horizontal":
                inkDraw.text.latex(
                    self, group, opts.rlc.value, upper_pos, fontSize=5, refPoint="bc"
                )
        elif opts.do_designator:
            if opts.rlc.draw_opts == "vertical":
                inkDraw.text.latex(
                    self, group, opts.designator, side_pos, fontSize=5, refPoint="cl"
                )
            elif opts.rlc.draw_opts == "horizontal":
                inkDraw.text.latex(
                    self,
                    group,
                    opts.designator,
                    upper_pos,
                    fontSize=5,
                    refPoint="bc",
                )

    def draw_resistor(self, parent, position: list[int], opts: Opts):
        group = self.createGroup(parent, "Resistor")
        elem = self.createGroup(group)

        inkDraw.line.relCoords(elem, [[-5.5, 0]], self.add(position, [-9.5, 0]))
        inkDraw.line.relCoords(
            elem,
            [[19, 0], [0, -6], [-19, 0], [0, 6]],
            self.add(position, [-9.5, 3]),
        )
        inkDraw.line.relCoords(elem, [[5.5, 0]], self.add(position, [9.5, 0]))

        if opts.rlc.do_variable:
            color = inkDraw.color.defined("black")
            arrow_len = 2.5
            marker_path = "M 0,0 l -%f,%f l 0,-%f z" % (
                arrow_len * 1.2,
                arrow_len / 2.0,
                arrow_len,
            )
            marker_arr = inkDraw.marker.createMarker(
                self,
                "arrow",
                marker_path,
                RenameMode=0,
                strokeColor=color,
                fillColor=color,
                lineWidth=0.6,
                markerTransform="translate (1,0)",
            )
            line_style = inkDraw.lineStyle.set(
                lineWidth=1, lineColor=color, markerEnd=marker_arr
            )

            inkDraw.line.relCoords(
                elem,
                [[20, -12]],
                self.add(position, [-10, 6]),
                lineStyle=line_style,
            )

        if opts.rlc.draw_opts == "vertical":
            self.rotateElement(elem, position, 90)

        self.draw_label_rlc(group, position, opts, 6, 1.5)

    def draw_capacitor(self, parent, position: list[int], opts: Opts):
        group = self.createGroup(parent, "Capacitor")
        elem = self.createGroup(group)

        inkDraw.line.relCoords(elem, [[13, 0]], self.add(position, [2, 0]))
        inkDraw.line.relCoords(elem, [[0, -14]], self.add(position, [2, 7]))
        inkDraw.line.relCoords(elem, [[-13, 0]], self.add(position, [-2, 0]))
        inkDraw.line.relCoords(elem, [[0, -14]], self.add(position, [-2, 7]))

        if opts.rlc.do_variable:
            color = inkDraw.color.defined("black")
            arrow_len = 2.5
            marker_path = "M 0,0 l -%f,%f l 0,-%f z" % (
                arrow_len * 1.2,
                arrow_len / 2.0,
                arrow_len,
            )
            marker_arr = inkDraw.marker.createMarker(
                self,
                "arrow",
                marker_path,
                RenameMode=0,
                strokeColor=color,
                fillColor=color,
                lineWidth=0.6,
                markerTransform="translate (1,0)",
            )
            line_style = inkDraw.lineStyle.set(
                lineWidth=1, lineColor=color, markerEnd=marker_arr
            )

            inkDraw.line.relCoords(
                elem,
                [[20, -12]],
                self.add(position, [-10, 6]),
                lineStyle=line_style,
            )

        if opts.rlc.draw_opts == "vertical":
            self.rotateElement(elem, position, 90)

        self.draw_label_rlc(group, position, opts, 10, 3)

    def draw_polcapacitor(self, parent, position: list[int], opts: Opts):
        group = self.createGroup(parent, "Polarized Capacitor")
        elem = self.createGroup(group)

        black_fill = inkDraw.lineStyle.set(
            fillColor=inkDraw.color.defined("black")
        )
        plus_sign = inkDraw.lineStyle.setSimpleBlack(0.6)

        inkDraw.line.relCoords(elem, [[11, 0]], self.add(position, [5, 0]))
        inkDraw.rectangle.corners(
            elem, [0, 0], [-3, -14], offset=self.add(position, [5, 7])
        )
        inkDraw.line.relCoords(elem, [[-11, 0]], self.add(position, [-4, 0]))
        inkDraw.rectangle.corners(
            elem,
            [0, 0],
            [2, -14],
            offset=self.add(position, [-4, 7]),
            lineStyle=black_fill,
        )

        if opts.rlc.draw_opts == "vertical":
            inkDraw.line.relCoords(
                elem,
                [[-3, 0]],
                self.add(position, [9.5, 4]),
                lineStyle=plus_sign,
            )
            inkDraw.line.relCoords(
                elem,
                [[0, -3]],
                self.add(position, [8, 5.5]),
                lineStyle=plus_sign,
            )
        else:
            inkDraw.line.relCoords(
                elem,
                [[-3, 0]],
                self.add(position, [9.5, -4]),
                lineStyle=plus_sign,
            )
            inkDraw.line.relCoords(
                elem,
                [[0, 3]],
                self.add(position, [8, -5.5]),
                lineStyle=plus_sign,
            )

        if opts.rlc.do_variable:
            color = inkDraw.color.defined("black")
            arrow_len = 2.5
            marker_path = "M 0,0 l -%f,%f l 0,-%f z" % (
                arrow_len * 1.2,
                arrow_len / 2.0,
                arrow_len,
            )
            marker_arr = inkDraw.marker.createMarker(
                self,
                "arrow",
                marker_path,
                RenameMode=0,
                strokeColor=color,
                fillColor=color,
                lineWidth=0.6,
                markerTransform="translate (1,0)",
            )
            line_style = inkDraw.lineStyle.set(
                lineWidth=1, lineColor=color, markerEnd=marker_arr
            )

            inkDraw.line.relCoords(
                elem,
                [[20, -12]],
                self.add(position, [-10, 6]),
                lineStyle=line_style,
            )

        if opts.rlc.draw_opts == "vertical":
            self.rotateElement(elem, position, 90)

        self.draw_label_rlc(group, position, opts, 10, 3)

    def draw_inductor(self, parent, position: list[int], opts: Opts):
        group = self.createGroup(parent, "Inductor")
        elem = self.createGroup(group)

        inkDraw.line.relCoords(elem, [[-3, 0]], self.add(position, [-12, 0]))
        inkDraw.line.relCoords(elem, [[3, 0]], self.add(position, [12, 0]))

        inkDraw.arc.centerAngStartAngEnd(
            elem,
            self.add(position, [-9, 0]),
            3.0,
            0.0,
            180.0,
            [0, 0],
            largeArc=True,
        )
        inkDraw.arc.centerAngStartAngEnd(
            elem,
            self.add(position, [-3, 0]),
            3.0,
            0.0,
            180.0,
            [0, 0],
            largeArc=True,
        )
        inkDraw.arc.centerAngStartAngEnd(
            elem,
            self.add(position, [3, 0]),
            3.0,
            0.0,
            180.0,
            [0, 0],
            largeArc=True,
        )
        inkDraw.arc.centerAngStartAngEnd(
            elem,
            self.add(position, [9, 0]),
            3.0,
            0.0,
            180.0,
            [0, 0],
            largeArc=True,
        )

        if opts.rlc.do_variable:
            color = inkDraw.color.defined("black")
            arrow_len = 2.5
            marker_path = "M 0,0 l -%f,%f l 0,-%f z" % (
                arrow_len * 1.2,
                arrow_len / 2.0,
                arrow_len,
            )
            marker_arr = inkDraw.marker.createMarker(
                self,
                "arrow",
                marker_path,
                RenameMode=0,
                strokeColor=color,
                fillColor=color,
                lineWidth=0.6,
                markerTransform="translate (1,0)",
            )
            line_style = inkDraw.lineStyle.set(
                lineWidth=1, lineColor=color, markerEnd=marker_arr
            )

            inkDraw.line.relCoords(
                elem,
                [[20, -12]],
                self.add(position, [-10, 6]),
                lineStyle=line_style,
            )

        if opts.rlc.draw_opts == "vertical":
            self.rotateElement(elem, position, -90)

        self.draw_label_rlc(group, position, opts, 6, 1.5)

    def draw_potentiometer(self, parent, position: list[int], opts: Opts):
        group = self.createGroup(parent, "Potentiometer")
        elem = self.createGroup(group)

        color = inkDraw.color.defined("black")
        arrow_len = 2.5
        marker_path = "M 0,0 l -%f,%f l 0,-%f z" % (
            arrow_len * 1.2,
            arrow_len / 2.0,
            arrow_len,
        )
        marker_arr = inkDraw.marker.createMarker(
            self,
            "PotentiometerArrow",
            marker_path,
            RenameMode=0,
            strokeColor=color,
            fillColor=color,
            lineWidth=0.6,
            markerTransform="translate (1,0)",
        )
        line_style_arr = inkDraw.lineStyle.set(
            lineWidth=1, lineColor=color, markerEnd=marker_arr
        )

        inkDraw.line.relCoords(
            elem, [[-5.5, 0]], self.add(position, [-9.5, 0])
        )
        inkDraw.line.relCoords(
            elem,
            [[19, 0], [0, -6], [-19, 0], [0, 6]],
            self.add(position, [-9.5, 3]),
        )
        inkDraw.line.relCoords(
            elem, [[5.5, 0]], self.add(position, [9.5, 0])
        )

        inkDraw.line.relCoords(
            elem,
            [[0, -10]],
            self.add(position, [0, 15]),
            lineStyle=line_style_arr,
        )

        if opts.rlc.draw_opts == "vertical":
            self.rotateElement(elem, position, 90)

        upper_pos = self.add(position, [0, -6])

        side_pos = self.add(position, [-6, 0])
        upper_side_pos = self.add(position, [-6, -1.5])
        lower_side_pos = self.add(position, [-6, 1.5])

        if opts.rlc.do_value and opts.do_designator:
            if opts.rlc.draw_opts == "vertical":
                inkDraw.text.latex(
                    self,
                    group,
                    opts.designator,
                    upper_side_pos,
                    fontSize=5,
                    refPoint="br",
                )
                inkDraw.text.latex(
                    self,
                    group,
                    opts.rlc.value,
                    lower_side_pos,
                    fontSize=5,
                    refPoint="tr",
                )
            elif opts.rlc.draw_opts == "horizontal":
                inkDraw.text.latex(
                    self,
                    group,
                    opts.rlc.value,
                    upper_pos,
                    fontSize=5,
                    refPoint="bc",
                )
                inkDraw.text.latex(
                    self,
                    group,
                    opts.designator,
                    self.add(upper_pos, [0, -7.5]),
                    fontSize=5,
                    refPoint="bc",
                )
        elif opts.rlc.do_value:
            if opts.rlc.draw_opts == "vertical":
                inkDraw.text.latex(
                    self, group, opts.rlc.value, side_pos, fontSize=5, refPoint="cr"
                )
            elif opts.rlc.draw_opts == "horizontal":
                inkDraw.text.latex(
                    self, group, opts.rlc.value, upper_pos, fontSize=5, refPoint="bc"
                )
        elif opts.do_designator:
            if opts.rlc.draw_opts == "vertical":
                inkDraw.text.latex(
                    self, group, opts.designator, side_pos, fontSize=5, refPoint="cr"
                )
            elif opts.rlc.draw_opts == "horizontal":
                inkDraw.text.latex(
                    self,
                    group,
                    opts.designator,
                    upper_pos,
                    fontSize=5,
                    refPoint="bc",
                )
