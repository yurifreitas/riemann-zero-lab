import mpmath as mp
from theta import theta

def gram_sequence(T_start, T_end):
    T_start = mp.mpf(T_start)
    T_end   = mp.mpf(T_end)

    n = int(theta(T_start) / mp.pi)

    t = mp.findroot(lambda x: theta(x) - n * mp.pi, T_start)

    grams = []

    while t <= T_end:
        if t >= T_start:
            grams.append(t)

        dtheta = 0.5 * mp.log(t / (2 * mp.pi))
        t += mp.pi / dtheta
        n += 1

    return grams
