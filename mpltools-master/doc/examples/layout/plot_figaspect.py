"""
============
Figure shape
============

Often, you want to adjust the shape (or aspect ratio) of a figure, but you
don't want to explicitly calculate its size. Matplotlib provides a function
called ``figaspect`` to fill this role. To adjust the aspect ratio of the
figure, ``plt.figaspect`` will change the *width* of the figure.  In contrast,
``layout.figaspect`` will change the *height* of the figure.  This behavior is
convenient if you have a fixed-width requirement (e.g., the width of columns in
a journal page or the width of a web page).

In this example, ``layout.figaspect`` creates a figure that fits comfortably
onto the page, while ``plt.figaspect`` does not.

"""
import numpy as np
import matplotlib.pyplot as plt

from mpltools import layout


x, y = np.random.normal(size=(2, 20))

aspect_functions = {'mpltools.layout.figaspect': layout.figaspect,
                    'matplotlib.pyplot.figaspect': plt.figaspect}

for label, figaspect in list(aspect_functions.items()):
    figsize = figaspect(0.5)
    fig, ax = plt.subplots(figsize=figsize)

    ax.plot(x, y, 'ro')
    ax.set_title(label)

plt.show()
