# String
word = "We were taught by two instructors today"
word2 = "Class was amazing today in CODELAB"
word3 = "53 is an example of a number"


# String slicing
newWord = word[22:34]
newWord2 = word2[27:35]
newWord3 = word3[3:9]


print(newWord)
print(newWord2)
print(newWord3)

# Assignment
# Subject= "Mathematics"
# assignment write a program that sum up the total value of Mathematics
# From the Variable write a program that display "math8matics"

david= 1
martins= 6
confidence= 1
ebuka= 2
miracle= 1
samuel= 1
colin= 2
daniel= 1
godwin= -1
joseph= -1
points= david, martins, confidence, ebuka, miracle, samuel, colin, daniel, godwin, joseph

max_point= max(points)
min_point= min(points)

print("Maximum point is " + str(max_point))
print("Minimum point is " + str(min_point))

question2 = input()
print(question2.capitalize())
print(question2[2:3])