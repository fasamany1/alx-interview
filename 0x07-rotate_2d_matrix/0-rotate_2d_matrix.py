#!/usr/bin/python3
""" Rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """
    rotates a 2d matrix 90° clockwise
    Returns: Nothing
    """
    # Replica Matrix
    replica = matrix[:]

    for i in range(len(matrix)):
        # retract column from replica
        column = [row[i] for row in replica]
        # Reverse matrix
        matrix[i] = column[::-1]
