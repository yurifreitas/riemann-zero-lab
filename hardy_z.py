import mpmath as mp
from theta import theta

def Z(t):
    t = mp.mpf(t)
    th = theta(t)
    N = int(mp.sqrt(t/(2*mp.pi)))
    s = mp.mpf(0)

    for n in range(1, N+1):
        s += mp.cos(th - t*mp.log(n)) / mp.sqrt(n)

    return 2*s
