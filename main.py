from config import *
from parallel_scan import process_gram_block
from turing_check import expected_zero_count

from multiprocessing import Pool, cpu_count
import numpy as np
import mpmath as mp

from plot_advanced import advanced_gap_plot
from gaps import normalized_gaps
from gram import gram_sequence
from gram_check import gram_failures


def deduplicate(xs, tol=5e-6):
    xs = sorted(xs)
    out = []
    for x in xs:
        if not out or abs(x - out[-1]) > tol:
            out.append(x)
    return out


if __name__ == "__main__":

    # =========================
    # 1. BUSCA DOS ZEROS
    # =========================

    search_blocks = []
    t = T_START
    while t < T_END:
        search_blocks.append((t, min(t + STEP + OVERLAP, T_END)))
        t += STEP

    with Pool(cpu_count()) as p:
        results = p.map(process_gram_block, search_blocks)

    all_zeros = deduplicate([z for sub in results for z in sub])

    print(f"\nZeros encontrados: {len(all_zeros)}")
    print("Primeiros zeros:")
    for z in all_zeros[:10]:
        print(z)

    # =========================
    # 2. TURING CHECK
    # =========================

    count_blocks = [
        (t, min(t + STEP, T_END))
        for t in np.arange(T_START, T_END, STEP)
    ]

    turing_ok = True
    for a, b in count_blocks:
        found = sum(1 for z in all_zeros if a <= z < b)

        expected = (
            expected_zero_count(mp.mpf(b))
            - expected_zero_count(mp.mpf(a))
        )

        tol = max(mp.mpf(2), mp.mpf("0.02") * mp.log(b))

        if abs(mp.mpf(found) - expected) > tol:
            turing_ok = False
            break

    print("\nTuring check:", turing_ok)

    # =========================
    # 3. GAP STATISTICS
    # =========================

    gaps = normalized_gaps(all_zeros)
    advanced_gap_plot(gaps)

    print("\n=== GAP STATISTICS ===")
    print(f"Total gaps: {len(gaps)}")
    print(f"Mean gap: {gaps.mean():.6f}")
    print(f"Std  gap: {gaps.std():.6f}")
    print(f"Min  gap: {gaps.min():.6f}")
    print(f"Max  gap: {gaps.max():.6f}")

    # =========================
    # 4. LEI DE GRAM (CORRETA)
    # =========================

    grams = gram_sequence(T_START, T_END)
    failures = gram_failures(grams, all_zeros)

    print("\n=== GRAM LAW CHECK ===")
    print(f"Gram points: {len(grams)}")
    print(f"Gram failures: {len(failures)}")

    if failures:
        print("First Gram failures:")
        for g0, g1, count in failures[:5]:
            print(f"  [{count} zeros] between {g0} and {g1}")
