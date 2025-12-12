import mpmath as mp
from theta import theta


def gram_point(n):
    """
    Resolve theta(t) = n*pi
    Chute inicial assintótico correto
    """
    n = mp.mpf(n)

    # chute inicial assintótico
    t0 = 2 * mp.pi * n / mp.log(n + 2)

    f = lambda t: theta(t) - n * mp.pi
    return mp.findroot(f, t0)


def gram_sequence(T_start, T_end):
    """
    Gera pontos de Gram no intervalo [T_start, T_end]
    """
    T_start = mp.mpf(T_start)
    T_end   = mp.mpf(T_end)

    n0 = int(theta(T_start) / mp.pi)
    grams = []

    n = n0
    while True:
        try:
            g = gram_point(n)
            if g > T_end:
                break
            if g >= T_start:
                grams.append(g)
        except:
            pass
        n += 1

    return grams
