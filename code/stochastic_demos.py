#!/usr/bin/env python3
"""
Stochastic Models -- live visual demos for a CDS 230 sample lesson.

Three self-contained animations you can run on screen (and screen-record),
or save straight to a .gif / .mp4 to play on the side during a talk.

    python stochastic_demos.py pi          # Monte Carlo: estimate pi with darts
    python stochastic_demos.py roadtrip     # a travel-time DISTRIBUTION building up
    python stochastic_demos.py markov       # a Markov chain settling to steady state

Save to a file instead of showing a window:
    python stochastic_demos.py roadtrip --save roadtrip.gif
    python stochastic_demos.py pi --save pi.mp4        # .mp4 needs ffmpeg installed

Options:
    --seed 7      reproducible run (omit for a fresh random run each time)
    --frames 200  number of animation frames

Dependencies: numpy, matplotlib  (+ pillow for .gif, ffmpeg for .mp4)
    pip install numpy matplotlib pillow
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Rectangle

# ---- color palette (matches the slide deck) ----
INK   = "#0F2A43"
TEAL  = "#2E86AB"
AMBER = "#F2A541"
SLATE = "#9DB4C8"
GOLD  = "#C77F00"
RED   = "#B5462F"
MUTE  = "#5A6B7B"

plt.rcParams.update({
    "figure.facecolor": "white",
    "axes.facecolor":   "white",
    "font.size":        12,
    "axes.titlesize":   15,
    "axes.titleweight": "bold",
    "axes.edgecolor":   SLATE,
})


def _style(ax):
    """Light, clean axes: drop the top/right spines."""
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.tick_params(colors=MUTE)
    ax.xaxis.label.set_color(MUTE)
    ax.yaxis.label.set_color(MUTE)


# ======================================================================
# 1) MONTE CARLO -- estimate pi by throwing random darts
# ======================================================================
def demo_pi(frames=220, batch=120, seed=None):
    rng = np.random.default_rng(seed)
    N = frames * batch
    x = rng.random(N)
    y = rng.random(N)
    inside = x * x + y * y <= 1.0          # which darts land in the quarter circle

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 5.2))
    fig.suptitle("Monte Carlo:  estimating \u03c0 by throwing random darts",
                 fontsize=16, fontweight="bold", color=INK)

    # --- left: the dartboard ---
    axL.set_aspect("equal")
    axL.set_xlim(0, 1); axL.set_ylim(0, 1)
    axL.set_xticks([]); axL.set_yticks([])
    th = np.linspace(0, np.pi / 2, 200)
    axL.plot(np.cos(th), np.sin(th), color=INK, lw=2.2, zorder=3)   # quarter circle
    axL.add_patch(Rectangle((0, 0), 1, 1, fill=False, edgecolor=INK, lw=1.8))
    sc_in  = axL.scatter([], [], s=7, c=AMBER, alpha=0.85, linewidths=0)
    sc_out = axL.scatter([], [], s=7, c=SLATE, alpha=0.7, linewidths=0)

    # --- right: the running estimate converging ---
    axR.set_xscale("log")
    axR.axhline(np.pi, color=AMBER, ls="--", lw=2, label="true \u03c0 = 3.14159")
    (line,) = axR.plot([], [], color=TEAL, lw=2.2, label="estimate")
    axR.set_xlim(batch * 0.8, N)
    axR.set_ylim(2.4, 4.0)
    axR.set_xlabel("number of darts (N)")
    axR.set_ylabel("estimate of \u03c0")
    axR.legend(loc="upper right", frameon=False, labelcolor=MUTE)
    _style(axR)

    ns, ests = [], []

    def update(f):
        k = (f + 1) * batch                       # darts revealed so far
        ins_k = inside[:k]
        sc_in.set_offsets(np.column_stack((x[:k][ins_k],  y[:k][ins_k])))
        sc_out.set_offsets(np.column_stack((x[:k][~ins_k], y[:k][~ins_k])))
        est = 4.0 * ins_k.sum() / k
        ns.append(k); ests.append(est)
        line.set_data(ns, ests)
        axL.set_title(f"darts: {k:,}      estimate: {est:.4f}", color=INK)
        return sc_in, sc_out, line

    fig.tight_layout(rect=[0, 0, 1, 0.95])
    anim = FuncAnimation(fig, update, frames=frames, interval=40,
                         blit=False, repeat=True)
    return fig, anim


# ======================================================================
# 2) MONTE CARLO -- a travel-time DISTRIBUTION building up trip by trip
# ======================================================================
def demo_roadtrip(frames=170, batch=400, seed=None):
    rng = np.random.default_rng(seed)
    N = frames * batch
    dist = 1200.0                                  # miles, New York -> Florida

    speed   = rng.normal(62, 4, N).clip(45, 75)    # avg moving speed, mph
    drive   = dist / speed                          # base driving hours
    traffic = rng.exponential(1.0, N)              # random congestion
    rain    = np.where(rng.random(N) < 0.35, rng.uniform(0.5, 2.0, N), 0.0)
    build   = np.where(rng.random(N) < 0.50, rng.uniform(0.2, 1.5, N), 0.0)
    rest    = (drive // 3.0) * rng.uniform(0.25, 0.55, N)
    total   = drive + traffic + rain + build + rest

    bins = np.linspace(15, 40, 52)
    fig, ax = plt.subplots(figsize=(10, 5.6))

    def update(f):
        k = (f + 1) * batch
        data = total[:k]
        ax.clear()
        ax.hist(data, bins=bins, color=TEAL, edgecolor="white", lw=0.4)
        med = np.median(data)
        p10, p90 = np.percentile(data, [10, 90])
        ax.axvspan(p10, p90, color=AMBER, alpha=0.10)
        ax.axvline(med, color=AMBER, lw=3)
        ax.set_xlim(15, 40)
        ax.set_yticks([])
        ax.set_xlabel("total travel time (hours)")
        ax.set_ylabel("number of simulated trips")
        _style(ax)
        over24 = (data > 24).mean() * 100
        ax.set_title(
            f"{k:,} simulated NY \u2192 FL trips     "
            f"median {med:.1f} h     {over24:.0f}% over 24 h",
            color=INK, fontsize=12.5)

    fig.tight_layout()
    anim = FuncAnimation(fig, update, frames=frames, interval=45,
                         blit=False, repeat=True)
    return fig, anim


# ======================================================================
# 3) MARKOV CHAIN -- traffic state hopping, settling to steady state
# ======================================================================
def demo_markov(frames=240, steps_per_frame=35, seed=None):
    rng = np.random.default_rng(seed)
    states = ["Sunny", "Cloudy", "Rainy"]
    colors = ["#E2A11C", "#7E8FA0", TEAL]          # sunny / cloudy / rainy
    # rows = today, cols = tomorrow  (Sunny, Cloudy, Rainy)
    P = np.array([[0.70, 0.20, 0.10],
                  [0.30, 0.40, 0.30],
                  [0.20, 0.40, 0.40]])

    # true stationary distribution (left eigenvector for eigenvalue 1)
    vals, vecs = np.linalg.eig(P.T)
    pi = np.real(vecs[:, np.argmin(np.abs(vals - 1))])
    pi = pi / pi.sum()

    counts = np.zeros(3)
    cur = 2                       # start rainy -- the chain will forget this
    history = []

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 5.2),
                                   gridspec_kw={"width_ratios": [1, 1.15]})
    fig.suptitle("Markov chain:  weather that remembers yesterday",
                 fontsize=16, fontweight="bold", color=INK)

    def update(f):
        nonlocal cur
        for _ in range(steps_per_frame):
            counts[cur] += 1
            history.append(cur)
            cur = rng.choice(3, p=P[cur])
        total = counts.sum()
        frac = counts / total

        # --- left: current weather + scrolling history strip ---
        axL.clear()
        axL.set_xlim(0, 1); axL.set_ylim(0, 1); axL.axis("off")
        axL.add_patch(plt.Circle((0.5, 0.72), 0.16, color=colors[cur], zorder=2))
        axL.text(0.5, 0.72, states[cur], ha="center", va="center",
                 color="white", fontsize=16, fontweight="bold", zorder=3)
        axL.text(0.5, 0.93, "today's weather", ha="center", color=MUTE, fontsize=11)
        recent = history[-60:]
        for i, st in enumerate(recent):
            axL.add_patch(Rectangle((0.04 + i * 0.0153, 0.30), 0.013, 0.10,
                                    color=colors[st]))
        axL.text(0.5, 0.20, "last 60 days", ha="center", color=MUTE, fontsize=11)

        # --- right: running share of days vs the true steady state ---
        axR.clear()
        axR.bar(states, frac * 100, color=colors, zorder=2)
        for j in range(3):                          # dashed target = steady state
            axR.hlines(pi[j] * 100, j - 0.42, j + 0.42,
                       color=INK, ls="--", lw=1.8, zorder=3)
        axR.set_ylim(0, 70)
        axR.set_ylabel("% of days in each state")
        axR.set_title(f"after {int(total):,} days   "
                      f"(dashed = true steady state)", color=INK)
        _style(axR)

    fig.tight_layout(rect=[0, 0, 1, 0.95])
    anim = FuncAnimation(fig, update, frames=frames, interval=45,
                         blit=False, repeat=True)
    return fig, anim


# ======================================================================
DEMOS = {"pi": demo_pi, "roadtrip": demo_roadtrip, "markov": demo_markov}


def main():
    p = argparse.ArgumentParser(description="Stochastic-models live demos.")
    p.add_argument("demo", nargs="?", default="pi", choices=DEMOS,
                   help="which animation to run (default: pi)")
    p.add_argument("--save", metavar="FILE",
                   help="save to .gif or .mp4 instead of showing a window")
    p.add_argument("--seed", type=int, default=None,
                   help="random seed for a reproducible run")
    p.add_argument("--frames", type=int, default=None,
                   help="override the number of animation frames")
    args = p.parse_args()

    kwargs = {"seed": args.seed}
    if args.frames:
        kwargs["frames"] = args.frames
    fig, anim = DEMOS[args.demo](**kwargs)

    if args.save:
        fps = 25
        if args.save.lower().endswith(".gif"):
            anim.save(args.save, writer="pillow", fps=fps)
        else:
            anim.save(args.save, writer="ffmpeg", fps=fps, dpi=120)
        print(f"saved -> {args.save}")
    else:
        plt.show()


if __name__ == "__main__":
    main()
