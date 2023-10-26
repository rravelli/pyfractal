from pyfractal import generator

def test_sequence():
    true_values=[(3+2j),(7+12j),(-93+168j),(-19573-31248j),()]
    test_values = generator.sequence(3+2j,2)
    for n in range(4):
        assert next(test_values)==true_values[n]
          
