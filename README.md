# Faculty_Candidate_Lecture

# CDS 230 — Stochastic Models: Monte Carlo & Markov Chains

A sample teaching lesson for **CDS 230 (Modeling and Simulation I)**, covering syllabus
Topic 17 — *Stochastic Models* — with both halves of the topic: **Monte Carlo methods**
and **Markov chains**. The lesson is built to be hands-on and code-first: every idea is
something students can run, not just watch.

---

## What the lesson covers

Starting from one everyday question — *how long is the drive from New York to Florida?* —
the lesson builds up the idea of **stochastic models** (models with randomness built in)
and the two main tools for working with them:

- **Monte Carlo** — use independent random samples to estimate an answer.
  Worked examples: estimating **π** by throwing random darts, and turning the road-trip
  question into a full **distribution** of travel times.
- **Markov chains** — random processes that evolve step by step, where the next state
  depends only on the current one (the *memoryless* property). Worked example: a
  **weather** chain (Sunny / Cloudy / Rainy) settling into a long-run **steady state**.

---

## Repository contents

```
presentation/
  Monte_Carlo_Pi_CDS230.pptx     Full ~20-slide teaching deck
  Weather_6day_iteration.pptx    Standalone worked example: 6 days of the weather chain
  Challenge_solutions.pptx       Answers to the in-class active-learning challenges

code/
  estimate_pi.py                 Minimal Monte Carlo π estimator (reports estimate + error)
  stochastic_demos.py            Animated demos: pi · roadtrip · markov

media/
  out_pi.gif                     Monte Carlo π: darts landing + estimate converging
  out_roadtrip.gif               Road-trip travel-time distribution building up
  out_markov.gif                 Weather Markov chain settling to its steady state
  weather_markov_diagram.png     Weather state diagram with transition probabilities
```

## Running the code

### Requirements

- Python 3.9+
- `numpy`, `matplotlib`
- `pillow` (only needed to save `.gif`), `ffmpeg` (only needed to save `.mp4`)

```bash
pip install numpy matplotlib pillow
```

### Estimate π

```bash
python code/estimate_pi.py
```

Prints the estimate and the error `|estimate − π|`. Increase `N` and watch the error shrink —
the Law of Large Numbers made visible.

### Animated demos

```bash
python code/stochastic_demos.py pi          # darts + π estimate converging
python code/stochastic_demos.py roadtrip    # a travel-time distribution building up
python code/stochastic_demos.py markov      # a weather chain settling to steady state
```

Useful flags:

| Flag | Meaning |
|------|---------|
| `--seed 7` | Reproducible run |
| `--frames 200` | Override the number of animation frames |
| `--save out.gif` | Save to a file instead of opening a window (`.gif` or `.mp4`) |

Each animation loops, so it can play on the side during a talk; or use `--save` to record it.

---

## Resources & links

- **Monte Carlo, in the real world (interactive):**
  [PortfolioVisualizer — Monte Carlo Simulation](https://www.portfoliovisualizer.com/monte-carlo-simulation)
  — runs thousands of random scenarios to produce a *distribution* of portfolio outcomes,
  exactly the same idea as the road-trip travel-time histogram.
- **Markov chains (interactive):**
  [Setosa — Markov Chains, visually explained](https://setosa.io/ev/markov-chains/)
- **Background reading:**
  [Monte Carlo method](https://en.wikipedia.org/wiki/Monte_Carlo_method) ·
  [Markov chain](https://en.wikipedia.org/wiki/Markov_chain) ·
  [Law of large numbers](https://en.wikipedia.org/wiki/Law_of_large_numbers)
- **Department:**
  [GMU Computational and Data Sciences](https://catalog.gmu.edu/colleges-schools/science/computational-data-sciences/)


---

## How to use this repo in class

1. Walk through the deck (`presentation/`), pausing at the live-code slides to run
   `estimate_pi.py`.
2. Play the matching animation from `media/` (or run it live with `stochastic_demos.py`).
3. Use the active-learning challenges near the end; `Challenge_solutions.pptx` has the answers.
4. `Weather_6day_iteration.pptx` is a slow, step-by-step worked example of the Markov chain
   if students want to see one iteration at a time.

---

## Author

*Shrabani Ghosh — sample teaching lesson, George Mason University, Department of Computational
and Data Sciences.*

## License

Released for educational use.
