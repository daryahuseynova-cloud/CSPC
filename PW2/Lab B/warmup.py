"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize

# ---------- 2A: easy convex function ----------
def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

# TODO 2A: minimise f three ways from x0=0 and print each result:
#   (1) gradient descent by hand (loop x = x - lr*df(x) until the step is tiny)
#   (2) scipy.optimize.newton(df, x0, fprime=d2f)
#   (3) scipy.optimize.minimize(f, x0, method="SLSQP")



#(1) gradient descent by hand
def grad_des(y, dy, x0, lr, tol):
  x=x0
  steps=0
  while True:
    step=dy(x)*lr
    x=x-step
    steps+=1
    if abs(step)<tol:
      break
  print(f"Gradient descent: x={x:.6f}, f(x)={y(x):.6f}, steps={steps}")

grad_des(f, df, x0=0.0, lr=0.1, tol=1e-10)


#(2) scipy.optimize.newton(df, x0, fprime=d2f)
x_newt=newton(df, x0=0, fprime=d2f)
print(f"Newton: x={x_newt:.6f}, f(x)={f(x_newt):.6f}")

#(3) scipy.optimize.minimize(f, x0, method="SLSQP")
result=minimize(f, x0=0, method="SLSQP")
print(f"SLSQP: x={result.x[0]:.6f}, f(x)={result.fun:.6f}")


# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

# TODO 2B: run the same three methods on g, from x0=0 AND from x0=2.
#   For Newton (which solves dg(x)=0), also check the sign of d2g at the answer:
#   d2g > 0 means a minimum, d2g < 0 means a maximum.
#   In your README note: do the methods agree? did Newton find a minimum or
#   another stationary point? how did the starting point change the result?


print("\n\tfor function g(x):")

#(1) gradient descent by hand
print("for x0=0: ")
grad_des(g, dg, x0=0.0, lr=0.1, tol=1e-10)
print("\nfor x0=2: ")
grad_des(g, dg, x0=2.0, lr=0.1, tol=1e-10)

#(2) scipy.optimize.newton

def classify(x, d2y):
  a=d2y(x)
  if a>0:
    point="minimum"
  elif a<0:
    point="maximum"
  else:
    point="inconclusive (d2g = 0)"
  print(f"d2g({x:.6f})={d2y(x):.6f}, which is {point}")

  
print("\nfor x0=0: ")
x_newt1=newton(dg, x0=0, fprime=d2g)
print(f"Newton: x={x_newt1:.6f}, g(x)={g(x_newt1):.6f}")
classify(x_newt1,d2g)

print("\nfor x0=2: ")
x_newt2=newton(dg, x0=2, fprime=d2g)
print(f"Newton: x={x_newt2:.6f}, g(x)={g(x_newt2):.6f}")
classify(x_newt2,d2g)

#(3) scipy.optimize.minimize(g, x0, method="SLSQP")
print("\nfor x0=0: ")
result1=minimize(g, x0=0, method="SLSQP")
print(f"SLSQP: x={result1.x[0]:.6f}, g(x)={result1.fun:.6f}")
print("\nfor x0=2: ")
result2=minimize(g, x0=2, method="SLSQP")
print(f"SLSQP: x={result2.x[0]:.6f}, g(x)={result2.fun:.6f}")