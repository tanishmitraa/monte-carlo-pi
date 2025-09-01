import matplotlib.pyplot as plt
from main import monte_carlo_pi

x = []
y = []

while True:
    N = int(input("Enter number of samples (0 to quit): "))
    if N == 0:
        break

    estimate = monte_carlo_pi(N)
    print("Estimated pi:", estimate)

    x.append(N)
    y.append(estimate)

plt.plot(x, y, marker='o', label="Monte Carlo Estimate")
plt.axhline(y=3.14159, color='r', linestyle='--', label="π (True Value)")

plt.xlabel("Number of Points (N)")
plt.ylabel("Estimated π")
plt.title("Monte Carlo Estimation of π")
plt.legend()
plt.grid(True)
plt.show()
