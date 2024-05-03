import numpy as np

# We will work on the following linear algebra problem:
# max z = 14*x1 + 12*x2 + 20*x3 + 0*e1 + 0*e2 + 0*e3 + 0*e4
# with the constraints:
# x1 + e1 = 700
# x2 + e2 = 600
# x3 + e3 = 400
# 4*x1 + 3*x2 + 5*x3 + e4 = 6000
# positivity for all variables

infinity = 99999

equation1 = [1,0,0,1,0,0,0,700,infinity]
equation2 = [0,1,0,0,1,0,0,600,infinity]
equation3 = [0,0,1,0,0,1,0,400,infinity]
equation4 = [4,3,5,0,0,0,1,6000,infinity]
equationz = [14,12,20,0,0,0,0,0]

def simplex_algorithm(A,b,C):
	# 
	n,p = A.shape
