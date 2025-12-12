import mpmath as mp

def expected_zero_count(T):
    T = mp.mpf(T)
    return (
        (T/(2*mp.pi))*mp.log(T/(2*mp.pi))
        - T/(2*mp.pi)
        + mp.mpf("7")/8
    )

def turing_check_blockwise(blocks):
    for a, b, found in blocks:
        expected = expected_zero_count(b) - expected_zero_count(a)
        tol = max(2, 0.02*mp.log(b))
        if abs(found - expected) > tol:
            return False
    return True
