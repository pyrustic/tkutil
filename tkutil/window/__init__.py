import os
import os.path
import tkinter as tk
from shared import JsonDoc
from tkutil import error


def make_modal(window):
    """turn into a modal window ! dialog effect !"""
    window.transient(window.master)
    window.lift()
    window.grab_set()
    window.focus_set()


def center(window, parent=None, correction=(0, 0)):
    """
    Returns the coords tuple: (x, y)
    """
    hide_early(window)
    x, y = compute_center(window, parent)
    coords = relocate(window, x, y, correction)
    return coords


def align(window, parent=None, side="n", correction=(0, 0)):
    if side not in ("n", "s", "w", "e", "nw", "sw", "ne", "se"):
        msg = "The Side argument should be one of: n, s, w, e "
        raise error.Error(msg)
    hide_early(window)
    if parent is None:
        x, y = compute_alignment(window, parent, side)
    else:
        if isinstance(parent, tk.Tk):
            pass
        elif isinstance(parent, tk.Toplevel):
            pass
        else:
            parent = parent.winfo_toplevel()
        x, y = compute_alignment(window, parent, side)
    coords = relocate(window, x, y, correction)
    return coords


def compute_center(window, parent=None):
    """Compute the x, y coords to set the window in the center of parent.
    If parent is None, the screen will be considered as parent"""
    width = window.winfo_width()
    height = window.winfo_height()
    if parent is None:
        x = (window.winfo_screenwidth() - width) // 2
        y = (window.winfo_screenheight() - height) // 2
    else:
        if isinstance(parent, tk.Tk):
            pass
        elif isinstance(parent, tk.Toplevel):
            pass
        else:
            parent = parent.winfo_toplevel()
        data = get_geometry(parent)
        x = ((data[0] // 2) + data[2]) - (width//2)
        y = ((data[1] // 2) + data[3]) - (height//2)
    return x, y


def compute_alignment(window, parent=None, side="n"):
    """Compute the x, y coords to perform an alignment.
    Legal sides are: n, s, w, e, nw, sw, ne, se.
    If you don't submit a parent, the screen will be considered as parent"""
    if parent:
        x, y = _compute_alignment_within_parent(window, parent, side)
    else:
        x, y =_compute_alignment_within_screen(window, side)
    return x, y


def hide_early(window):
    """Hide a window before a relocation"""
    window.withdraw()
    window.update_idletasks()
    window.geometry("+0+0")
    window.update_idletasks()


def relocate(window, x, y, correction=(0, 0)):
    width = window.winfo_width()
    height = window.winfo_height()
    if (window.winfo_screenwidth() - x) < width:
        x = window.winfo_screenwidth() - width
    if (window.winfo_screenheight() - y) < height:
        y = window.winfo_screenheight() - height
    cx, cy = correction
    x = x + cx
    y = y + cy
    spec = "+{}+{}".format(x, y)
    window.geometry(spec)
    window.deiconify()
    return x, y


def get_geometry(window):
    """
    Return a tuple: width, height, coord_x, coord_y
    """
    width = window.winfo_width()
    height = window.winfo_height()
    coord_x = window.winfo_x()
    coord_y = window.winfo_y()
    return width, height, coord_x, coord_y


def save_size(window, name=None):
    spec = (window.winfo_width(), window.winfo_height())
    if spec[0] <= 1 or spec[1] <= 1:
        return
    name = name if name else window.winfo_name()
    directory = os.path.join(os.path.expanduser("~"),
                             "PyrusticHome", "tkutil")
    jdoc = JsonDoc("{}_window.json".format(name), directory=directory)
    data = jdoc.read()
    data["size"] = spec
    jdoc.write(data)


def save_coords(window, name=None):
    name = name if name else window.winfo_name()
    spec = (window.winfo_x(), window.winfo_y())
    directory = os.path.join(os.path.expanduser("~"),
                             "PyrusticHome", "tkutil")
    jdoc = JsonDoc("{}_window.json".format(name), directory=directory)
    data = jdoc.read()
    data["coords"] = spec
    jdoc.write(data)


def save_geometry(window, name=None):
    width, height, x, y = get_geometry(window)
    geometry = "{}x{}+{}+{}".format(width, height, x, y)
    if geometry.startswith("0") or geometry.startswith("1x1"):
        return
    name = name if name else window.winfo_name()
    directory = os.path.join(os.path.expanduser("~"),
                             "PyrusticHome", "tkutil")
    jdoc = JsonDoc("{}_window.json".format(name), directory=directory)
    data = jdoc.read()
    data["geometry"] = geometry
    jdoc.write(data)


def restore_size(window, name=None, default=None):
    name = name if name else window.winfo_name()
    directory = os.path.join(os.path.expanduser("~"),
                             "PyrusticHome", "tkutil")
    jdoc = JsonDoc("{}_window.json".format(name), directory=directory)
    data = jdoc.read()
    size = data.get("size")
    spec = ""
    if size:
        spec = "{}x{}".format(size[0], size[1])
    elif default:
        spec = "{}x{}".format(default[0], default[1])
    window.geometry(spec)


def restore_coords(window, name=None, default=None):
    name = name if name else window.winfo_name()
    directory = os.path.join(os.path.expanduser("~"),
                             "PyrusticHome", "tkutil")
    jdoc = JsonDoc("{}_window.json".format(name), directory=directory)
    data = jdoc.read()
    coords = data.get("coords")
    spec = ""
    if coords:
        spec = "+{}+{}".format(coords[0], coords[1])
    elif default:
        spec = "+{}+{}".format(default[0], default[1])
    window.geometry(spec)


def restore_geometry(window, name=None, default=None):
    name = name if name else window.winfo_name()
    directory = os.path.join(os.path.expanduser("~"),
                             "PyrusticHome", "tkutil")
    jdoc = JsonDoc("{}_window.json".format(name), directory=directory)
    data = jdoc.read()
    geometry = data.get("geometry", "")
    if not geometry and default:
        geometry = default
    window.geometry(geometry)


class WinfoUpdater:
    def __init__(self, widget, delay=256):
        self._root = widget.nametowidget(".")
        self._delay = delay
        self._todo_id = None
        self._bind_id = None
        self._activated = False
               
    @property
    def root(self):
        return self._root
        
    def activate(self):
        if self._activated:
            return False
        self._clear_todo()
        self._bind_on_change()
        return True
        
    def deactivate(self):
        if not self._activated:
            return False
        self._activated = False
        self._unbind_on_change()
        self._clear_todo()
        self._bind_id = None
        return True
        
    def _bind_on_change(self):
        self._unbind_on_change()
        self._bind_id = self._root.bind("<Configure>", self._on_change, True)
        
    def _unbind_on_change(self):
        if not self._bind_id:
            return
        self._root.unbind("<Configure>", self._bind_id)
        self._bind_id = None
    
    def _on_change(self, event):
        if event.widget is not self._root:
            return
        self._clear_todo()
        self._todo_id = self._root.after(self._delay, self._update_winfo)

    def _update_winfo(self):
        self.deactivate()
        self._root.tkraise()
        self._root.update()
        self._root.after(10, self.activate)

    def _clear_todo(self):
        if not self._todo_id:
            return
        self._root.after_cancel(self._todo_id)
        self._todo_id = None
       


def _compute_alignment_within_screen(window, side="n"):
    width, height = window.winfo_width(), window.winfo_height()
    parent_width = window.winfo_screenwidth()
    parent_height = window.winfo_screenheight()
    if side == "n":
        x = (parent_width - width) // 2
        y = 0
    elif side == "s":
        x = (parent_width - width) // 2
        y = parent_height - height
    elif side == "w":
        x = 0
        y = (parent_height - height) // 2
    elif side == "e":
        x = parent_width - width
        y = (parent_height - height) // 2
    elif side == "nw":
        x = 0
        y = 0
    elif side == "sw":
        x = 0
        y = parent_height - height
    elif side == "ne":
        x = parent_width - width
        y = 0
    elif side == "se":
        x = parent_width - width
        y = parent_height - height
    else:
        msg = "The Side argument should be one of: n, s, w, e, nw, sw, ne, se"
        raise error.Error(msg)
    return x, y


def _compute_alignment_within_parent(window, parent, side="n"):
    width, height = window.winfo_width(), window.winfo_height()
    parent_width, parent_height, parent_x, parent_y = get_geometry(parent)
    if side == "n":
        x = ((parent_width - width) // 2) + parent_x
        y = parent_y
    elif side == "s":
        x = ((parent_width - width) // 2) + parent_x
        y = parent_y + parent_height - height
    elif side == "w":
        x = parent_x
        y = ((parent_height - height) // 2) + parent_y
    elif side == "e":
        x = parent_x + parent_width - width
        y = ((parent_height - height) // 2) + parent_y
    elif side == "nw":
        x = parent_x
        y = parent_y
    elif side == "sw":
        x = parent_x
        y = parent_y + parent_height - height
    elif side == "ne":
        x = parent_x + parent_width - width
        y = parent_y
    elif side == "se":
        x = parent_x + parent_width - width
        y = parent_y + parent_height - height
    else:
        msg = "The Side argument should be one of: n, s, w, e, nw, sw, ne, se"
        raise error.Error(msg)
    return x, y
