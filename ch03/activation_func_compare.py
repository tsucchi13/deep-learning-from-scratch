import numpy as np
import matplotlib.pylab as plt

def step_function(x):#引数はNumpy配列で返り値も
    #x > 0 の部分で配列の各要素の不等号演算結果のboolが返ってくる
    #dtype=np.int でtrue/falseで返ってきたのを0と1に直してる
    return np.array(x > 0, dtype=np.int)
#これを書き換えると
# def step_function2(x):
#     y = x > 0
#     return y.astype(np.int)

#Numpy配列を引数として受け取っても，ブロードキャストによりそのまま演算できるからシンプル
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0,x)

def identity_function(x):
    return x

def softmax(x):
    c = np.max(x)
    exp_x = np.exp(x - c)
    sum_exp_x = np.sum(exp_x)
    y = exp_x / sum_exp_x
    # print(np.sum(y))
    return y

x = np.arange(-5.0, 5.0, 0.1)
y1 = step_function(x)
y2 = sigmoid(x)
y3 = relu(x)
y4 = identity_function(x)
y5 = softmax(x)

plt.plot(x, y1, label = 'step')
plt.plot(x, y2, '--', label = 'sigmoid')
plt.plot(x, y3, '-.', label = 'ReLU')
plt.plot(x, y4, label = 'identity')
plt.plot(x, y5, label = 'softmax')
plt.legend()
plt.ylim(-0.1, 1.1) #図で描画するy軸の範囲を指定
plt.show()
