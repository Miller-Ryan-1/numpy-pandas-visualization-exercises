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
a2 = [1,2,3,4,5,6,7,8,9,10]
a2np = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# Note: used 'a2' to distnguish it from variable 'a' used earlier

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = 0
for n in a2:
    sum_of_a += n
 #or
sum_of_a2 = a2np.sum()

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = a2[0]
for n in a2:
    if n < min_of_a:
        min_of_a = n
 #or
min_of_a2 = a2np.min()

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = 0
for n in a2:
    if n > max_of_a:
        max_of_a = n
 #or
max_of_a2 = a2np.max()

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a2 = sum_ofa2/len(a2)
 #or
mean_of_a2 = a2np.mean()

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a2 = 1
for n in a2:
    product_of_a2 *= n
 #or
product_of_a2 = a2np.prod()

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a2 = [n**2 for n in a2]
 #or
squares_of_a2 = a2np**2

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a2 = []
for n in a2:
    if n % 2 == 1:
        odds_in_a2.append(n)
 #or
odds_in_a2 = a2np[a2np % 2 == 1]

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a2 = []
for n in a2:
    if n % 2 == 0:
        evens_in_a2.append(n)
 #or
evens_in_a2 = a2[a2np % 2 == 0]


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
variance_of_c = np.var(c)

# Exercise 4 - Print out the shape of the array c
shape_of_c = np.shape(c)

# Exercise 5 - Transpose c and print out transposed result.
transpose_of_c = np.transpose(c)
  # [[1 4 7]
  #  [2 5 8]
  #  [3 6 9]]

# Exercise 6 - Get the dot product of the array c with c. 
dot_prod_of_c = np.dot(c,c)

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
c_transpose_sum_of_c = (np.array(c) * np.tranpose(c)).sum()

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
c_transpose_prod_of_c = (np.array(c) * np.tranpose(c)).prod()


#~~~~~~~~~~


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Exercise 1 - Find the sine of all the numbers in d
sin_of_d = np.sin(d)

# Exercise 2 - Find the cosine of all the numbers in d
cos_of_d = np.cos(d)

# Exercise 3 - Find the tangent of all the numbers in d
tan_of_d = np.tan(d)

# Exercise 4 - Find all the negative numbers in d
neg_in_d = np.array(d)[np.array(d) < 0]

# Exercise 5 - Find all the positive numbers in d
pos_in_d = np.array(d)[np.array(d) > 0]

# Exercise 6 - Return an array of only the unique numbers in d.
unique_in_d = np.unique(d)

# Exercise 7 - Determine how many unique numbers there are in d.
unique_q_in_d = len(np.unique(d))

# Exercise 8 - Print out the shape of d.
shape_of_d = np.shape(d)

# Exercise 9 - Transpose and then print out the shape of d.
tranpose_of_d = np.transpose(d)
shape_of_tranposed_d = np.shape(np.transpose(d))

# Exercise 10 - Reshape d into an array of 9 x 2
reshape9x2_d = np.reshape(d,(9,2))