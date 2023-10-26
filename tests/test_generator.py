from pyfractal import generator


def test_sequence():
    epsilon = 0.00001
    true_values = [(3+2j), (7+12j), (-93+168j), (-19573-31248j), ()]
    test_values = generator.sequence(3+2j, 2)
    for n in range(4):
        assert abs(next(test_values)-true_values[n]) < epsilon


def test_mandelbrot_sequence():
    epsilon = 0.00001
    true_values_bounded = [(0), (0.1+0.1j), (0.1+0.12j), (0.0956+0.124j)]
    test_values_bounded = generator.mandelbrot_sequence(0.1+0.1j)
    for n in range(4):
        assert abs(next(test_values_bounded) -
                   true_values_bounded[n]) < epsilon

    true_values_unbounded = [(0), (5+5j), (5+55j), (-2995+555j)]
    test_values_unbounded = generator.mandelbrot_sequence(5+5j)
    for n in range(4):
        assert abs(next(test_values_unbounded) -
                   true_values_unbounded[n]) < epsilon
        
def test_julia_sequence():
    epsilon = 0.000000001
    true_values = [(0.1j), (0.29+0.5j), (0.1341+0.79j), (-0.30611719+0.711878j)]
    test_values = generator.julia_sequence(0.1j,0.3 + 0.5j)
    for n in range(4):
        assert abs(next(test_values) -
                   true_values[n]) < epsilon
