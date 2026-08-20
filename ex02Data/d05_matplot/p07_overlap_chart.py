import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')
plt.rcParams['figure.figsize'] = (6,5)
plt.rcParams['font.size'] = 12

x = np.arange(2020, 2027) #2020~2026
# print(x)
y1 = np.array([1,3,7,5,9,7,14])
y2 = np.array([1,3,5,7,9,11,13])

fig, ax1 = plt.subplots()
ax1.plot(x, y1, '-s', color='green', markersize=7,
         linewidth=5, alpha=0.7, label='Price')
ax1.set_ylim(0,18)
ax1.set_xlabel('Year')
ax1.set_ylabel('Price ($)')
ax1.tick_params(axis='both', direction='in')
ax1.legend(loc='upper right')

ax2 = ax1.twinx()
ax2.bar(x, y2, color='deeppink', label="Demand", alpha=0.7, width=0.7)
ax2.set_ylim(0,18)
ax2.set_ylabel(r'Demand ($\times10^6$)')
ax2.tick_params(axis='y', direction='in')
ax2.legend(loc='upper left')

for i in range(0, len(y2)):
  plt.text(x=x[i]-0.2, y=y2[i]-1,
           s=y2[i],
           color='white')
  plt.text(x=x[i] - 0.2, y=y1[i] + 1,
           s=y1[i],
           color='green')
plt.show()