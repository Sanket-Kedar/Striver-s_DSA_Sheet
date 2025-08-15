#reverse an array

def rev_array(arr,start,end):
    if start>=end:
        return
    arr[start],arr[end] = arr[end],arr[start]
    return rev_array(arr,start+1,end-1)

arr = [21,27,3,4]
rev_array(arr,0,len(arr)-1)
print(arr)