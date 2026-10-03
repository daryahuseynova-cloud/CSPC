"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.

A first-order reaction decays as  C(t) = C0 * exp(-k*t).  You have noisy
concentration-vs-time measurements; find the k that best matches them.
Complete the TODOs. Run:  python kinetics.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# TODO 1: read kinetics.csv (columns time, concentration) into arrays t, C.
#         Set C0 = the first concentration.

t, c = np.loadtxt("kinetics.csv",delimiter=",",skiprows=1,unpack=True)
c0=c[0]

# TODO 2: write total_error(k) = sum of (measured - C0*exp(-k*t))^2.
#         This is the "how bad" number: small when the model matches the data.

def total_error(k):
    pred_c=c0 * np.exp(-k*t)
    error=np.sum((c - pred_c)**2)
    return error

# TODO 3: minimise total_error with scipy.optimize.minimize (method "SLSQP",
#         bounds [(0, 5)], start x0=0.5). Print the fitted k.

result=minimize(total_error,method="SLSQP", bounds=[(0, 5)], x0=0.5)
print(f"the fitted k = {result.x[0]:.6f}, the error value = {result.fun:.6f}")

# TODO 4: plot the measured data (points) and your fitted curve (line) together.
#         Save as kinetics.png.
k=result.x[0]
c_fitted=c0 * np.exp(-k*t)
plt.scatter(t,c, color="red",label="measured data")
plt.plot(t,c_fitted,color="green",label=f"fitted for k={k:.6f}")
plt.xlabel("time")
plt.ylabel("concentration")
plt.legend()
plt.title("First-order decay fit")
plt.savefig("kinetics.png")
plt.show()