import matplotlib.pyplot as plt


variance = [2 ** i for i in range(9)]
bias_squared = sorted([2 ** i for i in range(9)], reverse=True)
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

# Show multiple series on the same chart
plt.plot(xs, variance, "g-", label="variance")
plt.plot(xs, bias_squared, "r--", label="bias^2")
plt.plot(xs, total_error, "b:", label="total error")
plt.legend(loc=9)  # top center
plt.xlabel("Model Complexity")
plt.xticks([])
plt.title("The Bias-Variance Trade-Off")
plt.show()
