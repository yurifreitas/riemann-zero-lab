import mpmath as mp
import numpy as np

def normalized_gaps(zeros):
    """
    Retorna gaps normalizados:
    delta_n = (γ_{n+1} - γ_n) * log(γ_n / 2π) / (2π)
    """
    gaps = []
    for i in range(len(zeros) - 1):
        g = zeros[i+1] - zeros[i]
        norm = g * mp.log(zeros[i] / (2 * mp.pi)) / (2 * mp.pi)
        gaps.append(float(norm))
    return np.array(gaps)
