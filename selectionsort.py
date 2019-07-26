import time
def findmaxsubarr(arr,i,n):
	max_idx=0
	max_ele=0

	for idx  in range(i,n):
		if arr[idx]>max_ele:
			max_ele = arr[idx]
			max_idx = idx

	return max_idx


def selectionsort(arr):
	n= len(arr)
	sortedindex=0
	for i in range(0,n):
		idx=findmaxsubarr(arr,i,n)
		arr[sortedindex],arr[idx]=arr[idx],arr[sortedindex]
		sortedindex+=1

	return arr

def main(): 


	arr = [12,13,41,53,52,18,15,75,19,2]
	start = time.time()
	arr = selectionsort(arr)
	end = time.time()
	print("time taken for selection sort is", end-start)
	for i in arr:
		print(i)
	
	arr = [12,13,41,53,52,18,15,75,19,2]
	start=time.time()
	arr.sort()
	end=time.time()
	print("time taken for inbuilt sort is" , end-start)

main()	

	
