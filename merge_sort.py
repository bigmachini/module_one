def merge(left, right):
    i,j,res = 0,0,[]
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i = i+1
        else:
            res.append(right[j])
            j = j + 1

    if i < len(left):
        res += left[i:]
    
    if j < len(right):
        res += right[j:]

    return res
 
def merge_sort(lst):
    n = int(len(lst) / 2)
    left = lst[:n]
    right = lst[n:]
   
    if len(left) == 1 or len(right) ==  1 :
        return merge(left, right)

    left = merge_sort(left)
    right = merge_sort(right)
    
    #merge
    return merge(left, right)


data = [4,9,7,6,5,3,1]
print('unsorted: {}'.format(data))

print('sorted: {}'.format(merge_sort(data)))