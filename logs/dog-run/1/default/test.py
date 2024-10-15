import matplotlib.pyplot as plt
import numpy as np

# 生成数据
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# 绘制图表
plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Sine Wave')
plt.grid(True)
plt.savefig('sine_wave.png')  # 保存图表为文件
print("图表已保存为 sine_wave.png。")