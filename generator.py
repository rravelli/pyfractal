def sequence(z, c) -> complex:
    """Générateur des éléments de la suite $z_{n+1}=z_n^2+c$
    c.f. Chapitre 2"""
    while True:
        yield z
        z = z**2 + c


def suite_mandelbrot(c) -> complex:
    """_summary_

    Args:
        c (_type_): _description_

    Returns:
        complex: _description_
    """
    return sequence(0, c)
