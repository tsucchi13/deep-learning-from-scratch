import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

def drawGraph():
    # データの作成
    x = np.arange(0, 6, 0.1) # 0から6まで0.1刻みで生成
    y1 = np.sin(x)
    y2 = np.cos(x)

    # グラフの描画
    plt.plot(x, y1, label="sin")
    plt.plot(x, y2, linestyle = "--", label="cos")
    plt.xlabel("x") # x軸のラベル
    plt.ylabel("y") # y軸のラベル
    plt.title('sin & cos')
    plt.legend() #凡例
    plt.show()

def showImage():
    img = imread('lena.jpg') # 画像の読み込み
    plt.imshow(img)

    plt.show()

drawGraph()
showImage()
