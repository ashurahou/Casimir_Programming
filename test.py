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
    theta = np.linspace(0,2*np.pi,100)
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    fig = plt.plot(x,y)
    #plt.show()
    plt.savefig('circle.png')
#    return

	

