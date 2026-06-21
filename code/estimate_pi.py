#!/usr/bin/env python3
"""
Estimate pi by Monte Carlo -- the "throw random darts" method.

Throw N random darts at a 1 x 1 square. The fraction that land inside the
quarter circle (radius 1, centered at the corner) is about pi/4, so

    pi  ~=  4 * (darts inside) / (total darts)

We already KNOW pi, so this is really a *test* of the method: we can compare
our estimate to the true value and watch the error shrink as N grows. Once we
trust it here, we use the same idea on problems where the answer is unknown.

Run:
    python estimate_pi.py

Dependencies: numpy
"""

import random
import numpy as np


def estimate_pi_loop(n):
    """Plain-Python version (easy to read): throw n darts one at a time."""
    inside = 0
    for _ in range(n):
        x, y = random.random(), random.random()      # a random dart in the unit square
        if x * x + y * y <= 1.0:                      # within distance 1 of the corner?
            inside += 1
    return 4.0 * inside / n


def estimate_pi(n, rng=None):
    """NumPy version (fast): throw all n darts at once."""
    rng = rng or np.random.default_rng()
    x = rng.random(n)
    y = rng.random(n)
    inside = np.count_nonzero(x * x + y * y <= 1.0)   # darts inside the quarter circle
    return 4.0 * inside / n


if __name__ == "__main__":
    # --- one run -------------------------------------------------------------
    N = 1_000_000
    pi_est = estimate_pi(N)
    error = abs(pi_est - np.pi)        # only possible because we already know pi
    print(f"darts    = {N:,}")
    print(f"estimate = {pi_est:.5f}")
    print(f"true pi  = {np.pi:.5f}")
    print(f"error    = {error:.5f}")

    # --- watch the error shrink as N grows (the Law of Large Numbers) --------
    print("\n        N        estimate      error")
    print("    ----------------------------------")
    for n in [100, 1_000, 10_000, 100_000, 1_000_000]:
        est = estimate_pi(n)
        print(f"    {n:>9,}    {est:.5f}     {abs(est - np.pi):.5f}")
