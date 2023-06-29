#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generate Pascal's triangle up to level n.

    Args:
        n (int): The level of Pascal's triangle to generate.

    Returns:
        list: A list of lists representing Pascal's triangle up to level n.
              Each inner list represents a row of the triangle, with the
              values in the row.

        If n <= 0, an empty list is returned.

    Raises:
        None.
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i-1]

        for j in range(1, i):
            row.append(prev_row[j-1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle
