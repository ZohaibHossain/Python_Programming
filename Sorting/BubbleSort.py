def DisplayResult(A):
	print("List:", end=" ")
	for i in range(len(A)):
		print ("%d" %A[i], end=" ")
	print("")

def BubbleSort(A):
	for i in range(len(A)):
		for j in range(i,len(A)):
			if (A[j] < A[j-1]):
				temp=A[j]
				A[j]=A[j-1]
				A[j-1]=temp

arr=[50, 30, 10, 25, 90, 88, 44]
DisplayResult(arr)
BubbleSort(arr)
DisplayResult(arr)
