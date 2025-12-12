import numpy as np
from math import log, sqrt, cos, pi

def theta_fast(t):
    return 0.5*t*log(t/(2*pi)) - 0.5*t - pi/8

def Z_fast(t):
    th = theta_fast(t)
    N = int(sqrt(t/(2*pi)))
    s = 0.0
    for n in range(1, N+1):
        s += cos(th - t*log(n)) / sqrt(n)
    return 2*s
