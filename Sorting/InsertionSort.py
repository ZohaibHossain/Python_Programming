def InsertionSort(A):
	for i in range(1,len(A)):
		key=A[i]
		j=i-1
		while(j>=0 and key<A[j]):
			A[j+1]=A[j]
			j -= 1
		A[j+1]=key

def DisplayResult(A):
	print("List:", end=" ")
	for i in range(len(A)):
		print("%d" %A[i], end=" ")
	print(" ")

arr=[3,4,5,1,2]
DisplayResult(arr)
InsertionSort(arr)
DisplayResult(arr)
