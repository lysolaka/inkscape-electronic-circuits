from argparse import Namespace


class Opts:
    def __init__(self, opts: Namespace) -> None:
        self.action = opts.action
        self.do_designator = opts.do_designator
        self.designator = opts.designator
        self.do_latex_math = opts.do_latex_math
        if self.action == "rlc":
            self.rlc = RLCOpts(opts)
        elif self.action == "tran":
            self.tran = TranOpts(opts)
        elif self.action == "diode":
            self.diode = DOpts(opts)
        elif self.action == "source":
            self.source = SourceOpts(opts)


class RLCOpts:
    def __init__(self, opts: Namespace) -> None:
        self.type = opts.rlc_type
        self.do_variable = opts.rlc_do_variable
        self.draw_opts = opts.rlc_draw_opts
        self.do_value = opts.rlc_do_value
        self.value = opts.rlc_value
        self.do_unit = opts.rlc_do_unit
        self.do_latex_value = opts.rlc_do_latex_value


class TranOpts:
    def __init__(self, opts: Namespace) -> None:
        self.type = opts.tran_type
        if self.type == "bjt":
            self.bjt = BJTOpts(opts)
        elif self.type == "fet":
            self.fet = FETOpts(opts)
        self.orientation = opts.tran_orientation
        self.do_envelope = opts.tran_do_envelope
        self.do_extra = opts.tran_do_extra
        self.extra = opts.tran_extra


class BJTOpts:
    def __init__(self, opts: Namespace) -> None:
        self.type = opts.bjt_type
        self.igbt = opts.bjt_igbt
        self.photo = opts.bjt_photo
        self.switch = opts.bjt_switch


class FETOpts:
    def __init__(self, opts: Namespace) -> None:
        self.type = opts.fet_type
        self.symbol = opts.fet_symbol
        self.channel = opts.fet_channel
        self.switch = opts.fet_switch


class DOpts:
    def __init__(self, opts: Namespace) -> None:
        self.type = opts.diode_type
        self.draw_opts = opts.diode_draw_opts
        self.do_extra = opts.diode_do_extra
        self.extra = opts.diode_extra
        self.fill = "#" + format(int(opts.diode_fill), "08x")


class SourceOpts:
    def __init__(self, opts: Namespace) -> None:
        self.type = opts.source_type
        self.do_invert = opts.source_do_invert
        self.draw_opts = opts.source_draw_opts
        self.do_value = opts.source_do_value
        self.value = opts.source_value
        self.do_unit = opts.source_do_unit
        self.do_latex_value = opts.source_do_latex_value
