def solution(rows, columns, queries):
    matrix = [[(i * columns + j + 1) for j in range(columns)] for i in range(rows)]
    
    result = []
    
    for query in queries:
        x1, y1, x2, y2 = [q - 1 for q in query] 
        
        prev_value = matrix[x1][y1]
        min_value = prev_value
        
        for y in range(y1 + 1, y2 + 1):
            matrix[x1][y], prev_value = prev_value, matrix[x1][y]
            min_value = min(min_value, prev_value)
        
        for x in range(x1 + 1, x2 + 1):
            matrix[x][y2], prev_value = prev_value, matrix[x][y2]
            min_value = min(min_value, prev_value)
        
        for y in range(y2 - 1, y1 - 1, -1):
            matrix[x2][y], prev_value = prev_value, matrix[x2][y]
            min_value = min(min_value, prev_value)
        
        for x in range(x2 - 1, x1 - 1, -1):
            matrix[x][y1], prev_value = prev_value, matrix[x][y1]
            min_value = min(min_value, prev_value)
        
        result.append(min_value)
    
    return result