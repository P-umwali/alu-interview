#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generate Pascal's triangle up to level n.
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i-1]
        
        """list: A list of lists representing Pascal's triangle up to level n.
              Each inner list represents a row of the triangle, with the
              values in the row.
        """

        for j in range(1, i):
            row.append(prev_row[j-1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle
