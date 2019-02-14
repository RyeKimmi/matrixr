from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]

matrix = new_matrix(4,8)
print(matrix)
print_matrix(matrix)
#print_matrix( ident(matrix) )

mat1 = [[1, 2, 3], [4, 5, 6]]
print( mat1 )
print_matrix( mat1 )
#print_matrix( ident(mat1) )

#mat2 = [[1, 2], [3, 4], [5, 6]]
#print_matrix( mat2 )
#print_matrix( ident(mat2) )

#draw_lines( matrix, screen, color )
#display(screen)
