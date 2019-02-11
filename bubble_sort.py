def bubble_sort(data):
    size = len(data)
    swap = False
    for i in range(size-1):
        if data[i] > data[i+1]:
            swap = True
            data[i],data[i+1] = data[i+1],data[i]
    while swap:
        swap = False
        for i in range(size-1):
            if data[i] > data[i+1]:
                swap = True
                data[i],data[i+1] = data[i+1],data[i]


def bubble_sort_two(data):
    list_size = len(data)
    for i in range(list_size,0, -1):
        for j in range(i-1):
            if data[j] < data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]



data = [4,9,7,1,3,6,2,3,323,43,43,54,3,2,342,35,4452,1341,24,2,41,4,14,1,412,412,421,424,24,214,124,24,24,14,124,12,45,5,8,7,4,52,-1]
bubble_sort_two(data)
print('bubble sort: {}'.format(data))