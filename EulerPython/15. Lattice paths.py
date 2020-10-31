# In a 20x20 grid, there will be 40 nodes where one will have to choose to either go right or down.
# We are interested in all cases where Down = 20 and Right = 20, because only then will we get to the bottom right of the grid without trespassing it along the way.
#
# Therefore, it's only a matter of 40 choose 20 (binomial coefficients): 40!/(20!*20!)

import math

print(math.comb(40, 20))