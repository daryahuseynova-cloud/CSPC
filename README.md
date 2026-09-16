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
- A Python script ('plot.py') that imports experimental decay data, calculates an analytical exponential decay curve (N0 * exp(-LAMBDA * t)), and generates a side-by-side comparison plot ('figure.png').
- An automated Snakemake pipeline ('Snakefile') to manage figure generation.

**Data & Model Comparison:**
- **Data observed:** The observed data showed a clear exponential decay of counts over time.
- **Match with analytical law:** The observed data points closely matched the analytical decay law curve, showing good compatibility of experimental observations and the theoretical model.

**Snakemake Pipeline:**
- The Snakemake workflow automatically generates 'figure.png' from 'decay_observed.csv' using 'plot.py', re-executing the code only when input files are modified.

**Conclusion:**
- Successfully automated the data plotting workflow and verified that the experimental decay fits the theoretical analytical model. I learned how to use Snakemake for reproducible pipeline automation and how to create shared-axis subplots in Matplotlib.