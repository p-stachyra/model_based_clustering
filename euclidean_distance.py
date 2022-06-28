import numpy as np

def main():

	point1 = np.array((1,2,3))
	point2 = np.array((1,1,1))

	print(euclideanLinalg(point1, point2))
	print(l2_dist(point1, point2))
	print(euclideanDot(point1, point2))

def euclideanLinalg(x, y):
	"""Calculate the Euclidean distance using NumPy's linalg class method norm().  
	"""
	distance = np.linalg.norm(x - y)
	return distance

def l2_dist(x, y):
	"""Calculate the Euclidean distance by calculating the square root of sum of squared pairwise differences between vectors' elements.
	"""
	return np.sqrt(sum((x - y) ** 2))

def euclideanDot(x, y):
	difference = x - y
	return np.sqrt(np.dot(difference.T, difference))




if __name__ == "__main__":
	main()