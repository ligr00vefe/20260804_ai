import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0. , 5., 0.2)
# plt.plot(t, t,'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()


xdata = [ '1st', '2st', '3rd', '4th', '5th']
y1data = [90,82,75,58,78]
y2data = [80,80,50,40,90]
y3data = [-40,50,90,90,60]
# plt.plot(xdata, y1data,'r-o',
#          xdata, y2data, 'g:x',
#          xdata, y3data, 'b--p');plt.show()

plt.rcParams['font.family'] = 'Malgun Gothic'
# minus 기호가 한글로 지정하면 깨지기 때문에 다시 지정
plt.rcParams['axes.unicode_minus'] = False

# font 다운받은 걸로 사용하려고 할 때
import matplotlib.font_manager as fm
font_path = 'C:\\Windows\\Fonts\\HANBatang.ttf'
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

# plt.title('다중 Line 챠트')
plt.title('다중 Line 챠트', loc='right', pad=20)
plt.plot(xdata, y1data,'r-o', label='Foo')
plt.plot(xdata, y2data, 'g:x', label='진자바')
plt.plot(xdata, y3data, 'b--p', label='Kim')
# loc :: x축 left, center, right
# loc :: y축 bottom, center, top
plt.xlabel('회차', labelpad= 15, loc='right'
           , fontdict={'family':'Malgun Gothic', 'color':'#0000FF', 'size':14})
plt.ylabel('Score', labelpad=20, loc='top'
           , fontdict={'family':'Malgun Gothic', 'color':'deeppink'
           , 'weight':'bold','size':'xx-large'})
# plt.axis([0,6,0,100]) # x1, x2, y1, y2
plt.xlim(0,7)
plt.ylim(0, 100)
# 'on','off','equal','scaled','tight','auto','normal','image','square'
plt.axis('on')
plt.legend(loc='upper right')
x_range, y_range = plt.xlim(), plt.ylim()
print(x_range, y_range)
axis_range = plt.axis('on')
print(axis_range)
plt.show()