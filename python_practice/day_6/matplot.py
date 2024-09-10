import matplotlib.pyplot as plt
import numpy as np



sp=np.linspace(0,10,20)
y=np.sin(sp)
plt.plot(sp,y)
plt.title("Sine Wave")
plt.xlabel("X AXIS")
plt.ylabel("Y AXIS")
plt.show()