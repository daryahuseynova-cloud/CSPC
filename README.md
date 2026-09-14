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