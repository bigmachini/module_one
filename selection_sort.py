import sys

data = [4,9,7,1,3,6,2,3,323,43,43,54,3,2,342,35,4452,1341,24,2,41,4,14,1,412,412,421,424,24,214,124,24,24,14,124,12,45,5,8,7,4,52,-1]
def selection_sort(lst):
    lst_len = len(lst)
    for i in range(lst_len):
        smallest,index = lst[i], i
        for j in range(i, lst_len):
            if lst[j] < smallest:
                smallest = lst[j]
                index = j
        lst[index], lst[i], =  lst[i], smallest

selection_sort(data)
print('sorted data: {} '.format(data))
