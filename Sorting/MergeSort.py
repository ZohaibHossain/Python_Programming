import math

def DisplayResults(A,a,b):
	print("List", end=" ")
	for i in range(a,b+1):
		print("%d" %A[i], end=" ")
	print(" ")

def MergeSort(A,p,r):
	if p<r:
		q=math.floor((p+r)/2)
		MergeSort(A,p,q)
		MergeSort(A,q+1,r)
		Merge(A,p,q,r)

def Merge(A,p,q,r):
	L=[]
	R=[]
	n1=q-p+1	#Length of Left Array
	n2=r-q		#Length of Right Array

	# Insertion of vaues in left & right array
	for i in range(n1):
		L.append(A[p+i])
	for j in range(n2):
		R.append(A[q+j+1])
	
	i=0
	j=0
	L.append(-99) # Sentinel Value
	R.append(-99) # Sentinel Value

	# Merging of values
	for k in range(p,r+1):
		if (R[j] == -99 and L[i] != -99):
			A[k] = L[i]
			i += 1
		elif (L[i] == -99 and R[j] != -99):
			A[k] = R[j]
			j += 1
		elif (L[i] <= R[j]):
			A[k] = L[i]
			i += 1
		elif (L[i] > R[j]):
			A[k] = R[j]
			j += 1

arr=[50,30,15,10,25,34,16,12,45]
DisplayResults(arr,0,len(arr)-1)
MergeSort(arr,0,len(arr)-1)
DisplayResults(arr,0,len(arr)-1)

