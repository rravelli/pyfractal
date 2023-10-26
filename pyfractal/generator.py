def sequence(z: complex, c: complex) -> complex:
    """Generator of the elements of the sequence z[n+1]=z[n]²+c

    Parameters
    ----------
    z : complex
        value of the precedent iteration of the sequence
    c : complex
        constant complex added

    Yield
    -----
    complex
        next value of the sequence
    """
    while True:
        yield z
        z = z**2 + c


def mandelbrot_sequence(c: complex) -> complex:
    """
    Generator of the elements of the elements of the Mandelbrot sequence.
    Mandelbrot sequence is z[n+1]=z[n]²+c with z[0]=0

    Parameters
    ----------
    c : complex
        c in the sequence z[n+1]=z[n]²+c

    Yield
    -----
    complex
        next value of the Mandelbrot sequence
    """
    return sequence(0, c)


def julia_sequence(z: complex, c: complex) -> complex:
    """
    Generator of the elements of the elements of the Julia sequence.
    Julia sequence is z[n+1]=z[n]²+c with z[0]!=0

    Parameters
    ----------
    z : complex
        z[0] in the sequence z[n+1]=z[n]²+c

    c : complex
        c in the sequence z[n+1]=z[n]²+c

    Yield
    -----
    complex
        next value of the Julia sequence
    """
    return sequence(z, c)
