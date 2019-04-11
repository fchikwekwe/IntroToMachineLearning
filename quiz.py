matrix = [
    [1000, 53],
    [2343, 34],
    [432432, 32],
    [489320, 43],
    [4334, 32],
    [43, 64]
]

def normalize(matrix):
    num_cols = len(matrix[0])
    col = 0 # keep track of current column
    col_sums = []

    max = None # keep track of max value
    min = None # keep track of min value

    while col < num_cols:
        total = 0
        for item in matrix:
            total += item[col]
            if max is None:
                max = item[col]
            if min is None:
                min = item[col]
        col_sums.append(total)
        # print(col_sums)
        col += 1
        # print(col)
    return col_sums

normalize(matrix)
