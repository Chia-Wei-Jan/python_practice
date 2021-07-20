import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 15, 0.5)
y = np.sin(x)

# plt.plot(x, y, 'r-.')
plt.plot(x, y, color='lime', linestyle='-.', linewidth=2,
         marker='o', markerfacecolor='white', markeredgecolor='blue', markersize=4, markeredgewidth=1,
         label='First', zorder=2)
# plt.scatter(x, y)
plt.plot(x+2, y, label='Second', zorder=1)

axis1 = plt.gca()
axis1.set_title('Practice', fontname='Arial', fontsize=20, weight='bold', style='italic')
axis1.set_xlabel('x')
axis1.set_ylabel('sin(x)')
plt.legend(loc='best')
plt.show()

fig, ax = plt.subplots(2,1)
ax[0].plot(x, y)
ax[1].plot(x+2, y, 'b')
plt.show()