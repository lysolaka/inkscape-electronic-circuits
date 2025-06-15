import numpy as np

import inkscapeMadeEasy.inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy.inkscapeMadeEasy_Draw as inkDraw

from opts import Opts


class DrawTran(inkBase.inkscapeMadeEasy):
    def add(self, vector, delta):
        return vector + np.array(delta)

    def draw_label_tran(self, group, position: list[int], opts: Opts):
        if opts.tran.do_envelope:
            label_offset = 32
        else:
            label_offset = 25

        if opts.tran.orientation == "horizontal":
            label_pos_top = [0, -label_offset - 7.5]
            label_pos_bot = [0, -label_offset]
            label_pos = [0, -label_offset]
            ref_points = ["bc", "bc", "bc"]
        elif opts.tran.orientation == "vertical":
            label_pos_top = [label_offset, -1.5]
            label_pos_bot = [label_offset, 1.5]
            label_pos = [label_offset, 0]
            ref_points = ["bl", "tl", "cl"]

        if opts.tran.do_extra and opts.do_designator:
            inkDraw.text.latex(
                self,
                group,
                opts.designator,
                self.add(position, label_pos_top),
                fontSize=5,
                refPoint=ref_points[0],
            )
            inkDraw.text.latex(
                self,
                group,
                opts.tran.extra,
                self.add(position, label_pos_bot),
                fontSize=5,
                refPoint=ref_points[1],
            )
        elif opts.do_designator:
            inkDraw.text.latex(
                self,
                group,
                opts.designator,
                self.add(position, label_pos),
                fontSize=5,
                refPoint=ref_points[2],
            )
        elif opts.tran.do_extra:
            inkDraw.text.latex(
                self,
                group,
                opts.tran.extra,
                self.add(position, label_pos),
                fontSize=5,
                refPoint=ref_points[2],
            )
        pass

    def draw_bjt(self, parent, position: list[int], opts: Opts):
        if opts.tran.bjt.switch:
            y_switch = -1
        else:
            y_switch = 1

        group = self.createGroup(parent, "BJT")
        elem = self.createGroup(group, "BJT")
        color_black = inkDraw.color.defined("black")

        # base
        if not opts.tran.bjt.photo:
            inkDraw.line.relCoords(elem, [[15, 0]], position)
        else:
            arrow = self.createGroup(elem)
            inkDraw.line.relCoords(arrow, [[7, 0]], position)
            inkDraw.line.relCoords(
                arrow,
                [[1.5, -1.5], [-1.5, -1.5]],
                self.add(position, [5.5, 1.5]),
            )
            self.rotateElement(arrow, position, -30)
            self.moveElement(arrow, [1, -7])
            self.copyElement(arrow, elem, distance=[0, 7])

        # junction line
        style = inkDraw.lineStyle.setSimpleBlack(lineWidth=2)
        inkDraw.line.relCoords(
            elem, [[0, 12]], self.add(position, [14.5, -6]), lineStyle=style
        )

        # emitter arrow marker
        len_arr = 2.5
        bjt_marker = inkDraw.marker.createMarker(
            self,
            "BJTArrow",
            "M 0,0 l -%f,%f l 0,-%f z"
            % (len_arr * 1.2, len_arr / 2.0, len_arr),
            RenameMode=0,
            strokeColor=color_black,
            fillColor=color_black,
            lineWidth=0.6,
        )
        line_style_arrow = inkDraw.lineStyle.set(
            lineWidth=1, lineColor=color_black, markerEnd=bjt_marker
        )

        # draw emitter and collector terminals
        # collector
        inkDraw.line.relCoords(
            elem,
            [[7, -y_switch * 5], [0, -y_switch * 7]],
            self.add(position, [15, -y_switch * 3]),
        )
        # emitter
        if opts.tran.bjt.type == "npn":
            inkDraw.line.relCoords(
                elem,
                [[7, y_switch * 5]],
                self.add(position, [15, y_switch * 3]),
                lineStyle=line_style_arrow,
            )
            inkDraw.line.relCoords(
                elem,
                [[0, y_switch * 7]],
                self.add(position, [22, y_switch * 8]),
            )
        else:
            inkDraw.line.relCoords(
                elem,
                [[-7, -y_switch * 5]],
                self.add(position, [22, y_switch * 8]),
                lineStyle=line_style_arrow,
            )
            inkDraw.line.relCoords(
                elem,
                [[0, y_switch * 7]],
                self.add(position, [22, y_switch * 8]),
            )

        if opts.tran.do_envelope:
            inkDraw.circle.centerRadius(
                elem,
                centerPoint=self.add(position, [19, 0]),
                radius=10,
                offset=[0, 0],
                label="envelope",
            )

        if opts.tran.orientation == "horizontal":
            self.rotateElement(elem, position, 90)

        self.draw_label_tran(group, position, opts)

    def draw_igbt(self, parent, position: list[int], opts: Opts):
        if opts.tran.bjt.switch:
            y_switch = -1
        else:
            y_switch = 1

        group = self.createGroup(parent, "BJT")
        elem = self.createGroup(group, "BJT")
        color_black = inkDraw.color.defined("black")

        # base
        inkDraw.line.relCoords(elem, [[13, 0]], position)

        # junction line
        inkDraw.line.relCoords(elem, [[0, 12]], self.add(position, [15, -6]))
        inkDraw.line.relCoords(elem, [[0, 10]], self.add(position, [13, -5]))

        # emitter arrow marker
        len_arr = 2.5
        bjt_marker = inkDraw.marker.createMarker(
            self,
            "BJTArrow",
            "M 0,0 l -%f,%f l 0,-%f z"
            % (len_arr * 1.2, len_arr / 2.0, len_arr),
            RenameMode=0,
            strokeColor=color_black,
            fillColor=color_black,
            lineWidth=0.6,
        )
        line_style_arrow = inkDraw.lineStyle.set(
            lineWidth=1, lineColor=color_black, markerEnd=bjt_marker
        )

        # draw emitter and collector terminals
        # collector
        inkDraw.line.relCoords(
            elem,
            [[7, -y_switch * 5], [0, -y_switch * 7]],
            self.add(position, [15, -y_switch * 3]),
        )
        # emitter
        if opts.tran.bjt.type == "npn":
            inkDraw.line.relCoords(
                elem,
                [[7, y_switch * 5]],
                self.add(position, [15, y_switch * 3]),
                lineStyle=line_style_arrow,
            )
            inkDraw.line.relCoords(
                elem,
                [[0, y_switch * 7]],
                self.add(position, [22, y_switch * 8]),
            )
        else:
            inkDraw.line.relCoords(
                elem,
                [[-7, -y_switch * 5]],
                self.add(position, [22, y_switch * 8]),
                lineStyle=line_style_arrow,
            )
            inkDraw.line.relCoords(
                elem,
                [[0, y_switch * 7]],
                self.add(position, [22, y_switch * 8]),
            )

        if opts.tran.do_envelope:
            inkDraw.circle.centerRadius(
                elem,
                centerPoint=self.add(position, [19, 0]),
                radius=10,
                offset=[0, 0],
                label="envelope",
            )

        if opts.tran.orientation == "horizontal":
            self.rotateElement(elem, position, 90)

        self.draw_label_tran(group, position, opts)
