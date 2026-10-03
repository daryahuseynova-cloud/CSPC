"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: write k_imbalance(x) = (2x)^2/((a-x)(b-x)) - K.
#         It equals zero exactly at equilibrium.
def k_imbalance(x):
        z =(2*x)**2/((a-x)*(b-x)) - K
        return z

# TODO 2 (method 1): use scipy.optimize.newton to find the root of k_imbalance
#         (start x0=0.5). This is root-finding.

x1=newton(k_imbalance,x0=0.5)

# TODO 3 (method 2): use scipy.optimize.minimize to minimise k_imbalance(x)**2
#         (method "SLSQP", bounds [(0, 0.999)], x0=[0.5]). Print both answers
#         and confirm they agree.
def square(x):
        return k_imbalance(x)**2

x2=minimize(square,method="SLSQP",bounds=[(0, 0.999)],x0=[0.5])

print(f"newton: x = {x1:.6f}, minimize: x = {x2.x[0]:.6f}")
# TODO 4: report the equilibrium amounts (H2, I2, HI), and plot how the three
#         amounts change with the extent x, marking the equilibrium. Save
#         equilibrium.png.
print(f"equilibrium is reached at H2={1-x2.x[0]:.6f}, I2={1-x2.x[0]:.6f} and HI={2*x2.x[0]:.6f}")
xs=np.linspace(0, 0.999,200)

plt.plot(xs,1-xs,color="green",linewidth=4, label="H2")
plt.plot(xs,1-xs,color="red", linewidth=1.5,linestyle="--",label="I2")
plt.plot(xs,2*xs,color="purple",label="HI")
plt.xlabel("extent")
plt.ylabel("amount")
plt.title("Equilibrium composition vs extent")
plt.axvline(x2.x[0], color="black", linestyle="--", label="equilibrium point")
plt.savefig("equilibrium.png")
plt.legend()
plt.show()
