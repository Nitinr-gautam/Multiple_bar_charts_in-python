import matplotlib.pyplot as plt
import numpy as np

# Generate some random data for the charts
data1 = np.random.randint(1, 10, size=5)
data2 = np.random.randint(2, 10, size=5)

# Set the width of each bar
bar_width = 0.30

# Calculate the x positions for the bars
x_pos = np.arange(len(data1))

# Create the first bar chart
plt.bar(x_pos, data1, bar_width, color='b', label='Data 1')

# Calculate the x positions for the second set of bars
x_pos2 = x_pos + bar_width

# Create the second bar chart
plt.bar(x_pos2, data2, bar_width, color='g', label='Data 2')

# Add axis labels and a title
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Multiple Bar Charts Example')

# Add a legend
plt.legend()

# Show the chart
plt.show()