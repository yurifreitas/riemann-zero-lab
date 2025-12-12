from adaptive_scan import adaptive_intervals
from zero_finder import find_zero

def process_gram_block(args):
    a, b = args
    zeros = []

    for x, y in adaptive_intervals(a, b):
        z = find_zero(x, y)
        if z is not None:
            zeros.append(z)

    return zeros
