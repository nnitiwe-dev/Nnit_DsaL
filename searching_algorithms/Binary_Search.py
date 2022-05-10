#Recursive Binary Search Tree

def Binary_Search(ArrayL,low,high,target):
	mid=low+(high-low)//2

	if low<=high:
		if target==ArrayL[mid]:
			#return index of mid
			return mid 
		elif target<ArrayL[mid]:
			return Binary_Search(ArrayL,low,mid-1,target)
		elif target>ArrayL[mid]:
			return Binary_Search(ArrayL,low,mid+1,target)
	else:
		#didnt find item
		return -1