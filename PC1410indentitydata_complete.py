# PC1410 Identity data 
# Name and School: 

print("Enter your name, email address and phone number")

firstName = input("Enter your first name : ")
surName = input("Enter your surname : ")

validInput = False
validNonDigits = ["(",")"," "]
while not validInput:
    foundInvalidDigit=False     # This gets set true inside the for loop if
                                # we get an invalid digit
    phoneNo = input("Please enter your Irish phone number, "+firstName+" : ")
    # Convert to a list so we can manipualte digits .. strings are immutable
    phoneNoList = list(phoneNo)   
    for digit in phoneNoList:
        if not digit.isdigit():
            if digit not in validNonDigits:
                foundInvalidDigit=True
    if not foundInvalidDigit:
        # Digits are all numbers or allowed digits
        validInput = True
        
# Now process the phone number
popList = []    #Set up a list of digits to be removed
                # Don't "pop() as you go" as the indices get mucked up
for pos in range(len(phoneNoList)):
    if phoneNoList[pos] in validNonDigits:
        popList.append(pos)  # Record the position of chars to be removed

# Remove all the digits together, so the indices don't get messed up
# Also remove from the right - we reverse the list for this reason
popList.reverse()
for pos in popList:
    x = phoneNoList.pop(pos)

#And strip a leading zero if it exists
if phoneNoList[0] == '0':
    phoneNoList.pop(0)

#Now insert +353 at the start of the list
phoneNoList.insert(0,"+353")   
# Use the join function to reform the list to a string.
# Note we have left all digits as strings in the phoneNoList[]
# as we didn't need to do any arithmetic with them.
# If using join() on a list of integers, cast them individually
# as strings first
# join() is not in reference guide. The '' before .join() is the
# separator in the string e.g. 'x'.join(list) could give 8x6x9x1 etc
phoneNo= ''.join(phoneNoList)
print(phoneNo)

# Now for email. Use the same while not validInput construct 
validInput = False
validNonAlphaNum = ["@","_","-","."]
while not validInput:
    email= input("Please enter your email address : ")
    foundInvalidChar=False     # This gets set true inside the for loop if
                                # we get an invalid character
    # Convert to a list so we can manipualte characters .. strings are immutable
    for char in email:
        if not char.isalnum():
            if not char in validNonAlphaNum:
                foundInvalidChar=True
    # Chars must not just be individually valid .. order matters and there are rules
    # Check there is only 1 "@"
    if not foundInvalidChar and email.count('@') == 1:
        #check the last 3 digits of the email for .xx or the last 4 digits for .xxx
        # using the pass statement here for readability. I had prints in these positions when testing
        if email[-3] == '.' and email[-2].isalpha() and email[-1].isalpha():
            pass
        elif email[-4] == '.' and email[-3].isalpha() and email[-2].isalpha()and email[-1].isalpha():
            pass
        else:
            # invalid high level domain ... back to the while loop
            continue
        #Check if there is something before the @
        atPos = email.index('@')
        if atPos > 0:
            # Check there is something between the @ and the .ie
            # create a new string that is just the "gmail.com" part of the email address
            afterAt = email[atPos+1:]
            if afterAt.index('.') > 0:
                #There is a character between the @ and the dot
                #This is the final check so we can set validInput = True
                validInput = True


print("Thank you,",firstName, ". Your data as been stored")
dataString=firstName+','+surName+','+phoneNo+','+email+'\n'
print(dataString)
fp=open("PC1410CustData.csv",'a')
fp.write(dataString)
fp.close()


