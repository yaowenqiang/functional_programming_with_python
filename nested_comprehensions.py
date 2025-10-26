binary_matrix = [
        [1,0,0,1],
        [0,0,0,1],
        [1,1,1,1],
        [1,0,0,0],
        ]

true_false_matrix = []
#for row in binary_matrix:
    #new_row = []
    #for item in row:
    #    new_row.append(bool(item))
    #new_row = [bool(item) for item in row]
#    true_false_matrix.append([bool(item) for item in row])

true_false_matrix = [[bool(item) for item in row] for row in binary_matrix]

print(true_false_matrix)
