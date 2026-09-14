import time
from decay import simulate, simulate_loop


N0 = 200000
lam = 0.4
dt = 0.05
steps = 200
seed = 0


start = time.perf_counter()
simulate_loop(N0, lam, dt, steps, seed)
end = time.perf_counter()
loop_time = end-start


start = time.perf_counter()
simulate(N0, lam, dt, steps, seed)
end = time.perf_counter()
numpy_time = end-start


print(f"Pure-Python loop takes {loop_time:.3f} seconds")
print(f"NumPy simulation takes {numpy_time:.3f} seconds")
print(f"NumPy version is {loop_time / numpy_time:.1f} times faster")

