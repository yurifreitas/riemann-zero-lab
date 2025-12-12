from z_fast import Z_fast

def gram_failures(gram_points):
    """
    Detecta falhas da Lei de Gram:
    Z(g_n) e Z(g_{n+1}) não alternam sinal
    """
    failures = []
    for i in range(len(gram_points) - 1):
        g0, g1 = gram_points[i], gram_points[i+1]
        z0, z1 = Z_fast(float(g0)), Z_fast(float(g1))
        if z0 * z1 > 0:
            failures.append((g0, g1))
    return failures
