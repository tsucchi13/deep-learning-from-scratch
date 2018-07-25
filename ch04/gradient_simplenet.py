import sys, os
sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import numpy as np
from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient


class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3)#正規分布で-1～1の値をランダムに出力．2×3の行列

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        # print('出力：')
        # print(y)
        loss = cross_entropy_error(y, t)

        return loss
#正解ラベル
t = np.array([0, 0, 1])

x = np.array([0.6, 0.9])
print('入力：')
print(x)

net = simpleNet()#インスタンス化．コンストラクタだけ実行されWという重みパラメータがインスタンス変数として格納される
print('重みパラメータ：')
print(net.W)

dst = net.predict(x)
print('出力=入力・重み：')
print(dst)

soft = softmax(dst)
print('ソフトマックス層の後の出力=確率：')
print(soft)

print('正解ラベル')
print(t)

loss = net.loss(x, t)
print('損失関数(出力と正解ラベルの差分)：')
print(loss)

f = lambda w: net.loss(x, t)#lambda 引数: 返り値で簡易的に関数作れる
dW = numerical_gradient(f, net.W)#損失関数fを重みwで微分

print('勾配=損失関数を重みの各要素で偏微分：')
print(dW)
