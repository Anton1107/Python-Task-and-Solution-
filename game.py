answerList = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B", "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]
correctAns = 0
wrongAns = 0
userAns = []
incorrectAns = []

userInput = input("Enter your answers! :")
count = 0

if userInput.endswith(".txt"):
    file = open(userInput, 'r')
    filename = file.read().strip().splitlines()
    i = 0
    while i < 20:
        answer = filename[i].split(". ")
        i += 1
        userAns.append(answer[1].strip())

for i in answerList:
    if i == userInput[count]:
        correctAns += 1
    else:
        wrongAns += 1
        count += 1

if correctAns < 15:
    print("You have failed")
else:
    print("You have passed")

print("Your total of correct answers is :", correctAns)
print("Your total of incorrect answers is :", wrongAns)
