def linear_seach(data, search_value):
    for i in data:
        if i == search_value:
            return True
 
    return False

data = [-1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 6, 7, 7, 8, 9, 12, 14, 14, 24, 24, 24, 24, 35, 41, 43, 43, 45, 52, 54, 124, 124, 214, 323, 342, 412, 412, 421, 424, 1341, 4452]
print('is 1000 in data {} '.format(linear_seach(data, 1000)))
print('is -1 in data {} '.format(linear_seach(data, -1)))