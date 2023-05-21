# GH Formatting Output
# Student No (or name): ________________


import random

myWordList = []
myMarksList = []


for i in range(6):
    # Type in 6 words of various lengths
    subj = input("Enter a word :")
    myWordList.append(subj)
    # Randomly generate a number which will appear in 2nd column
    myMarksList.append(random.randint(0,100))
    
for j in range(len(myWordList)):
    # Print long and short words (up to 20 chars) with a gap
    # followed by a second column of numbers.
    print(myWordList[j],(20-len(myWordList[j]))*" ",end='')
    print(myMarksList[j])
          