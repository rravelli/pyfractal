import matplotlib.pyplot as plt
from pyfractal.generator import mandelbrot_sequence
import numpy as np


def is_in_MandelBrot(c: complex, max_iter: int = 50) -> bool:
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
    limit = 2
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
    plot: bool = True,
    save: bool = True,
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
    plot: bool
        whether or not to plot the image in a matplotlib figure
    save : bool
        whether or not to save the generated image
    """

    x_size = int((zmax.real - zmin.real) / pixel_size)
    y_size = int((zmax.imag - zmin.imag) / pixel_size)

    Y, X = np.ix_(np.arange(y_size), np.arange(x_size))

    C = X * pixel_size + zmin.real + (Y * pixel_size + zmin.imag) * 1j
    Z = np.zeros(C.shape)
    for _ in range(max_iter):
        Z = Z * Z + C

    image = abs(Z) < 2

    if save:
        plt.imsave(fname=figname, arr=image)
    if plot:
        plt.imshow(
            image,
            extent=[zmin.real, zmax.real, zmin.imag, zmax.imag],
            cmap="binary",
        )
        plt.title(figname)
        plt.show()
