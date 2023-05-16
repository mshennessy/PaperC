# PC GH 1060 Quiz with 
# Student Name or Number :

print("Welcome to the Capitals Quiz")
score = 0
questions = {'France':'Paris', 'Ireland': 'Dublin', 'Spain': 'Madrid'}

for country, city in questions.items():

    print("What is the capital of", country, " ",end = '')
    ans = input()
    if ans.lower() == city.lower():
        score += 1
        print("Correct")
    else:
        print("Incorrect")
print ("Your score was",score)