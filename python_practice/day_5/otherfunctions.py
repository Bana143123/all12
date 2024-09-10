#Histogram
import numpy as np

data=np.random.randn(5)
hist,binpoints=np.histogram(data,bins=10)
print("Histogram :",hist)
print("Bin points:",binpoints)
#For better visualization using matplotlib
import matplotlib
matplotlib.use("Agg")# Use the Agg backend for headless environments
import matplotlib.pyplot as plt
plt.hist(data,bins=10,edgecolor="black")
plt.title("Histogram visualization")
plt.xlabel("Value")
plt.ylabel("Frequency")
# Save the plot to a file
plt.savefig('histogram.png')
print("Histogram saved to 'histogram.png'")
plt.show()



