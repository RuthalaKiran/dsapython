
def findsuperior(arr):
    n = len(arr)
    ele = 0
    count = 0
    i = 0 
    for j in range(i+1,n):
        if arr[i] > arr[j]:
            count = 1
        if count == 1:
            ele = ele + 1
            count = 0
    return ele
            
            
def findsuperior1(arr):
    n = len(arr)
    count =0
    sup = float('-inf')
    for i in range(n-1,-1,-1):
        if arr[i] > sup :
            count += 1
            sup = arr[i]
    return count
            
            

arr = [8,10,6,2,9,7]
print(findsuperior1(arr))   
     