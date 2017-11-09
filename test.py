import numpy as np

import matplotlib.pyplot as plt


print('Hello World')

print('Hello Heaven')

def circcir(r):
	return np.pi*2*r

# print('Circumference of circle with radius 5 is',circcir(5)) # This is not useful here

print('Circumference of circle with radius 5 is',circcir(5))


'''
def surarea(r):
	return np.pi*r**2
'''
# print('Surface area of the cirlce with radius 5 is', surarea(5)) # This is not useful here

def circplot(x0,y0,r):
	"""
	(x0,y0) is the center of the circle
	r is the radius of the circle
	"""
	x = np.linspace(-1,1,100)
	y = y0+ np.sqrt(r**2-(x-x0)**2)
	plt.plot(x,y)
	plt.savefig('circle.png',format='png')
	return

	

