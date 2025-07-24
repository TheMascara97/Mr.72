import matplotlib.pyplot as plt  
import numpy as np  
from matplotlib.font_manager import FontProperties  


font = FontProperties(fname='C:\\Users\\Administrator\\AppData\\Local\\Microsoft\\Windows\\Fonts\\SourceHanSansCN-Normal.otf', size=14)
# 准备数据  
data = {  
    '运营商': ['N41(移动)', 'N41(移动)', 'N41(移动)', 'N41(广电)', 'N41(广电)', 'N41(广电)', 'N78(电信)', 'N78(电信)', 'N78(电信)', 'N78(联通)', 'N78(联通)', 'N78(联通)'],  
    '测试场景': ['2.4G-WIFI', '5G-WIFI', 'LAN', '2.4G-WIFI', '5G-WIFI', 'LAN', '2.4G-WIFI', '5G-WIFI', 'LAN', '2.4G-WIFI', '5G-WIFI', 'LAN'],  
    '上传(Mbps)': [58, 53, 51, 53, 64, 54, 81, 98, 97, 79, 78, 77],  
    '下载(Mbps)': [102, 354, 338, 104, 291, 330, 104, 400, 808, 112, 306, 328]  
}  
  
# 设置图表大小  
plt.figure(figsize=(12, 8))  
  
# 设置柱状图的位置和宽度  
bar_width = 0.2  
index = np.arange(len(data['运营商']))  # 生成0到11的索引  
  
# 为每个测试场景分配颜色  
colors = {'2.4G-WIFI': 'b', '5G-WIFI': 'g', 'LAN': 'r'}  
  
# 绘制上传速度柱状图  
for i in range(len(data['运营商'])):  
    plt.bar(index[i], data['上传(Mbps)'][i], bar_width, label='上传(Mbps)' if i == 0 else '', color=colors[data['测试场景'][i]])  
  
# 绘制下载速度柱状图，使用不同的颜色  
for i in range(len(data['运营商'])):  
    plt.bar(index[i] + bar_width, data['下载(Mbps)'][i], bar_width, label='下载(Mbps)' if i == 0 else '', color=colors[data['测试场景'][i]])  
  
# 添加标题和标签，使用中文字体  
plt.title('不同运营商、场景下的网络速度测试', fontproperties=font)  
plt.xlabel('运营商', fontproperties=font)  
plt.ylabel('速度 (Mbps)', fontproperties=font)  
plt.xticks(index + bar_width / 2, data['运营商'], rotation=45, fontproperties=font)  
plt.legend(prop=font)  
plt.grid(True)  
  
# 保存图表  
plt.tight_layout()  
plt.savefig('network_speed_test_bar_chart_colored_fixed.png')