import numpy as np
from z_fast import Z_fast

def adaptive_intervals(t0, t1):
    steps = int(300 + 40*np.log(t1))
    ts = np.linspace(t0, t1, steps)
    zs = np.array([Z_fast(t) for t in ts])

    intervals = []
    for i in range(len(zs)-1):
        if zs[i]*zs[i+1] <= 0:
            intervals.append((ts[i], ts[i+1]))

    return intervals
