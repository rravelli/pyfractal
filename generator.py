def sequence(z, c) -> complex:
    """Generator of the elements of the sequence $z_{n+1}=z_n^2+c$

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


def mandelbrot_sequence(c:complex) -> complex:
    """
    Generator of the elements of the elements of the Mandelbrot sequence.
    Mandelbrot sequence is $z_{n+1}=z_n^2+c$ with $z_{0}=0$

    Parameters
    ----------
    c : complex
        c in the sequence $z_{n+1}=z_n^2+c$

    Yield   
    -----
    complex
        next value of the Mandelbrot sequence
    """
    return sequence(0, c)

def julia_sequence(z:complex,c=complex)-> complex:
    """
    Generator of the elements of the elements of the Julia sequence.
    Julia sequence is $z_{n+1}=z_n^2+c$ with $z_{0}!=0$

    Parameters
    ----------
    z : complex
        $z_{0}$ in the sequence $z_{n+1}=z_n^2+c$
    
    c : complex
        c in the sequence $z_{n+1}=z_n^2+c$

    Yield   
    -----
    complex
        next value of the Julia sequence
    """
    return sequence(z,c)
