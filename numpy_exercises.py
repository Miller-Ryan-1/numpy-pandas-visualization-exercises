import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

#1. How many negative numbers are there?
neg_count = len(a[a < 0])
print(neg_count)
 # ANS = 4

#2. How many positive numbers are there?
pos_count = len(a[a > 0])
print(pos_count)
 # ANS = 5

#3. How many even positive numbers are there?
even_pos_count = len(a[(a > 0) & (a % 2 == 0)])
print(even_pos_count)
 # ANS = 3

#4. If you were to add 3 to each data point, how many positive numbers would there be?
plus_three_count = len(a[(a+3) > 0])
print(plus_three_count)
 # ANS = 10

#5. If you squared each number, what would the new mean and standard deviation be?
print(f'Old Mean = {a.mean()}, Old Stddev = {a.std()}')
new_a = a**2
print(f'New Mean = {new_a.mean()}, New Stddev = {new_a.std()}')
 # ANS = 74, 144

#6. A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data set.
centered_a = a - a.mean()
print(centered_a)
 # ANS = [  1.   7.   9.  20.  -5.  -4.  -3.  -3.  -3.  -9.   0. -10.]

#7. Calculate the z-score for each data point.
z_scores = (a - a.mean())/a.std()
print(z_scores)
 # ANS = [ 0.12403473  0.86824314  1.11631261  2.48069469 -0.62017367 -0.49613894  -0.3721042  -0.3721042  -0.3721042  -1.11631261  0.         -1.24034735]


#~~~~~~~~~~


 #8. More numpy exercises:
 ## Setup 1
a2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# Note: used 'a2' to distnguish it from variable 'a' used earlier

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a2 = a2.sum()

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a2 = a2.min()

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a2 = a2.max()

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a2 = a2.mean()

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a2 = a2.prod()

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a2 = a2**2

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a2 = a2[a2 % 2 == 1]

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a2 = a2[a2 % 2 == 0]


#~~~~~~~~~~


## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

bumpy = np.array(b)
  # transforming this list of lists into a numpy array allows you to do operations on the entire list of two lists

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

sum_of_b = np.array(b).sum()

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])

min_of_b = np.array(b).min()  

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

max_of_b = np.array(b).max()

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

mean_of_b = np.array(b).mean()

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

product_of_b = np.array(b).prod()

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

squares_of_b = np.hstack(b)**2

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

odds_in_b = np.array(b)[np.array(b) % 2 == 1]

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

evens_in_b = np.array(b)[np.array(b) % 2 == 0]

# Exercise 9 - print out the shape of the array b.
shape_of_b = np.shape(b)

# Exercise 10 - transpose the array b.
transpose_of_b = np.transpose(b)

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
reshape1x6_b = np.reshape(b,(1,6))

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
reshape6x1_b = np.reshape(b,(6,1))


#~~~~~~~~~~


## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
c_array_characteristics = [np.min(c), np.max(c), np.sum(c), np.prod(c)]

# Exercise 2 - Determine the standard deviation of c.
stddev_of_c = np.std(c)

# Exercise 3 - Determine the variance of c.

# Exercise 4 - Print out the shape of the array c

# Exercise 5 - Transpose c and print out transposed result.

# Exercise 6 - Get the dot product of the array c with c. 

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Exercise 1 - Find the sine of all the numbers in d

# Exercise 2 - Find the cosine of all the numbers in d

# Exercise 3 - Find the tangent of all the numbers in d

# Exercise 4 - Find all the negative numbers in d

# Exercise 5 - Find all the positive numbers in d

# Exercise 6 - Return an array of only the unique numbers in d.

# Exercise 7 - Determine how many unique numbers there are in d.

# Exercise 8 - Print out the shape of d.

# Exercise 9 - Transpose and then print out the shape of d.

# Exercise 10 - Reshape d into an array of 9 x 2