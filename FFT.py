import numpy as np 
import matplotlib.pyplot as plt 
import random

def fft(x):
	fft_rec(x)
	return x


def fft_rec(X):
	N = len(X)
	if N <= 1:
		return

	even = np.array(X[0:N:2])
	odd = np.array(X[1:N:2])

	fft_rec(even)
	fft_rec(odd)

	for k in xrange(0, N/2):
		w = np.exp(np.complex(0, -2*np.pi*k/N))*odd[k]
		X[k] = even[k] + w
		X[k+ N/2] = even[k] -w



num_samples = 256
n_sec = 1.0
sample_rate = num_samples/n_sec
freq_res = sample_rate/ num_samples

freqs =   [2, 5, 11, 17, 29]

# For some reason iterating through freqs wasn't working so I manually added them :p
x = [0 for x in xrange(0,num_samples)]
for i in xrange(0, num_samples):
	x[i] =  np.sin(2*np.pi*freqs[0]*i/num_samples) + np.sin(2*np.pi*freqs[1]*i/num_samples) + np.sin(2*np.pi*freqs[2]*i/num_samples) + np.sin(2*np.pi*freqs[3]*i/num_samples) + np.sin(2*np.pi*freqs[4]*i/num_samples)
	x[i] = np.complex(x[i],0)


_, plots = plt.subplots(3)
plt.xlabel('Frequencies')
plots[0].plot(x)


X = fft(x)
plots[1].plot(X)
amps = np.abs(np.divide(X, num_samples/2))
frequencies = np.divide(np.multiply(sample_rate, np.arange(0,num_samples/int(np.log2(num_samples)))),num_samples)
plots[2].plot(frequencies, amps[:num_samples/int(np.log2(num_samples))])

plt.show()
