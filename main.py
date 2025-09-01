import numpy as np

def monte_carlo_pi(N):
    x = np.random.uniform(-1, 1, N)
    y = np.random.uniform(-1, 1, N)
    inside = np.sum(x**2 + y**2 <= 1)
    return 4 * (inside / N)

while True:
    N = int(input("Enter number of samples: (0 to exit)"))
    if N == 0:
        break
    print("Estimated pi:", monte_carlo_pi(N))
