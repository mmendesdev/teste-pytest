from math_functions import eh_par

def test_eh_par():
    assert eh_par(2) is True   
    assert eh_par(3) is False  
    assert eh_par(0) is True   
    assert eh_par(-2) is True 
    assert eh_par(-3) is False 
