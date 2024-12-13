questions = (
    "Dunyanin en boyuk okeani hansidir?: ",
    "H2O nəyi ifadə edir?: ",
    "Günəş sistemi neçə planetdən ibarətdir?: ",
    "İnsan bədənində neçə əsas orqan var?: "
    )

options = (("A. Sakit Okean", "B. Atlantik okean", "C. Hind okenai", "D. Qara deniz"),
           ("A. Neft", "B. Su", "C. Qizil", "D. Demir"),
           ("A. 4", "B. 7", "C. 9", "D. 8"),
           ("A. 12", "B. 8", "C. 6", "D. 4"))

answers = ("A", "B", "D", "D")
guesses = [ ]
score = 0
question_num = 0

for question in questions:
    print("-----------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter(A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!!!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
    
score = int(score / len(questions) * 100)
print(f"Your score is: {score}")
