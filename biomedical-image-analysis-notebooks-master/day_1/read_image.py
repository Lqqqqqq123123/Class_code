import math
import numpy as np
import matplotlib.pyplot as plt
from skimage import io

# 读取图像
img = io.imread("../images/nuclei-dapi.tif")

# 显示图像
plt.imshow(img, cmap='gray')  # 使用 cmap='gray' 将图像显示为灰度
plt.show()

# 打印图像的类型和形状
print(type(img))
print(img.shape)