import numpy as np

import inkscapeMadeEasy.inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy.inkscapeMadeEasy_Draw as inkDraw

from opts import Opts


class DrawDiode(inkBase.inkscapeMadeEasy):
    def add(self, vector, delta):
        return vector + np.array(delta)

    def draw_label_diode(
        self,
        group,
        position: list[int],
        opts: Opts,
    ):
        if opts.diode.type in ["led", "photo"]:
            upper_pos = self.add(position, [0, -16])
        else:
            upper_pos = self.add(position, [0, -9])
        lower_pos = self.add(position, [0, 9])

        side_pos = self.add(position, [9, 0])
        upper_side_pos = self.add(position, [9, -1.5])
        lower_side_pos = self.add(position, [9, 1.5])

        if opts.diode.do_extra and opts.do_designator:
            if opts.diode.draw_opts in ["up", "down"]:
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
                    opts.diode.extra,
                    lower_side_pos,
                    fontSize=5,
                    refPoint="tl",
                )
            elif opts.diode.draw_opts in ["left", "right"]:
                inkDraw.text.latex(
                    self,
                    group,
                    opts.designator,
                    upper_pos,
                    fontSize=5,
                    refPoint="bc",
                )
                inkDraw.text.latex(
                    self, group, opts.diode.extra, lower_pos, fontSize=5, refPoint="tc"
                )
        elif opts.diode.do_extra:
            if opts.diode.draw_opts in ["up", "down"]:
                inkDraw.text.latex(
                    self, group, opts.diode.extra, side_pos, fontSize=5, refPoint="cl"
                )
            elif opts.diode.draw_opts in ["left", "right"]:
                inkDraw.text.latex(
                    self, group, opts.diode.extra, upper_pos, fontSize=5, refPoint="bc"
                )
        elif opts.do_designator:
            if opts.diode.draw_opts in ["up", "down"]:
                inkDraw.text.latex(
                    self, group, opts.designator, side_pos, fontSize=5, refPoint="cl"
                )
            elif opts.diode.draw_opts in ["left", "right"]:
                inkDraw.text.latex(
                    self,
                    group,
                    opts.designator,
                    upper_pos,
                    fontSize=5,
                    refPoint="bc",
                )

    def draw_diode(self, parent, position: list[int], opts: Opts):
        group = self.createGroup(parent, "Diode")
        elem = self.createGroup(group)

        line_style_body = inkDraw.lineStyle.set(fillColor=opts.diode.fill)

        inkDraw.line.relCoords(elem, [[9, 0]], self.add(position, [6, 0]))

        inkDraw.line.relCoords(elem, [[-9, 0]], self.add(position, [-6, 0]))
        inkDraw.line.relCoords(
            elem,
            [[-12, 6], [0, -12], [12, 6]],
            self.add(position, [6, 0]),
            lineStyle=line_style_body,
            closePath=True,
        )

        if opts.diode.type in ["regular", "led", "photo"]:
            inkDraw.line.relCoords(elem, [[0, 12]], self.add(position, [6, -6]))
        elif opts.diode.type == "schottky":
            inkDraw.line.relCoords(
                elem,
                [[0, 2], [3, 0], [0, -12], [3, 0], [0, 2]],
                self.add(position, [6 - 3, 6 - 2]),
            )
        elif opts.diode.type == "zener":
            inkDraw.line.relCoords(
                elem, [[0, -12], [-3, 0]], self.add(position, [6, 6])
            )

        if opts.diode.type == "led":
            arrow = self.createGroup(elem)
            inkDraw.line.relCoords(arrow, [[7, 0]], position)
            inkDraw.line.relCoords(arrow, [[1.5, -1.5], [-1.5, -1.5]], self.add(position, [5.5, 1.5]))
            self.rotateElement(arrow, position, 60)
            self.moveElement(arrow, [-3, -8])
            self.copyElement(arrow, elem, distance=[5, 2])

        if opts.diode.type == "photo":
            arrow = self.createGroup(elem)
            inkDraw.line.relCoords(arrow, [[7, 0]], position)
            inkDraw.line.relCoords(arrow, [[1.5, -1.5], [-1.5, -1.5]], self.add(position, [5.5, 1.5]))
            self.rotateElement(arrow, position, -120)
            self.moveElement(arrow, [0, -14])
            self.copyElement(arrow, elem, distance=[5, 2])

        if opts.diode.draw_opts == "left":
            if opts.diode.type in ["led", "photo"]:
                self.scaleElement(elem, -1, 1, position)
            else:
                self.rotateElement(elem, position, 180)
        elif opts.diode.draw_opts == "up":
            self.rotateElement(elem, position, 90)
        elif opts.diode.draw_opts == "down":
            if opts.diode.type in ["led", "photo"]:
                self.rotateElement(elem, position, 90)
                self.scaleElement(elem, 1, -1, position)
            else:
                self.rotateElement(elem, position, -90)

        self.draw_label_diode(group, position, opts)
