import matplotlib.pyplot as plt

ratio = [34, 32, 16, 18]
labels = ['Apple', 'Banana', 'Melon', 'Grapes']
colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
explode = [0.3, 0.05, 0.05, 0.05]
wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}

plt.pie(ratio, labels=labels, autopct='%.1f%%',
        counterclock=False, startangle=90,
        colors=colors, explode=explode,
        # shadow=True,
        wedgeprops=wedgeprops)
font1 = {
  'family': 'Times New Roman','color': 'blue','weight': 'bold',
  'size': 14,'alpha': 0.7}
plt.text(-0.2, -0.2, 'Fruits', fontdict=font1, rotation=30)
plt.savefig('../source/pie_chart.png')
plt.show()