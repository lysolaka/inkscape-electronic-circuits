import numpy as np

import inkscapeMadeEasy.inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy.inkscapeMadeEasy_Draw as inkDraw

from opts import Opts

SRC_MUL = {
    "f": r"\text{f}",
    "p": r"\text{p}",
    "n": r"\text{n}",
    "u": r"\mu",
    "m": r"\text{m}",
    "k": r"\text{k}",
    "M": r"\text{M}",
    "G": r"\text{G}",
}


class DrawSource(inkBase.inkscapeMadeEasy):
    def add(self, vector, delta):
        return vector + np.array(delta)

    def parse_value_source(self, opts: Opts):
        value = opts.source.value
        if opts.source.do_latex_value and value is not None:
            if value[-1] in SRC_MUL:
                value = value[:-1] + SRC_MUL[value[-1]]
            if opts.source.do_unit:
                if opts.source.type in ["voltage", "voltage_ac"]:
                    unit = r"\si\volt"
                elif opts.source.type in ["current_1", "current_2"]:
                    unit = r"\si\ampere"
                value += unit
            value = "$" + value + "$"

        return value

    def draw_label_source(
        self, group, position: list[int], opts: Opts, size: float
    ):
        upper_pos = self.add(position, [0, -size])
        lower_pos = self.add(position, [0, size])

        side_pos = self.add(position, [size, 0])
        upper_side_pos = self.add(position, [size, -1.5])
        lower_side_pos = self.add(position, [size, 1.5])

        if opts.source.do_value and opts.do_designator:
            if opts.source.draw_opts == "vertical":
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
                    opts.source.value,
                    lower_side_pos,
                    fontSize=5,
                    refPoint="tl",
                )
            elif opts.source.draw_opts == "horizontal":
                inkDraw.text.latex(
                    self,
                    group,
                    opts.designator,
                    upper_pos,
                    fontSize=5,
                    refPoint="bc",
                )
                inkDraw.text.latex(
                    self,
                    group,
                    opts.source.value,
                    lower_pos,
                    fontSize=5,
                    refPoint="tc",
                )
        elif opts.source.do_value:
            if opts.source.draw_opts == "vertical":
                inkDraw.text.latex(
                    self,
                    group,
                    opts.source.value,
                    side_pos,
                    fontSize=5,
                    refPoint="cl",
                )
            elif opts.source.draw_opts == "horizontal":
                inkDraw.text.latex(
                    self,
                    group,
                    opts.source.value,
                    upper_pos,
                    fontSize=5,
                    refPoint="bc",
                )
        elif opts.do_designator:
            if opts.source.draw_opts == "vertical":
                inkDraw.text.latex(
                    self,
                    group,
                    opts.designator,
                    side_pos,
                    fontSize=5,
                    refPoint="cl",
                )
            elif opts.source.draw_opts == "horizontal":
                inkDraw.text.latex(
                    self,
                    group,
                    opts.designator,
                    upper_pos,
                    fontSize=5,
                    refPoint="bc",
                )

    def draw_voltage(self, parent, position: list[int], opts: Opts):
        group = self.createGroup(parent, "Voltage")
        elem = self.createGroup(group, "Voltage")

        inkDraw.line.relCoords(elem, [[-8, 0]], self.add(position, [-7, 0]))
        inkDraw.line.relCoords(elem, [[8, 0]], self.add(position, [7, 0]))
        inkDraw.circle.centerRadius(elem, position, 7)

        line_style_arr = inkDraw.lineStyle.set(
            lineWidth=0.7,
            fillColor=inkDraw.color.defined("black"),
        )
        if opts.source.do_invert:
            inkDraw.line.relCoords(
                elem,
                [[-5, 0], [0, 1.2], [-3, -1.2], [3, -1.2], [0, 1.2]],
                self.add(position, [4, 0]),
                lineStyle=line_style_arr,
            )
        else:
            inkDraw.line.relCoords(
                elem,
                [[5, 0], [0, 1.2], [3, -1.2], [-3, -1.2], [0, 1.2]],
                self.add(position, [-4, 0]),
                lineStyle=line_style_arr,
            )

        if opts.source.draw_opts == "vertical":
            self.rotateElement(elem, position, 90)

        self.draw_label_source(group, position, opts, 10)

    def draw_voltage_ac(self, parent, position: list[int], opts: Opts):
        group = self.createGroup(parent, "AC Voltage")
        elem = self.createGroup(group, "AC Voltage")

        inkDraw.line.relCoords(elem, [[-8, 0]], self.add(position, [-7, 0]))
        inkDraw.line.relCoords(elem, [[8, 0]], self.add(position, [7, 0]))
        inkDraw.circle.centerRadius(elem, position, 7)

        line_style_sin = inkDraw.lineStyle.setSimpleBlack(lineWidth=0.6)
        sin = self.createGroup(group)

        inkDraw.arc.startEndRadius(
            sin,
            self.add(position, [-4, 0]),
            position,
            2,
            [0, 0],
            lineStyle=line_style_sin,
            flagRightOf=True,
            largeArc=False,
        )
        inkDraw.arc.startEndRadius(
            sin,
            self.add(position, [4, 0]),
            position,
            2,
            [0, 0],
            lineStyle=line_style_sin,
            flagRightOf=True,
            largeArc=False,
        )

        if opts.source.draw_opts == "vertical":
            self.rotateElement(elem, position, 90)

        self.draw_label_source(group, position, opts, 10)

    def draw_current1(self, parent, position: list[int], opts: Opts):
        group = self.createGroup(parent, "Current")
        elem = self.createGroup(group, "Current")

        inkDraw.line.relCoords(elem, [[-4, 0]], self.add(position, [-11, 0]))
        inkDraw.line.relCoords(elem, [[4, 0]], self.add(position, [11, 0]))
        inkDraw.circle.centerRadius(elem, [4, 0], 7, offset=position)
        inkDraw.circle.centerRadius(elem, [-4, 0], 7, offset=position)

        line_style_arr = inkDraw.lineStyle.set(
            lineWidth=0.7, fillColor=inkDraw.color.defined("black")
        )
        if opts.source.do_invert:
            inkDraw.line.relCoords(
                elem,
                [[-13, 0], [0, 1.2], [-3, -1.2], [3, -1.2], [0, 1.2]],
                self.add(position, [8, 0]),
                lineStyle=line_style_arr,
            )
        else:
            inkDraw.line.relCoords(
                elem,
                [[13, 0], [0, 1.2], [3, -1.2], [-3, -1.2], [0, 1.2]],
                self.add(position, [-8, 0]),
                lineStyle=line_style_arr,
            )

        if opts.source.draw_opts == "vertical":
            self.rotateElement(elem, position, 90)

        self.draw_label_source(group, position, opts, 10)

    def draw_current2(self, parent, position: list[int], opts: Opts):
        group = self.createGroup(parent, "Current")
        elem = self.createGroup(group, "Current")

        inkDraw.line.relCoords(elem, [[-8, 0]], self.add(position, [-7, 0]))
        inkDraw.line.relCoords(elem, [[8, 0]], self.add(position, [7, 0]))
        inkDraw.circle.centerRadius(elem, position, 7)
        inner_radius = inkDraw.lineStyle.setSimpleBlack(lineWidth=0.6)
        inkDraw.circle.centerRadius(elem, position, 5.5, lineStyle=inner_radius)

        line_style_arr = inkDraw.lineStyle.set(
            lineWidth=0.7,
            lineColor=inkDraw.color.defined("black"),
            fillColor=inkDraw.color.defined("black"),
        )
        if opts.source.do_invert:
            inkDraw.line.relCoords(
                elem,
                [[-5, 0], [0, 1.2], [-3, -1.2], [3, -1.2], [0, 1.2]],
                self.add(position, [4, 0]),
                lineStyle=line_style_arr,
            )
        else:
            inkDraw.line.relCoords(
                elem,
                [[5, 0], [0, 1.2], [3, -1.2], [-3, -1.2], [0, 1.2]],
                self.add(position, [-4, 0]),
                lineStyle=line_style_arr,
            )

        if opts.source.draw_opts == "vertical":
            self.rotateElement(elem, position, 90)

        self.draw_label_source(group, position, opts, 10)
