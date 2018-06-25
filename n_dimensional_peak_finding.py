# problem statement: find a peak if it exists. (Only one peak)

# definition of a peak: a[i] is a peak iff a[i] >= a[i+1] and a[i] >= a[i-1]
	
def one_d_peak_finder(a):
	n = len(a)

	if n == 0:
		return -1

	elif n == 1:
		return a[0]

	elif n == 2:
		if a[0] > a[1]:
			return a[0]
		else:
			return a[1]

	else:
		if a[n/2] < a[(n/2) - 1]:
			a = a[:n/2]
			return(one_d_peak_finder(a))

		elif a[n/2] < a[(n/2) + 1]:
			a = a[n/2:]
			return(one_d_peak_finder(a))

		else:
			return a[n/2]

''' definition of a peak: 
a[i,j] is a peak iff a[i,j] >= a[i+1,j], a[i,j] >= a[i-1,j], a[i,j] >= a[i,j+1] and a[i,j] >= a[i,j-1]
'''

def two_d_peak_finder(a):
	rows = len(a)
	cols = len(a[0])

	if rows == 0 or cols == 0:
		return -1

	elif rows == 1 and cols == 1:
		return a[0][0]

	elif rows == 1 and cols > 1:
		return one_d_peak_finder(a[0])

	elif rows > 1 and cols == 1:
		return one_d_peak_finder(a)

	elif rows >= 2 and cols == 2:
		print(a)
		m = one_d_peak_finder(a[:][0])
		print(a[0])
		print(m)
		
		n = one_d_peak_finder(a[:][1])
		print(a[1])
		print(n)
		
		if m > n:
			return m
		else:
			return n

	elif rows == 2 and cols >= 2:
		m = one_d_peak_finder(a[0][:])
		n = one_d_peak_finder(a[1][:])
		if m > n:
			return m
		else:
			return n

	else:
		index = 0
		temp = a[0][cols/2]
		for i in range(rows - 1):
			if temp < a[i+1][cols/2]:
				temp = a[i+1][cols/2]
				index = i+1

		if a[index][cols/2] < a[index][(cols/2) + 1]:
			a = a[:][cols/2:]
			return(two_d_peak_finder(a))

		elif a[index][cols/2] < a[index][(cols/2) - 1]:
			a = a[:][:cols/2]
			return(two_d_peak_finder(a))

		else:
			return a[index][cols/2]

def test():
	a = [[1,2,3,4,5,2,1],
	     [2,3,4,5,7,3,2],
	     [0,3,2,3,6,7,4],
	     [1,2,3,2,4,8,6],
	     [0,1,2,3,5,7,5]]

	b = [[1,2,3,4,3,2,1],
	     [2,3,4,5,4,3,2],
	     [1,2,3,4,3,2,1],
	     [0,1,2,3,2,1,0],
	     [0,0,1,2,1,0,0]]

	c = [[1,2,3,4,3,2,1],
	     [2,3,4,5,4,3,2]]

	d = [[1,2],
	     [2,3],
	     [3,4],
	     [4,5]]

	e = [[1,2,3,4],
	     [2,3,4,5]]

	print(two_d_peak_finder(d))
	'''
	a = []
	c = [1]
	d = [1,2]
	e = [1,2,3,4,5]
	peaks = []

	f = [a,b,c,d,e]
	
	for i in f:
		print(i)
		peaks.append(one_d_peak_finder(i))

	print(peaks) 
	'''

if __name__ == '__main__':
	test()