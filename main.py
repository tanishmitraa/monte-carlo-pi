import numpy as np
N=10**7
def monte_carlo_pi(N):
    inside = 0
    x = np.random.uniform(-1, 1, N)
    y = np.random.uniform(-1, 1, N)
    inside = np.sum(x**2 + y**2 <= 1)
    inside += 1
    return 4 * (inside / N)
print("Estimated pi:", monte_carlo_pi(N))
