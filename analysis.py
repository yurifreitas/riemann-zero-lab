from gaps import normalized_gaps
from gram import gram_sequence
from gram_check import gram_failures

def analyze_zeros(zeros, T_START, T_END):
    print("\n=== GAP STATISTICS ===")
    gaps = normalized_gaps(zeros)
    print(f"Total gaps: {len(gaps)}")
    print(f"Mean gap: {gaps.mean():.4f}")
    print(f"Std gap:  {gaps.std():.4f}")

    print("\n=== GRAM LAW CHECK ===")
    grams = gram_sequence(T_START, T_END)
    failures = gram_failures(grams)
    print(f"Gram points: {len(grams)}")
    print(f"Gram failures: {len(failures)}")

    if failures:
        print("First failures:")
        for g0, g1 in failures[:5]:
            print(f"  Failure between {g0} and {g1}")
