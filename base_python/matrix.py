"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
#    ln = ''
#    for i in matrix:
#        for j in i:
#            ln += str(j)
#            ln += ' '
#        ln = ln[:-1]
#        ln += '\n'
#    ln = ln[:-1]
#    print(ln)

    ln = ''
    for i in range( len( matrix ) ):
        ln += str( matrix[i][j]

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    m = []
    for c in range( len(matrix) ):
        m.append( [] )
        i = 0
        for r in range( len(matrix) ):
            if i == c:
                m[c].append( 1 )
            else:
                m[c].append( 0 )
            i += 1
    return m

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    l1 = ''
    l2 = ''
    for i in m1:
        for j in i:
            l1 += str(j)
    for k in m1:
        for l in k:
            l2 += str(j)
            




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
