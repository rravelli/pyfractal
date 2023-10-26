from pyfractal import julia


def test_is_in_julia():
    """Tests returned value of function is_in_julia() for several inputs.
    """
    assert julia.is_in_Julia(0.25+0.25j, 0.25) == True
    assert julia.is_in_Julia(0.2j, 0.3+0.5j, 100) == True
    assert julia.is_in_Julia(0.25+0.25j, 1, 100) == False
    assert julia.is_in_Julia(2, 0.3+0.5j, 100) == False
