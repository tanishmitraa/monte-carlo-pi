import numpy as np

def monte_carlo_pi(N):
    x = np.random.uniform(-1, 1, N)
    y = np.random.uniform(-1, 1, N)
    inside = np.sum(x**2 + y**2 <= 1)
    return 4 * (inside / N)

if __name__ == "__main__":
    while True:
        N = int(input("Enter number of samples (0 to quit): "))
        if N == 0:
            break
        print("Estimated pi:", monte_carlo_pi(N))
