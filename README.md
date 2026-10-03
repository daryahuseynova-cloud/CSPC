# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.
## Setup
Create the environment for a given lab:
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc
---
## PW1 - Lab A: Reproducible Foundations
**What I built:**
- Created the CSPC repository and conda environment.
- Added the decay simulation, tests, and speed comparison using NumPy.
**Speed comparison (loop vs NumPy):**
- loop : 3.835 s
- numpy :0.000 s
- speed-up: 12868.1 x faster
**Tests:** all passing? (yes / no) yes
**Conclusion:**
- I successfully created the repository, environment, tests, and speed comparison.
All three tests passed.
The NumPy implementation was faster than the pure-Python loop, showing the advantage of vectorized numerical calculations.
---
## PW1 - Lab B: Data, Plotting, and Automation

**What I built:**
- A Python script (`plot.py`) that imports experimental decay data, calculates an analytical exponential decay curve (N0 * exp(-LAMBDA * t)), and generates a side-by-side comparison plot (`figure.png`).
- An automated Snakemake pipeline (`Snakefile`) to manage figure generation.

**Data & Model Comparison:**
- **Data observed:** The observed data showed a clear exponential decay of counts over time.
- **Match with analytical law:** The observed data points closely matched the analytical decay law curve, showing good compatibility of experimental observations and the theoretical model.

**Snakemake Pipeline:**
- The Snakemake workflow automatically generates `figure.png` from `decay_observed.csv` using `plot.py`, re-executing the code only when input files are modified.

**Conclusion:**
- Successfully automated the data plotting workflow and verified that the experimental decay fits the theoretical analytical model. I learned how to use Snakemake for reproducible pipeline automation and how to create shared-axis subplots in Matplotlib.
---

## PW2 - Lab A: Motion from Tracking Data

**What I built:**
- A Python script (`analysis.py`) that reads noisy free-fall position data from `freefall.csv`, differentiates it twice with `np.gradient` to get velocity and acceleration, and integrates the acceleration back with `cumulative_trapezoid` to recover velocity and position.
- A figure (`motion.png`) with three stacked panels (position, velocity, acceleration vs time), with the true value -9.81 m/s^2 marked on the acceleration panel.

**Measured acceleration:**
- mean acceleration: -8.580 m/s^2 (expected: -9.81 m/s^2, difference: 1.23 m/s^2)
- standard deviation of acceleration: 28.7 m/s^2

**Why the acceleration is noisy:**
- The acceleration is noisy because differentiating twice divides the small random measurement errors in position by the tiny time step squared, which amplifies them enormously, while the position values themselves are not divided by anything, so the same errors stay too small to see.
- The mean is close to -9.81 but not exact, because the mean of a second derivative depends mostly on the noisy first and last velocity values.

**What integrating back showed:**
- The position recovered by integration matches the measured position closely. The largest difference was 0.785 m.
- Integration sums many points multiplied by a small time step, so the random errors (positive and negative) largely cancel out instead of growing. It cleaned up the noise that differentiation had amplified.

**Conclusion:**
- Differentiating noisy data amplifies the noise, while integrating smooths it. I learned how to use `np.gradient` and `cumulative_trapezoid`, and how to make stacked subplots with a reference line in Matplotlib.

## PW2 - Lab B: Optimization in Chemistry

**What I built:**
- `warmup.py`: compares gradient descent (by hand), Newton's method (`scipy.optimize.newton` on the derivative) and SLSQP (`scipy.optimize.minimize`) on an easy function f(x) = (x-3)^2 + 1 and a harder one g(x) = x^4 - 3x^2 + x + 5.
- `kinetics.py`: reads `kinetics.csv`, defines a sum-of-squares `total_error(k)` for the first-order decay C(t) = C0 e^(-kt), and fits k with SLSQP (bounds 0 to 5, x0 = 0.5). Output: `kinetics.png`.
- `equilibrium.py`: finds the extent x of H2 + I2 <=> 2 HI for K = 15.6 by root-finding (Newton) and by minimising the squared imbalance (SLSQP). Output: `equilibrium.png`.
- [bonus, if done] `titration.py`: finds the equivalence point from the steepest slope of the pH curve. Output: `titration.png`.

**How the three methods compared (Part 2):**
- On the easy convex function f, all three reached x = 3 (f = 1). Newton needed about 1 step because f' is linear, gradient descent needed 102 steps with lr = 0.1.
- On g, the methods did not all agree. g has three stationary points (x = -1.300840, 0.169938, 1.130901): two minima and one maximum, with the global minimum at x = -1.300840.
- From x0 = 0, Newton landed on x = 0.169938, where d2g = -5.653451 < 0, so it found a maximum, not a minimum. Newton only solves g'(x) = 0 and cannot tell a minimum from a maximum, which is why the sign of 2dg must be checked.
- From x0 = 2, Newton landed on x = 1.130901 , where d2g = 9.347248 > 0, a local minimum.
- Gradient descent: from x0 = 0 it ended at x = -1.300840 and from x0 = 2 at x = -1.300840 . SLSQP: from x0 = 0 at x = -1.300857 and from x0 = 2 at x -1.300639.
- The starting point changes which stationary point is reached. On a simple convex problem the methods agree easily; on a complicated landscape the starting point and the algorithm matter.

**Fitted rate constant (Part 3):**
- Fitted k = 0.261761 (expected about 0.25), with a minimum total error of 266.129419.
- The fitted curve passes through the data, and the points scatter randomly above and below it with no systematic pattern, so the first-order model is appropriate.
- Some measured concentrations at late times are slightly negative, which is just measurement noise since real concentrations cannot be negative.

**Equilibrium composition (Part 4):**
- Newton (root-finding) gave x = 0.663848 and SLSQP on the squared imbalance gave x = 0.663847, so the two methods agree.
- Equilibrium amounts: H2 = I2 = 0.336153 mol and HI = 1.327695 mol. Check: (2x)^2 / (1-x)^2 = 15.6.
- Minimising k_imbalance directly would not work, because it goes negative on one side of the root. Squaring it makes the root the minimum.
- Since K > 1, the products are favoured, so more than half of the reactants are converted.

**Conclusion:**
- Optimization appears in chemistry as curve fitting (kinetics), root-finding (equilibrium). I learned that Newton finds stationary points rather than guaranteed minima, that the starting point matters on complicated functions, and that squaring a function turns a root-finding problem into a minimisation problem.