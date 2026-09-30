"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
#         (hint: np.loadtxt with a comma delimiter, skipping the header)
t, y = np.loadtxt("freefall.csv", delimiter=",", skiprows=1, unpack=True)


# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?
veloc_s=np.gradient(y, t)
acc_s=np.gradient(veloc_s,t)
acc_aver=np.mean(acc_s)
print(f"the average acceleration of the object is {acc_aver:.3f}.std of acceleration: {np.std(acc_s):.1f}")
#it differs from the needed value by 1.23 m/s^2 because of the noise in velocity and acceleration values


# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)

veloc_rec=cumulative_trapezoid(acc_s, t, initial=0) + veloc_s[0]
y_rec=cumulative_trapezoid(veloc_rec,t,initial=0)+y[0]
max_diff = np.max(np.abs(y_rec - y))
print(f"largest difference between recovered and original position: {max_diff:.3f} m")


# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png
fig, (pos, vel, acc) = plt.subplots(3, 1, sharex=True, figsize=(7, 9))

pos.scatter(t, y, color="green", s=15, label="measured y")
pos.plot(t, y_rec, color="black", label="recovered (integrated)")
pos.set_title("y position")
pos.set_ylabel("position")
pos.legend()

vel.scatter(t, veloc_s, color="red", s=15, label="derivative of y")
vel.plot(t, veloc_rec, color="black", label="recovered (integrated)")
vel.set_title("velocity")
vel.set_ylabel("velocity")
vel.legend()

acc.scatter(t, acc_s, color="purple", label="acceleration", s=15)
acc.set_title("acceleration")
acc.set_xlabel("Time")
acc.set_ylabel("acceleration")

acc.axhline(-9.81, color="black", linestyle="--", label="true g = -9.81")
acc.legend()

plt.tight_layout()
plt.savefig("motion.png")
plt.show()