import tkinter as tk


def center_window(window, within=None):
    """ Center the window within another window (tk obj) or the screen (None)"""
    window.withdraw()
    window.update_idletasks()
    window.geometry("+0+0")
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    if within is None:
        x = (window.winfo_screenwidth() - width) // 2
        y = (window.winfo_screenheight() - height) // 2
    else:
        if isinstance(within, tk.Tk):
            pass
        elif isinstance(within, tk.Toplevel):
            pass
        else:
            within = within.winfo_toplevel()
        data = formal_geometry(within)
        x = ((data[0] // 2) + data[2]) - (width//2)
        y = ((data[1] // 2) + data[3]) - (height//2)
    if (window.winfo_screenwidth() - x) < width:
        x = window.winfo_screenwidth() - width
    if (window.winfo_screenheight() - y) < height:
        y = window.winfo_screenheight() - height
    window.geometry("+{}+{}".format(x, y))
    window.deiconify()


def align_window(window, under=None):
    window.withdraw()
    window.update_idletasks()
    width = window.winfo_reqwidth()
    height = window.winfo_reqheight()
    under_x = under.winfo_rootx()
    under_y = under.winfo_rooty()
    x = under_x
    y = under_y + under.winfo_height()
    x = abs(x)
    y = abs(y)
    if window.winfo_screenwidth() - x < width:
        x = window.winfo_screenwidth() - width
    if window.winfo_screenheight() - y < height:
        y = under_y - window.winfo_reqheight()
    # align
    window.geometry("+{}+{}".format(x, y))
    window.deiconify()


def dialog_effect(window):
    window.transient(window.master)
    window.lift()
    window.grab_set()
    window.focus_set()


def formal_geometry(window):
    width = window.winfo_width()
    height = window.winfo_height()
    coord_x = window.winfo_x()
    coord_y = window.winfo_y()
    return width, height, coord_x, coord_y


def center_dialog_effect(window, within=None):
    center_window(window, within=within)
    dialog_effect(window)


def merge_megaconfig(primary=None, secondary=None):
    primary = primary if primary else dict()
    secondary = secondary if secondary else dict()
    megaconfig = dict()
    # parse secondary megaconfig
    for part, config in secondary.items():
        megaconfig[part] = config
    # parse primary megaconfig
    for part, config in primary.items():
        if config is not None:
            megaconfig[part] = config
    return megaconfig


class Error(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else ""
        super().__init__(self.message)

    def __str__(self):
        return self.message
