import pandas as pd


## EXERCISES PART I

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

#1. Determine the number of elements in fruits.
print(fruits.size)

#2. Output only the index from fruits.
print(fruits.index)

#3. Output only the values from fruits.
print(fruits.values)

#4. Confirm the data type of the values in fruits.
print(fruits.dtype)

#5. Output only the first five values from fruits. Output the last three values. Output two random values from fruits.
print(fruits.head(5))
print(fruits.tail(3))
print(fruits.sample(2))

#6. Run the .describe() on fruits to see what information it returns when called on a Series with string values.
print(fruits.describe())

#7. Run the code necessary to produce only the unique string values from fruits.
print(fruits.unique())

#8. Determine how many times each unique string value occurs in fruits.
print(fruits.value_counts())

#9. Determine the string value that occurs most frequently in fruits.
print(fruits.value_counts().head(1)) #can also use .idxmax() - index max

#10. Determine the string value that occurs least frequently in fruits.
print(fruits.value_counts().nsmallest(n=1, keep ='all')) 


## EXERCISES PART II

#1. Capitalize all the string values in fruits.
print(fruits.str.capitalize())

#2. Count the letter "a" in all the string values (use string vectorization).
print(fruits.str.count('a'))

#3. Output the number of vowels in each and every string value.
def vowel_count(string):
  count = 0
  for letter in string:
    if letter in list('aeiou'):
      count += 1
  return count

print(fruits.apply(vowel_count)) 

#4. Write the code to get the longest string value from fruits.
print(fruits[fruits.str.len().idxmax()])

#5. Write the code to get the string values with 5 or more letters in the name.
print(fruits[fruits.str.len() >= 5])

#6. Use the .apply method with a lambda function to find the fruit(s) containing the letter "o" two or more times.
print(fruits[fruits.apply(lambda fruit: fruit.count('o') >= 2)])

#7. Write the code to get only the string values containing the substring "berry".
print(fruits[fruits.apply(lambda fruit: True if 'berry' in  fruit else False)])

#8. Write the code to get only the string values containing the substring "apple".
print(fruits[fruits.str.contains('apple')]) #this is a better way for 7 & 8

#9. Which string value contains the most vowels?
print(fruits[fruits.apply(vowel_count).idxmax()])


## Exercises Part IIIa

letters = pd.Series(list(    'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
))

#1. Which letter occurs the most frequently in the letters Series?
print(letters.value_counts().head(1))

#2. Which letter occurs the Least frequently?
print(letters.value_counts().tail(1))

#3. How many vowels are in the Series?
print(letters.apply(vowel_count).sum())

#4. How many consonants are in the Series?
print(len(letters) - (letters.apply(vowel_count).sum()))

#5. Create a Series that has all of the same letters but uppercased.
print(letters.str.upper())

#6. Create a bar plot of the frequencies of the 6 most commonly occuring letters.
letters.value_counts().head(6).plot.bar()


## Exercises Part IIIb

numbers = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])

#1 What is the data type of the numbers Series?
print(type(numbers))
#<class 'pandas.core.series.Series'>

#2. How many elements are in the number Series?
print(len(numbers))

#3. Perform the necessary manipulations by accessing Series attributes and methods to convert the numbers Series to a numeric data type.
numbers = numbers.str.replace('$','').str.replace(',','').astype(float)

#4. Run the code to discover the maximum value from the Series.
print(numbers.max())

#5. Run the code to discover the minimum value from the Series.
print(numbers.min())

#6. What is the range of the values in the Series?
print(numbers.max() - numbers.min())

#7. Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.
numbers = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])

numbers = numbers.str.replace('$','').str.replace(',','').astype(float)

pd.cut(numbers,4).value_counts()

#(-4511.11, 1197705.993]       7
#(3592560.778, 4789988.17]     6
#(1197705.993, 2395133.385]    4
#(2395133.385, 3592560.778]    3

#8. Plot the binned data in a meaningful way. Be sure to include a title and axis labels.
pd.cut(numbers,4).value_counts().plot.bar(title = 'Numbers in equal interval bins').set(xlabel = 'bin', ylabel = '$')


## Exercises Part IIIc


exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])

#1. How many elements are in the exam_scores Series?
print(len(exam_scores))

#2. Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.
print(f'Max = {exam_scores.max()}\nMin = {exam_scores.min()}\nMean = {exam_scores.mean()}\nMedian = {exam_scores.median()}')

#3. Plot the Series in a meaningful way and make sure your chart has a title and axis labels.
exam_scores.plot.hist(title = "Exam Scores").set(xlabel = 'Scores', ylabel = 'Frequency')

#4. Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades. Add the necessary points to the highest grade to make it 100, and add the same number of points to every other score in the Series as well.
curve_add = 100 - exam_scores.max()
curved_exam_scores = exam_scores + curve_add

#5. Use a method to convert each of the numeric values in the curved_grades Series into a categorical value of letter grades. For example, 86 should be a 'B' and 95 should be an 'A'. Save this as a Series named letter_grades.
grade_bins = [0, 60, 70, 80, 90, 100]
letter_grades = ['F', 'D', 'C', 'B', 'A']

letter_exam_scores = pd.cut(curved_exam_scores, bins = grade_bins, labels = letter_grades).value_counts()

#6. Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.
letter_exam_scores.plot.hist(title = "Exam Scores").set(xlabel = 'Scores', ylabel = 'Frequency')