import mpmath as mp

mp.mp.dps = 60

T_START = 10_000.0
T_END   = 10_200.0

STEP    = 5.0
OVERLAP = 1.0

ZERO_TOL = mp.mpf("1e-12")
