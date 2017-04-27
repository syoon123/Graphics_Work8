from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
csStack = []
edges = []
transform = new_matrix()

# print_matrix( make_bezier() )
# print
# print_matrix( make_hermite() )
# print

parse_file( 'script', csStack, edges, screen, color )
