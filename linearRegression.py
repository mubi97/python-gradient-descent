from readData import readData
import numpy as np
X, Y = readData()
m = len(X)
t0 = 0
t1 = 0
alpha = .01
iter = 9
from gradientDescent import gradientDescent
t0,t1 = gradientDescent(X, Y, t0, t1, alpha, iter, m)
print t0, t1