import matplotlib.pyplot as plt
from pyfractal.generator import julia_sequence
import numpy as np


def is_in_Julia(c: complex, z: complex, max_iter: int = 50) -> bool:
    """
    Checks if c is in Julia set.

    Parameters
    ----------
    c : complex
        c parameter for Julia
    z : complex
        complex to be checked
    max_iter : int
        maximum number of iteration to go through

    Returns
    -------
    bool
        True if z is member of the Julia set, False otherwise
    """
    i = 0
    over_limit = False
    limit = 10
    for z in julia_sequence(z, c):
        # stop if z goes over the limit
        if abs(z) > limit:
            over_limit = True
            break
        # stop if i go over max iteration
        if i > max_iter:
            break
        i += 1
    return not over_limit


def plot_julia(
    c: complex,
    zmin: complex = -2 - 1j,
    zmax: complex = 1 + 1j,
    pixel_size: float = 1e-3,
    max_iter=50,
    figname: str = "Julia.png",
    save: bool = True,
):
    """
    Creates plot of the Julia set and saves it in PNG format.

    Parameters
    ----------
    c : complex,
        c parameter to use to generate the Julia set
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
            if is_in_Julia(c, x + y * 1j, max_iter=max_iter):
                image[j, i, :] = 0

    plt.imshow(image, extent=[zmin.real, zmax.real, zmin.imag, zmax.imag])
    plt.title(figname)
    plt.show()
    if save:
        plt.imsave(fname=figname, arr=image)
