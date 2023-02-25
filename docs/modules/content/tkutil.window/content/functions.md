Back to [All Modules](https://github.com/pyrustic/tkutil/blob/master/docs/modules/README.md#readme)

# Module Overview

**tkutil.window**
 
No description

> **Classes:** &nbsp; [WinfoUpdater](https://github.com/pyrustic/tkutil/blob/master/docs/modules/content/tkutil.window/content/classes/WinfoUpdater.md#class-winfoupdater)
>
> **Functions:** &nbsp; [\_compute\_alignment\_within\_parent](#_compute_alignment_within_parent) &nbsp;&nbsp; [\_compute\_alignment\_within\_screen](#_compute_alignment_within_screen) &nbsp;&nbsp; [align](#align) &nbsp;&nbsp; [center](#center) &nbsp;&nbsp; [compute\_alignment](#compute_alignment) &nbsp;&nbsp; [compute\_center](#compute_center) &nbsp;&nbsp; [get\_geometry](#get_geometry) &nbsp;&nbsp; [hide\_early](#hide_early) &nbsp;&nbsp; [make\_modal](#make_modal) &nbsp;&nbsp; [relocate](#relocate) &nbsp;&nbsp; [restore\_coords](#restore_coords) &nbsp;&nbsp; [restore\_geometry](#restore_geometry) &nbsp;&nbsp; [restore\_size](#restore_size) &nbsp;&nbsp; [save\_coords](#save_coords) &nbsp;&nbsp; [save\_geometry](#save_geometry) &nbsp;&nbsp; [save\_size](#save_size)
>
> **Constants:** &nbsp; None

# All Functions
[\_compute\_alignment\_within\_parent](#_compute_alignment_within_parent) &nbsp;&nbsp; [\_compute\_alignment\_within\_screen](#_compute_alignment_within_screen) &nbsp;&nbsp; [align](#align) &nbsp;&nbsp; [center](#center) &nbsp;&nbsp; [compute\_alignment](#compute_alignment) &nbsp;&nbsp; [compute\_center](#compute_center) &nbsp;&nbsp; [get\_geometry](#get_geometry) &nbsp;&nbsp; [hide\_early](#hide_early) &nbsp;&nbsp; [make\_modal](#make_modal) &nbsp;&nbsp; [relocate](#relocate) &nbsp;&nbsp; [restore\_coords](#restore_coords) &nbsp;&nbsp; [restore\_geometry](#restore_geometry) &nbsp;&nbsp; [restore\_size](#restore_size) &nbsp;&nbsp; [save\_coords](#save_coords) &nbsp;&nbsp; [save\_geometry](#save_geometry) &nbsp;&nbsp; [save\_size](#save_size)

## \_compute\_alignment\_within\_parent
No description



**Signature:** (window, parent, side='n')





**Return Value:** None

[Back to Top](#module-overview)


## \_compute\_alignment\_within\_screen
No description



**Signature:** (window, side='n')





**Return Value:** None

[Back to Top](#module-overview)


## align
No description



**Signature:** (window, parent=None, side='n', correction=(0, 0))





**Return Value:** None

[Back to Top](#module-overview)


## center
Returns the coords tuple: (x, y)



**Signature:** (window, parent=None, correction=(0, 0))





**Return Value:** None

[Back to Top](#module-overview)


## compute\_alignment
Compute the x, y coords to perform an alignment.
Legal sides are: n, s, w, e, nw, sw, ne, se.
If you don't submit a parent, the screen will be considered as parent



**Signature:** (window, parent=None, side='n')





**Return Value:** None

[Back to Top](#module-overview)


## compute\_center
Compute the x, y coords to set the window in the center of parent.
If parent is None, the screen will be considered as parent



**Signature:** (window, parent=None)





**Return Value:** None

[Back to Top](#module-overview)


## get\_geometry
Return a tuple: width, height, coord_x, coord_y



**Signature:** (window)





**Return Value:** None

[Back to Top](#module-overview)


## hide\_early
Hide a window before a relocation



**Signature:** (window)





**Return Value:** None

[Back to Top](#module-overview)


## make\_modal
turn into a modal window ! dialog effect !



**Signature:** (window)





**Return Value:** None

[Back to Top](#module-overview)


## relocate
No description



**Signature:** (window, x, y, correction=(0, 0))





**Return Value:** None

[Back to Top](#module-overview)


## restore\_coords
No description



**Signature:** (window, name=None, default=None)





**Return Value:** None

[Back to Top](#module-overview)


## restore\_geometry
No description



**Signature:** (window, name=None, default=None)





**Return Value:** None

[Back to Top](#module-overview)


## restore\_size
No description



**Signature:** (window, name=None, default=None)





**Return Value:** None

[Back to Top](#module-overview)


## save\_coords
No description



**Signature:** (window, name=None)





**Return Value:** None

[Back to Top](#module-overview)


## save\_geometry
No description



**Signature:** (window, name=None)





**Return Value:** None

[Back to Top](#module-overview)


## save\_size
No description



**Signature:** (window, name=None)





**Return Value:** None

[Back to Top](#module-overview)


