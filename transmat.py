def transpose(matrix):
    result = []
    for col in range(len(matrix[0])):
        new_row = []
        for row in matrix:
            new_row.append(row[col])
        result.append(new_row)
    return result

# Example usage:
matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(transpose(matrix))
