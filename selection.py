A = [64, 25, 12, 22, 11]
  
# # Traverse through all array elements
# for i in range(len(A)):
      
#     # Find the minimum element in remaining 
#     # unsorted array
#     min_idx = i
#     for j in range(i+1, len(A)):
#         if A[min_idx] > A[j]:
#             min_idx = j
              
#     # Swap the found minimum element with 
#     # the first element        
#     A[i], A[min_idx] = A[min_idx], A[i]
  
# # Driver code to test above
# print ("Sorted array")
# for i in range(len(A)):
#     print("%d" %A[i])
def binary(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]< key:
            low =mid+1
        else:
            high=mid-1
    return -1
print(binary(sorted(A),13))