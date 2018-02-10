# import numpy as np
from matplotlib import pyplot as plt
from computeCost import computeCost
def gradientDescent(X, Y, t0, t1, alpha, iter, m):

	J = []
	jtem = 0
	for i in range(iter):
		grad0, grad1, jtem = computeCost(X, Y, t0, t1, m)
		t0 = t0 - alpha * grad0
		t1 = t1 - alpha * grad1
		J.append(jtem)
		x_values = [i for i in range(int(min(X))-1, int(max(X))+2)]
		j_values = [(t1 * x + t1) for x in x_values]
		plt.plot(X, Y, 'ro')
		plt.plot(j_values, x_values, 'b')
		plt.show()
	print J
	return t0,t1