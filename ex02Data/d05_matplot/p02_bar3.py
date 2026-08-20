import matplotlib.pyplot as plt
import numpy as np

years = ['2018', '2019', '2020']
values = [100, 400, 900]
colors = ['y', 'dodgerblue', 'C2']

# x = np.arange(3)
# plt.bar(x, values, color=colors, width=0.8,
#         align='edge', edgecolor='#eee',
#         linewidth=5)
# plt.xticks(x, years)

y = np.arange(3)
plt.barh(y, values, color=colors, height=0.8,
         align='edge', edgecolor='#eee',
         linewidth=5)
plt.yticks(y, years)

plt.show()