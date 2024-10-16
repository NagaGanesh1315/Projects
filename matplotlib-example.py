# Simple Ppyhton code used for graph

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]   # Provide your values of x-axis
y = [10, 40, 30, 65, 25]  # Provide your values of y-axis

# Creating the plot
plt.plot(x, y, marker='o')

# You can Add you lablel for X and Y axis.
# Label is what you wanted to see on the graph plot 
plt.xlabel('Day')
plt.ylabel('Income generation')
plt.title('Day-wise income graph')

# Show the plot
plt.show()
