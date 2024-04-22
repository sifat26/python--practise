import numpy as np
import matplotlib.pyplot as plt

# Data
X = ['Group A', 'Group B', 'Group C', 'Group D']
Ygirls = [10, 20, 20, 40]
Zboys = [20, 30, 25, 30]

# Create an array with the positions of each group
X_axis = np.arange(len(X))

# Plot bars for girls and boys
plt.bar(X_axis - 0.2, Ygirls, 0.4, label='Girls', color='pink')
plt.bar(X_axis + 0.2, Zboys, 0.4, label='Boys', color='blue')

# Add xticks on the middle of the group bars
plt.xticks(X_axis, X)

# Add labels and title
plt.xlabel("Groups")
plt.ylabel("Number of Students")
plt.title("Number of Students in each group")

# Add legend
plt.legend()

# Show plot
plt.show()
