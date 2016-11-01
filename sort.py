from time import time
from random import randint
# Bubble Sort
def Bubble_sort(t):
	check_length = len(t) - 1
	flag = 1
	while flag:
		flag = 0
		for i in range(check_length):
			if t[i] > t[i+1]:
				t[i], t[i+1] = t[i+1], t[i]
				check_length = i
				flag = 1
	return t

# Insertion Sort
def Insertion_sort(t):
	length = len(t)
	for i in range(1, length):
		for j in range(i, 0, -1):
			if t[j] < t[j-1]:
				t[j], t[j-1] = t[j-1], t[j]
			else:
				break
	return t

# Shell Sort
def Shell_sort(t):
	length = len(t)
	gap = length
	while gap > 1:
		gap //= 2
		for i in range(gap, length):
			for j in range(i, 0, -gap):
				if t[j] < t[j-gap]:
					t[j], t[j-gap] = t[j-gap], t[j]
				else:
					break
	return t

# Selection Sort
def Selection_sort(t):
	length = len(t)
	for i in range(length):
		min_pos = i
		for j in range(i+1, length):
			if t[j] < t[min_pos]:
				min_pos = j
		t[i], t[min_pos] = t[min_pos], t[i]

	return t

# Merge Sort
def Merge_sort():
	pass


if __name__ == '__main__':
	a = [7, 8, 5, 1, 9, 2, 4, 6, 3, 10]
	for i in range(10000):
		a.append(randint(1, 10000))
	print('Data ready')

	start = time()
	p = Bubble_sort(a)
	print(time()-start)