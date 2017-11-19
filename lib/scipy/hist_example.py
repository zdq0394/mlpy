import numpy
from numpy.random import normal
import matplotlib.pyplot as plt

def matlab_hist(v):
    plt.hist(v, bins=50, normed=False)
    plt.show()

def numpy_hist(v):
    (n,bins) = numpy.histogram(v, bins=50, normed=False)
    plt.plot(.5*(bins[1:]+bins[:-1]), n)
    plt.show()

if __name__ == "__main__":
    mu, sigma = 100, 0.5
    v = normal(mu, sigma, 10000)
    matlab_hist(v)
    numpy_hist(v)