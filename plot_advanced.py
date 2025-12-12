import numpy as np
import matplotlib.pyplot as plt
from math import pi, exp

# -----------------------------
# Distribuição GUE (Wigner)
# -----------------------------
def gue_pdf(s):
    return (32 / (pi**2)) * s**2 * np.exp(-4 * s**2 / pi)

def gue_cdf(s):
    return 1 - np.exp(-4 * s**2 / pi) * (1 + 4 * s**2 / pi)

# -----------------------------
# Plot avançado
# -----------------------------
def advanced_gap_plot(gaps, output="gaps_advanced.png"):

    gaps = np.array(gaps)
    gaps = gaps[gaps > 0]

    fig = plt.figure(figsize=(14, 10))
    grid = fig.add_gridspec(2, 2)

    # 1️⃣ Histograma + PDF GUE
    ax1 = fig.add_subplot(grid[0, 0])
    s = np.linspace(0, max(gaps)*1.1, 400)

    ax1.hist(
        gaps, bins=40, density=True,
        alpha=0.6, label="Empirical gaps"
    )
    ax1.plot(s, gue_pdf(s), linewidth=2, label="GUE (Wigner)")
    ax1.set_title("Normalized Gap Distribution")
    ax1.set_xlabel("s")
    ax1.set_ylabel("Density")
    ax1.legend()

    # 2️⃣ CDF empírica vs GUE
    ax2 = fig.add_subplot(grid[0, 1])

    gaps_sorted = np.sort(gaps)
    ecdf = np.arange(1, len(gaps_sorted)+1) / len(gaps_sorted)

    ax2.plot(gaps_sorted, ecdf, label="Empirical CDF")
    ax2.plot(s, gue_cdf(s), linewidth=2, label="GUE CDF")
    ax2.set_title("CDF Comparison")
    ax2.set_xlabel("s")
    ax2.set_ylabel("CDF")
    ax2.legend()

    # 3️⃣ Correlação gapₙ vs gapₙ₊₁
    ax3 = fig.add_subplot(grid[1, 0])

    ax3.scatter(
        gaps[:-1], gaps[1:],
        s=15, alpha=0.6
    )
    ax3.set_title("Gap Correlation: $s_n$ vs $s_{n+1}$")
    ax3.set_xlabel("$s_n$")
    ax3.set_ylabel("$s_{n+1}$")

    # 4️⃣ Heatmap de densidade (estrutura fina)
    ax4 = fig.add_subplot(grid[1, 1])

    h = ax4.hist2d(
        gaps[:-1], gaps[1:],
        bins=40, cmap="inferno"
    )
    plt.colorbar(h[3], ax=ax4)
    ax4.set_title("Gap Density Heatmap")
    ax4.set_xlabel("$s_n$")
    ax4.set_ylabel("$s_{n+1}$")

    plt.tight_layout()
    plt.savefig(output, dpi=300)
    plt.close()

    print(f"Plot salvo em: {output}")
