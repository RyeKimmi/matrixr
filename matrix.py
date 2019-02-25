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
    ln = ''
    for i in range( len( matrix[0] ) ):
        for j in range( len( matrix ) ):
            ln += str( matrix[j][i] )
            ln += ' '
        ln = ln[:-1]
        ln += '\n'
    ln = ln[:-1]
    print(ln)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    m = []
    for c in range( len(matrix[0]) ):
        m.append( [] )
        i = 0
        for r in range( len(matrix[0]) ):
            if i == c:
                m[c].append( 1 )
            else:
                m[c].append( 0 )
            i += 1
    return m

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    h2 = new_matrix(len(m2[0]), len(m2))
    for i in range(len(m2)):
        #print(i)
        #print(len(m2))
        temp = [l2 for l2 in m2[i]]
        #print(temp)
        for j in range(len(m2[i])):
            #print(j)
            #print(len(m2[i]))
            value = 0
            for k in range(len(m2[i])):
                #print(k)
                value += m1[k][j] * temp[k]
                #print(value)
            h2[i][j] = value
    for x in range(len(m2)):
        for y in range(len(m2[i])):
            m2[x][y] = h2[x][y]
    #m = new_matrix( len(m1[0]), len(m2) )
    #for i in m:
    #    for j in i:
    #        j = (m1[i][0]*m2[0][j] + m1[i][1]*m2[1][j])
    #return m

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
