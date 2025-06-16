import numpy as np

import inkscapeMadeEasy.inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy.inkscapeMadeEasy_Draw as inkDraw

from opts import Opts


class DrawTran(inkBase.inkscapeMadeEasy):
    def add(self, vector, delta):
        return vector + np.array(delta)

    def draw_label_tran(
        self,
        group,
        position: list[int],
        opts: Opts,
        label_offsets: tuple[float, float],
    ):
        if opts.tran.do_envelope:
            label_offset = label_offsets[1]
        else:
            label_offset = label_offsets[0]

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

        self.draw_label_tran(group, position, opts, (25, 32))

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

        self.draw_label_tran(group, position, opts, (25, 32))

    def draw_mosfet(self, parent, position: list[int], opts: Opts):
        group = self.createGroup(parent, "MOSFET")
        elem = self.createGroup(group, "MOSFET")
        color_black = inkDraw.color.defined("black")

        len_arr = 2.0

        mos_arr_a = inkDraw.marker.createMarker(
            self,
            "MOSArrowA",
            "M -0.1,0 l -%f,%f l 0,-%f z"
            % (len_arr * 1.2, len_arr / 2.0, len_arr),
            RenameMode=0,
            strokeColor=color_black,
            fillColor=color_black,
            lineWidth=0.6,
        )
        line_style_arr = inkDraw.lineStyle.set(
            lineWidth=1.0, lineColor=color_black, markerEnd=mos_arr_a
        )
        mos_arr_b = inkDraw.marker.createMarker(
            self,
            "MOSArrowB",
            "M -0.3,0 l -%f,%f l 0,-%f z"
            % (len_arr * 1.2, len_arr / 2.0, len_arr),
            RenameMode=0,
            strokeColor=color_black,
            fillColor=color_black,
            lineWidth=0.6,
        )
        line_style_arr_s = inkDraw.lineStyle.set(
            lineWidth=1, lineColor=color_black, markerEnd=mos_arr_b
        )

        # gate
        inkDraw.line.relCoords(elem, [[0, 11]], self.add(position, [17, -6]))
        inkDraw.line.relCoords(
            elem, [[-17.75, 0]], self.add(position, [16.75, 5])
        )

        # drain
        inkDraw.line.relCoords(
            elem, [[0, -9.6]], self.add(position, [24, -5.4])
        )
        inkDraw.line.relCoords(elem, [[5, 0]], self.add(position, [19, -5.25]))

        # source
        inkDraw.line.relCoords(elem, [[0, 9.6]], self.add(position, [24, 5.4]))
        inkDraw.line.relCoords(elem, [[5, 0]], self.add(position, [19, 5.25]))

        # bulk
        if opts.tran.fet.symbol == "4_term":
            inkDraw.line.relCoords(elem, [[15, 0]], self.add(position, [24, 0]))
        if opts.tran.fet.symbol == "3_term":
            inkDraw.line.relCoords(
                elem, [[0, -5.25]], self.add(position, [24, 5.25])
            )
            inkDraw.circle.centerRadius(
                elem,
                self.add(position, [24, 5.25]),
                radius=0.4,
                offset=[0, 0],
                label="circle",
            )

        # bulk arrow
        if opts.tran.fet.symbol == "4_term":
            if opts.tran.fet.channel == "negative":
                inkDraw.line.relCoords(
                    elem,
                    [[-4.75, 0]],
                    self.add(position, [24, 0]),
                    lineStyle=line_style_arr,
                )
            elif opts.tran.fet.channel == "positive":
                inkDraw.line.relCoords(
                    elem,
                    [[5, 0]],
                    self.add(position, [19.25, 0]),
                    lineStyle=line_style_arr,
                )

        if opts.tran.fet.symbol == "3_term":
            if opts.tran.fet.channel == "negative":
                inkDraw.line.relCoords(
                    elem,
                    [[-5, 0]],
                    self.add(position, [24, 0]),
                    lineStyle=line_style_arr_s,
                )
            elif opts.tran.fet.channel == "positive":
                inkDraw.line.relCoords(
                    elem,
                    [[5, 0]],
                    self.add(position, [19, 0]),
                    lineStyle=line_style_arr_s,
                )

        # switch source and drain terminals
        if opts.tran.fet.switch:
            self.scaleElement(elem, scaleX=1.0, scaleY=-1.0, center=position)

        # channel line
        if opts.tran.fet.type == "mos_e":
            inkDraw.line.relCoords(
                elem, [[0, 3.5]], self.add(position, [19, -7])
            )
            inkDraw.line.relCoords(
                elem, [[0, 3.5]], self.add(position, [19, -1.75])
            )
            inkDraw.line.relCoords(
                elem, [[0, 3.5]], self.add(position, [19, 3.5])
            )
        elif opts.tran.fet.type == "mos_d":
            inkDraw.line.relCoords(
                elem, [[0, 14]], self.add(position, [19, -7])
            )

        # envelope
        if opts.tran.do_envelope:
            inkDraw.circle.centerRadius(
                elem,
                centerPoint=self.add(position, [20, 0]),
                radius=10,
                offset=[0, 0],
                label="envelope",
            )

        if opts.tran.orientation == "horizontal":
            self.rotateElement(elem, position, 90)

        self.draw_label_tran(group, position, opts, (27, 32))

    def draw_jfet(self, parent, position: list[int], opts: Opts):
        if opts.tran.fet.switch:
            y_switch = -1
        else:
            y_switch = 1

        group = self.createGroup(parent, "JFET")
        elem = self.createGroup(group, "JFET")
        color_black = inkDraw.color.defined("black")

        len_arr = 2.0
        gate_arr = inkDraw.marker.createMarker(
            self,
            "GateArrow",
            "M -0.3,0 l -%f,%f l 0,-%f z"
            % (len_arr * 1.2, len_arr / 2.0, len_arr),
            RenameMode=0,
            strokeColor=color_black,
            fillColor=color_black,
            lineWidth=0.6,
        )
        line_style_arr = inkDraw.lineStyle.set(
            lineWidth=1.0, lineColor=color_black, markerEnd=gate_arr
        )

        # source and drain terminals
        inkDraw.line.relCoords(
            elem, [[6, 0], [0, 10]], self.add(position, [17, 5])
        )
        inkDraw.line.relCoords(
            elem, [[6, 0], [0, -10]], self.add(position, [17, -5])
        )

        # junction line
        inkDraw.line.relCoords(
            elem,
            [[0, 14]],
            self.add(position, [17, -7]),
            lineStyle=inkDraw.lineStyle.setSimpleBlack(lineWidth=2),
        )

        gate_y = y_switch * 5
        theta = np.asin(gate_y / 10)
        p1 = [10 + 10 * (1 - np.cos(theta)), gate_y]
        p2 = [10 + 10 - 3, gate_y]

        # gate terminal
        inkDraw.line.absCoords(elem, [[-2, gate_y], p1], position)

        # gate arrow
        if opts.tran.fet.channel == "negative":
            inkDraw.line.absCoords(
                elem, [p1, p2], position, lineStyle=line_style_arr
            )
        elif opts.tran.fet.channel == "positive":
            inkDraw.line.absCoords(
                elem, [p2, p1], position, lineStyle=line_style_arr
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

        self.draw_label_tran(group, position, opts, (27, 32))

    def draw_cmos(self, parent, position: list[int], opts: Opts):
        group = self.createGroup(parent, "Shorthand MOSFET")
        elem = self.createGroup(group, "Shorthand MOSFET")
        color_black = inkDraw.color.defined("black")

        line_style_bold = inkDraw.lineStyle.set(
            lineWidth=2, lineColor=color_black
        )
        # gate
        if opts.tran.fet.type == "cmos_d":
            inkDraw.line.relCoords(
                elem, [[0, 12]], self.add(position, [16, -6])
            )
            if opts.tran.fet.channel == "negative":
                inkDraw.line.relCoords(
                    elem, [[-16.75, 0]], self.add(position, [15.75, 0])
                )
            elif opts.tran.fet.channel == "positive":
                inkDraw.line.relCoords(
                    elem, [[-14.75, 0]], self.add(position, [13.75, 0])
                )
                inkDraw.circle.centerRadius(
                    elem,
                    self.add(position, [15, 0]),
                    radius=1.0,
                    offset=[0, 0],
                    label="not",
                )
        elif opts.tran.fet.type == "cmos_e":
            inkDraw.line.relCoords(
                elem, [[0, 12]], self.add(position, [17, -6])
            )
            if opts.tran.fet.channel == "negative":
                inkDraw.line.relCoords(
                    elem, [[-17.75, 0]], self.add(position, [16.75, 0])
                )
            elif opts.tran.fet.channel == "positive":
                inkDraw.line.relCoords(
                    elem, [[-15.75, 0]], self.add(position, [14.75, 0])
                )
                inkDraw.circle.centerRadius(
                    elem,
                    self.add(position, [16, 0]),
                    radius=1.0,
                    offset=[0, 0],
                    label="not",
                )

        # drain
        inkDraw.line.relCoords(
            elem, [[0, -9.6]], self.add(position, [24, -5.4])
        )
        inkDraw.line.relCoords(elem, [[5, 0]], self.add(position, [19, -5.25]))

        # source
        inkDraw.line.relCoords(elem, [[0, 9.6]], self.add(position, [24, 5.4]))
        inkDraw.line.relCoords(elem, [[5, 0]], self.add(position, [19, 5.25]))

        # channel line
        if opts.tran.fet.type == "cmos_e":
            inkDraw.line.relCoords(
                elem, [[0, 14]], self.add(position, [19, -7])
            )
        elif opts.tran.fet.type == "cmos_d":
            inkDraw.line.relCoords(
                elem,
                [[0, 14]],
                self.add(position, [18.65, -7]),
                lineStyle=line_style_bold,
            )

        # envelope
        if opts.tran.do_envelope:
            inkDraw.circle.centerRadius(
                elem,
                centerPoint=self.add(position, [20, 0]),
                radius=10,
                offset=[0, 0],
                label="envelope",
            )

        if opts.tran.orientation == "horizontal":
            self.rotateElement(elem, position, 90)

        self.draw_label_tran(group, position, opts, (27, 32))
