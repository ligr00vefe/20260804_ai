import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [100, 200, 300, 400, 500]

plt.bar(x, y)
# 좌표 (x축 = v, y축 = y[0]..y[1], 표시 = y[0]..y[1])
for i, v in enumerate(x):
  plt.text(v, y[i], y[i],
           fontsize=9,
           color='blue',
           horizontalalignment='center',  # horizontalalignment (left, center, right)
           verticalalignment='bottom')  # verticalalignment (top, center, bottom)

plt.show()