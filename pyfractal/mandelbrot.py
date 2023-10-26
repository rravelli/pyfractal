import matplotlib.pyplot as plt
from pyfractal.generator import mandelbrot_sequence
import numpy as np


def is_in_MandelBrot(c: complex, max_iter: int) -> bool:
    """
    Checks if c is in Mandelbrot set.

    Parameters
    ----------
    c : complex
        complex to be checked
    max_iter : int
        maximum number of iteration to go through

    Returns
    -------
    bool
        True if c is member of the Mandelbrot set, False otherwise
    """
    i = 0
    over_limit = False
    limit = 10
    for z in mandelbrot_sequence(c):
        # stop if z goes over the limit
        if abs(z) > limit:
            over_limit = True
            break
        # stop if i go over max iteration
        if i > max_iter:
            break
        i += 1
    return not over_limit


def plot_mandelbrot(
    zmin: complex = -2 - 1j,
    zmax: complex = 1 + 1j,
    pixel_size: float = 1e-3,
    max_iter=50,
    figname: str = "Mandelbrot.png",
):
    """
    Creates plot of the Mandelbrot set and saves it in PNG format.

    Parameters
    ----------
    zmin : complex
        min affix in the plot. Default to -2-1j
    zmax : int
        max affix in the plot. Default to 1+1j
    pixel_size : float
        size of a pixel on the plot. Default to 1e-3
    max_iter : int
        maximum number of iteration to go through. Default to 50
    figname : str
        name of the output PNG plot. Default to "Mandelbrot.png"
    """
    x_size = int((zmax.real - zmin.real) / pixel_size)
    y_size = int((zmax.imag - zmin.imag) / pixel_size)

    image = np.zeros([y_size, x_size, 3], dtype=np.uint8)
    image.fill(255)
    x = zmin.real
    for i in range(x_size):
        x += pixel_size
        y = zmin.imag
        for j in range(y_size):
            y += pixel_size
            if is_in_MandelBrot(x + y * 1j, max_iter=max_iter):
                image[j, i, :] = 0

    plt.imshow(image)
    plt.show()
    plt.imsave(fname=figname, arr=image)
