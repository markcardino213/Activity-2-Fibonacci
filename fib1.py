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

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))


print("Fibonacci sequence:\n")

def term1():
	print('\n10 terms:')
	for i in range(n1):
	    print(recur_fibo(i))

def term2():
	print('\n15 terms:')
	for i in range(n2):
	    print(recur_fibo(i))

def term3():
	print('\n20 terms:')
	for i in range(n3):
	    print(recur_fibo(i))

def term4():
	print('\n30 terms:')
	for i in range(n4):
	    print(recur_fibo(i))


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