# Contenu de __main__.py
"""Main call to helloworld. Mostly a parser."""
import argparse
from pyfractal.mandelbrot import plot_mandelbrot
from pyfractal.julia import plot_julia


def cli_plot_mandelbrot():
    """Console command function for `plot_mandelbrot()`"""
    parser = argparse.ArgumentParser(
        description="Plot the Mandelbrot set and save it to an image file"
    )
    parser.add_argument(
        "--origin",
        "-o",
        metavar="origin",
        type=str,
        help="Name for generated image",
        required=True,
    )
    parser.add_argument(
        "--zmin",
        "-zmin",
        metavar="z minimum",
        type=complex,
        help="Lower bound for z",
        default=-2 - 1j,
    )
    parser.add_argument(
        "--zmax",
        "-zmax",
        metavar="name",
        type=complex,
        help="Upper bound for z",
        default=1 + 1j,
    )
    parser.add_argument(
        "--pixel_size",
        "-s",
        metavar="pixel_size",
        type=float,
        help="Size of one pixel",
        default=1e-3,
    )
    parser.add_argument(
        "--max_iter",
        "-i",
        metavar="max_iter",
        type=complex,
        help="Maximum number of iteration to run",
        default=50,
    )

    args = parser.parse_args()

    plot_mandelbrot(
        zmin=args.zmin,
        zmax=args.zmax,
        pixel_size=args.pixel_size,
        max_iter=args.max_iter,
        figname=args.origin,
        save=True,
        plot=True,
    )


def cli_plot_julia():
    """Console command function for `plot_mandelbrot()`"""
    parser = argparse.ArgumentParser(
        description="Plot the Julia set and save it to an image file"
    )
    parser.add_argument(
        "-c",
        metavar="c",
        type=complex,
        help="Value for the c parameter",
        required=True,
    )
    parser.add_argument(
        "--origin",
        "-o",
        metavar="origin",
        type=str,
        help="Name for generated image",
        required=True,
    )
    parser.add_argument(
        "--zmin",
        "-zmin",
        metavar="z minimum",
        type=complex,
        help="Lower bound for z",
        default=-2 - 1j,
    )
    parser.add_argument(
        "--zmax",
        "-zmax",
        metavar="name",
        type=complex,
        help="Upper bound for z",
        default=1 + 1j,
    )
    parser.add_argument(
        "--pixel_size",
        "-s",
        metavar="pixel_size",
        type=float,
        help="Size of one pixel",
        default=1e-3,
    )
    parser.add_argument(
        "--max_iter",
        "-i",
        metavar="max_iter",
        type=complex,
        help="Maximum number of iteration to run",
        default=50,
    )

    args = parser.parse_args()

    plot_julia(
        c=args.c,
        zmin=args.zmin,
        zmax=args.zmax,
        pixel_size=args.pixel_size,
        max_iter=args.max_iter,
        figname=args.origin,
        save=True,
        plot=True,
    )
