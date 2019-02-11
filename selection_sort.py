import sys

data = [4,9,7,1,3,6,2,3,323,43,43,54,3,2,342,35,4452,1341,24,2,41,4,14,1,412,412,421,424,24,214,124,24,24,14,124,12,45,5,8,7,4,52,-1]
tmp_value,tmp_index = 0,0

def get_min(data):
    min_index = 0
    for i in range(1,len(data)):
        if data[min_index] < data[i]:
            min_index= i
    
    return min_index

for i in range(len(data)):
    tmp = get_min(data[i:])
    data[i],data[tmp+i] = data[tmp+i],data[i]

print('data: {} index: {} list: {}'.format(get_min(data), data[get_min(data)],data))


