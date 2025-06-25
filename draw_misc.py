import numpy as np

import inkscapeMadeEasy.inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy.inkscapeMadeEasy_Draw as inkDraw

from opts import Opts


class DrawMisc(inkBase.inkscapeMadeEasy):
    def add(self, vector, delta):
        return vector + np.array(delta)

    def parse_value_misc(self, opts: Opts) -> str:
        value = opts.misc.value
        if opts.misc.do_latex_value and opts.misc.value is not None:
            value = "$" + opts.misc.value + "$"
        return value

    def draw_signal(self, parent, position: list[int], opts: Opts):
        group = self.createGroup(parent, "Signal")
        elem = self.createGroup(group)

        inkDraw.line.relCoords(elem, [[-4, 0]], position)
        inkDraw.circle.centerRadius(elem, self.add(position, [-6, 0]), 2)

        if opts.misc.draw_opts == "left":
            label_pos = self.add(position, [-11, 0])
            designator_pos = self.add(label_pos, [0, -1.5])
            value_pos = self.add(label_pos, [0, 1.5])
            align = ("cr", "br", "tr")
        elif opts.misc.draw_opts == "right":
            label_pos = self.add(position, [11, 0])
            designator_pos = self.add(label_pos, [0, -1.5])
            value_pos = self.add(label_pos, [0, 1.5])
            align = ("cl", "bl", "tl")
            self.rotateElement(elem, position, 180)
        elif opts.misc.draw_opts == "up":
            label_pos = self.add(position, [0, -11])
            designator_pos = self.add(label_pos, [0, -7.5])
            value_pos = label_pos
            align = ("bc", "bc", "bc")
            self.rotateElement(elem, position, -90)
        elif opts.misc.draw_opts == "down":
            label_pos = self.add(position, [0, 11])
            designator_pos = label_pos
            value_pos = self.add(label_pos, [0, 7.5])
            align = ("tc", "tc", "tc")
            self.rotateElement(elem, position, 90)

        if opts.misc.do_value and opts.do_designator:
            inkDraw.text.latex(
                self,
                group,
                opts.designator,
                designator_pos,
                fontSize=5,
                refPoint=align[1],
            )
            inkDraw.text.latex(
                self,
                group,
                opts.misc.value,
                value_pos,
                fontSize=5,
                refPoint=align[2],
            )
        elif opts.do_designator:
            inkDraw.text.latex(
                self,
                group,
                opts.designator,
                label_pos,
                fontSize=5,
                refPoint=align[0],
            )
        elif opts.misc.do_value:
            inkDraw.text.latex(
                self,
                group,
                opts.misc.value,
                label_pos,
                fontSize=5,
                refPoint=align[0],
            )

    def draw_gnd(self, parent, position: list[int], opts: Opts):
        group = self.createGroup(parent, "GND")
        elem = self.createGroup(group)

        inkDraw.line.relCoords(elem, [[0, 6]], position)
        inkDraw.line.relCoords(elem, [[6, 0]], self.add(position, [-3, 6]))

        if opts.misc.draw_opts == "left":
            self.rotateElement(elem, position, -90)
        elif opts.misc.draw_opts == "right":
            self.rotateElement(elem, position, 90)
        elif opts.misc.draw_opts == "up":
            self.rotateElement(elem, position, 180)

    def draw_dot(self, parent, position: list[int]):
        group = self.createGroup(parent, "Dot")
        elem = self.createGroup(group)

        color_black = inkDraw.color.defined("black")
        line_style_fill = inkDraw.lineStyle.set(fillColor=color_black)

        inkDraw.circle.centerRadius(elem, position, 1, lineStyle=line_style_fill)
