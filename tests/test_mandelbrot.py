from pyfractal import mandelbrot


def test_is_in_mandelbrot():
    """Tests returned value of function is_in_mandelbrot()
    for several inputs."""
    assert mandelbrot.is_in_MandelBrot(0.251)
    assert mandelbrot.is_in_MandelBrot(0.1 + 0.1j, 100)
    assert not mandelbrot.is_in_MandelBrot(0.251, 100)
    assert not mandelbrot.is_in_MandelBrot(1.1 + 0.1j, 100)
