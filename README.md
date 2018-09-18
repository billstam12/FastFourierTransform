# FastFourierTransform
FFT implementation in python *(and almost node-js)*
##A quick implementation of the fourier transform

Given a sinusoid composed of many frequencies 

```python

freqs =   [2, 5, 11, 17, 29]

# For some reason iterating through " wasn't working so I manually added them :p
x = [0 for x in xrange(0,num_samples)]
for i in xrange(0, num_samples):
	x[i] =  np.sin(2*np.pi*freqs[0]*i/num_samples) + np.sin(2*np.pi*freqs[1]*i/num_samples) + np.sin(2*np.pi*freqs[2]*i/num_samples) + np.sin(2*np.pi*freqs[3]*i/num_samples) + np.sin(2*np.pi*freqs[4]*i/num_samples)
	x[i] = np.complex(x[i],0)
```

I calculated the Fourier Transformed wave based on teh Cooley Tuckey FFT algorithm
```python
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
```
The result for sinusoids with frequencies 2,5,7,11,17,29 is the following
![logo](https://i.imgur.com/vzJ8wnT.png)

TbA
Giving sinusoids by the user and better graphic representation.
