import time
import matplotlib.pyplot as plt
import numpy as np


#nterms = random.randint(1,100)
#nterms = nterms = int(input("How many terms? "))
a = 10
b = 15
c = 20
d = 30

x = []
y = []

print("Fibonacci sequence:\n")

def iter_fibo1():
	n1, n2 = 0, 1
	count = 0
	print('\n 10 terms:')
	while count < a:
	    print(n1)
	    nth = n1 + n2
	    n1 = n2
	    n2 = nth
	    count += 1

def iter_fibo2():
	n1, n2 = 0, 1
	count = 0
	print('\n 15 terms:')
	while count < b:
	    print(n1)
	    nth = n1 + n2
	    n1 = n2
	    n2 = nth
	    count += 1

def iter_fibo3():
	n1, n2 = 0, 1
	count = 0
	print('\n 20 terms:')
	while count < c:
	    print(n1)
	    nth = n1 + n2
	    n1 = n2
	    n2 = nth
	    count += 1

def iter_fibo4():
	n1, n2 = 0, 1
	count = 0
	print('\n 30 terms:')
	while count < d:
	    print(n1)
	    nth = n1 + n2
	    n1 = n2
	    n2 = nth
	    count += 1

def Runtime():
	start1 = time.time()
	iter_fibo1()
	stop1 = time.time()
	runtime1 = stop1 - start1
	print("Runtime:", runtime1)
	x.append(a)
	y.append(runtime1)

	start2 = time.time()
	iter_fibo2()
	stop2 = time.time()
	runtime2 = stop2 - start2
	print("Runtime:", runtime2)
	x.append(b)
	y.append(runtime2)

	start3 = time.time()
	iter_fibo3()
	stop3 = time.time()
	runtime3 = stop3 - start3
	print("Runtime:", runtime3)
	x.append(c)
	y.append(runtime3)

	start4 = time.time()
	iter_fibo4()
	stop4 = time.time()
	runtime4 = stop4 - start4
	print("Runtime:", runtime4)
	x.append(d)
	y.append(runtime4)

	print(x)
	print(y)

with open('filee.txt', 'w') as f:
    for item in y:
        f.write("%s\n" % item)

Runtime()
plt.plot(x,y, label = 'linear')
plt.xlabel('Terms')
plt.ylabel('Runtime')
plt.axis([0, 30, 0, 0.01])
plt.title("Fibonacci")
plt.legend()
plt.show()