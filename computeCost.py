# import numpy as np
def hypo(x, t0, t1):
	hyp = t1 * x + t0
	return hyp
def computeCost(X, Y, t0, t1, m):
	grad0 = 0
	grad1 = 0
	for i in range(1, m):
		grad0 = grad0 + hypo(X[i], t0, t1) - Y[i]
		grad1 = grad1 + (hypo(X[i], t0, t1) - Y[i]) * X[i]
	J = ((grad0 ** 2) / (2 * m))
	return grad0 / m, grad1 / m, J
