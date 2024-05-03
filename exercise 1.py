import numpy as np
import matplotlib.pyplot as plt

def equation2(x):
	return (40-2*x)

def equation3(x):
	return	(60-2*x)/3
	
def equation1(x):
	return	np.full_like(x,34)
	
x = np.arange(0,40,0.5)

plt.xlim(0,40)
plt.ylim(0,40)

p1 = plt.plot(equation1(x), x, color="yellow")
p2 = plt.plot(x, equation2(x), color="blue")
p3 = plt.plot(x, equation3(x), color="red")

# Generating borders of optimal solution
q1 = np.minimum(equation1(x), equation2(x))
q2 = np.minimum(q1, equation3(x))

# Filling the optimal solution space
plt.fill_between(x, q2, color="green", alpha=0.5)
plt.show()

# Generating solutions
# generate all combinations (x,y) with x from 0 to 20 and y from 0 to 20, and pick only the ones where (x,equation1(x)) or ...
solutions1=[(x,y) for x in range(40) for y in range(40) if x==0 and y==0]
solutions2=[(x,y) for x in range(40) for y in range(40) if x==0 and equation3(x)==y]
solutions3=[(x,y) for x in range(40) for y in range(40) if equation3(x)==y and equation2(x)==y]
solutions4=[(x,y) for x in range(40) for y in range(40) if y==0 and equation2(x)==y]

print("Les sommets sont: ")
print([solutions1,solutions2,solutions3,solutions4])

z1 = [200 * sol[0] + 100 * sol[1] for sol in solutions1]
z2 = [200 * sol[0] + 100 * sol[1] for sol in solutions2]
z3 = [200 * sol[0] + 100 * sol[1] for sol in solutions3]
z4 = [200 * sol[0] + 100 * sol[1] for sol in solutions4]

print("La solution optimale est: ")
max_solution=max([z1[0],z2[0],z3[0],z4[0]])
print(max_solution)
