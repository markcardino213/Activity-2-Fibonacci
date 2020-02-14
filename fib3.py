import random
import matplotlib.pyplot as plt
import numpy as np
import time

#nterms = random.randint(1,100)
n1 = 10
n2 = 15
n3 = 20
n4 = 30

x = []
y = []

def fibonacci(n):
	if n < 0:
		raise ValueError("Negative arguments not implemented")
	return _fib(n)[0]

def _fib(n):
	if n == 0:
		return (0, 1)
	else:
		a, b = _fib(n // 2)
		c = a * (b * 2 - a)
		d = a * a + b * b
		if n % 2 == 0:
			return (c, d)
		else:
			return (d, c + d)

def term1():
	for i in range(n1):
		print(_fib(i))

def term2():
	for i in range(n2):
		print(_fib(i))

def term3():
	for i in range(n3):
		print(_fib(i))

def term4():
	for i in range(n4):
		print(_fib(i))

def Runtime():
	start1 = time.time()
	#recur_fibo(n1)
	term1()
	stop1 = time.time()
	runtime1 = stop1 - start1
	print("Runtime:", runtime1)
	x.append(n1)
	y.append(runtime1)

	start2 = time.time()
	#recur_fibo(n2)
	term2()
	stop2 = time.time()
	runtime2 = stop2- start2
	print("Runtime:", runtime2)
	x.append(n2)
	y.append(runtime2)

	start3 = time.time()
	#recur_fibo(n3)
	term3()
	stop3 = time.time()
	runtime3 = stop3 - start3
	print("Runtime:", runtime3)
	x.append(n3)
	y.append(runtime3)

	start4 = time.time()
	#recur_fibo(n4)
	term4()
	stop4 = time.time()
	runtime4 = stop4 - start4
	print("Runtime:", runtime4)
	x.append(n4)
	y.append(runtime4)

	print(x)
	print(y)

Runtime()
plt.plot(x,y, label = 'linear')
plt.xlabel('Terms')
plt.ylabel('Runtime')
plt.axis([0, 30, 0, 0.01])
plt.title("Fibonacci")
plt.legend()
plt.show()