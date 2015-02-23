#String it Together

##10
def censor (text, word):
	for words in text.split():
		#print words
		if words == word:
			#print words
			censorWord = "*" * len(words)
	newText = text.replace(word,censorWord)
	return newText

censor ("hey hey hey", "hey")

#List Your Problems

##11 - Count
def count(sequence, item):
	countSeq = 0
	for i in sequence:
		if i == item:
			countSeq += 1
	return countSeq


count([1,2,1,1], 1)

##12 - Purify
def purify(numbers):
	i = 0
	newlist=[]
	for num in numbers:
		if (num % 2 == 0):
			newlist.append(num)
	return newlist

purify([1,2,3,8,9,108])

##13 - Product
def product(numbers):
	prod = 1
	for i in numbers:
		prod = prod * i
	return prod

product([4,5,5])

##14 - Remove_Duplicates
def remove_duplicates(numbers):
	nodups = []
	for i in numbers:
		if i not in nodups:
			nodups.append(i)
	return nodups

remove_duplicates([1,1,2,3,4,4,5])

##15 - Median
def median(numbers):
	sortedlist = sorted(numbers)
	median_num = 0.0
	if (len(sortedlist) % 2 == 0):
		mid_element1 = len(sortedlist)/2
		median_num = ((sortedlist[mid_element1-1] + sortedlist[mid_element1]) / 2.0)
		return median_num
	else:
		mid = len(sortedlist)/2
		return sortedlist[mid]
		
median([7,3,1,4])


#Exam Statistics

##2 - Print those grades
def print_grades(grades):
	for i in grades:
		print i
	return 0

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
#print_grades(grades)

##4 - The sum of scores
def grades_sum(scores):
	score_sum = 0
	for i in scores:
		score_sum += i
	return  score_sum

#print grades_sum(grades)

##5 - Computing the average
def grades_average(grades):
    avg = grades_sum(grades)/float(len(grades))
    return avg

#print grades_average(grades)

##7 - Variance
def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    total_variance = (variance/len(scores))
    return total_variance

#print grades_variance(grades)
def grades_std_deviation(variance):
    return variance ** 0.5
    
#variance = grades_variance(grades)
#print grades_std_deviation(variance)

