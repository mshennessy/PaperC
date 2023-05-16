# GH 1601 Averages
# Student No (or name): ________________



def findMean(values):
    # Mean is straightforward. Add the numbers and divide by the number of numbers.
    # Also round the result to two dec places
    mean = round(sum(values)/len(values),2)
    return mean

def findMode(values):
    # Mode is more complicated. First build a frequency distribution using two lists.
    # Or using a dictionary if you prefer
    """ freqDist={}
    for i in values:
        if i in freqDist.keys():
            currentFreq = freqDist.get(i)
            currentFreq += 1
            newEntry={i:currentFreq}
            freqDist.update(newEntry)
        else:
            newEntry={i:1}
            freqDist.update(newEntry)
    # Now find the biggest value the frequencies
    biggest = max(freqDist.values())
    #Now find which key this frequency matches
    for key, value in freqDist.items():
        if value == biggest:
            mode = key
            break """
    #Using Lists
    valuesList = []
    freqList = []
    for i in values:
        if i in valuesList:
            pos = valuesList.index(i)
            freqList[pos] += 1
        else:
            valuesList.append(i)
            freqList.append(1)

    # Now find the biggest value the frequencies
    biggest = max(freqList)
    pos = freqList.index(biggest)
    mode = valuesList[pos]
    if biggest == 1:
        mode = 'X'
    return mode
    
def findMedian(values):
    # For median, rank the data and find middle value. (Odd and even case)
    values.sort()
    n = len(values)
    if n%2 == 0:
        #Even eg 4 items in list [0,1,2,3]...we want to find mean of items at index 2 and 1
        median=(values[int(n/2)]+values[(int(n/2))-1])/2
    else:
        #Odd eg 5 items in list [0,1,2,3,4]...median is at index 2 
        median=values[int((n-1)/2)]
    return median

# Test Data
#numList = [0,1,2,3,2,3,4,8,1,9]
#numList = [22,34,65,25,87,43,56,98,54,43,21,54,88,17,66,32,87,59,43,12,88,63,28,75]
#numList = [2.3,4.2,5.6,1.7]
numList = [1,2,3,4,5,6,7]

print("Welcome to the averages calculator")
print("List of numbers to be processed :",numList)

while True:
    print("Choose from these options:")
    print("\tFind Mean (1):")
    print("\tFind Median (2):")
    print("\tFind Mode (3):")
    print("\tExit (4)")
    option = int(input())
    if option == 1:
        myMean = findMean(numList)
        print("The mean of the values is",myMean)
    elif option == 2:
        myMedian = findMedian(numList)
        print("The median of the values is",myMedian)
    elif option == 3:
        myMode = findMode(numList)
        if myMode == 'X':
            print("This data has no mode")
        else:
            print("The mode of the values is",myMode)
    elif option == 4:
        print ("Good-bye")
        break
    else:
        print ("Invalid option")
        
