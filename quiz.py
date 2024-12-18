class Quiz:
    """Quiz classi yaradiriq"""
    def __init__(self, questions):
        self.questions = questions
        self.guesses = []
        self.score = 0

    def quiz_proses(self):
        """Imtahan proeseini temsil eden func"""
        for question in self.questions:
            question.show_terminal() #suallari terminalda gosterir
            guess = input("Enter A, B, C, D: ").upper() # daxil edilen inputun boyuk herifle qebul edilmesi ucun
            self.guesses.append(guess) # verilen cavabi texminler siyahisinda tutur
            if question.check_answer(guess):
                self.score += 1 #verilen cavab dogrudursa scoreye bal elave edir
                print("CORRECT!!!")
            else:
                print("WRONG!!!")
                print(f"{question.answer} is the correct variant")

        self.show_result()

    def show_result(self):
        """sonda neticeni faizle gosterir"""
        final_score = int(self.score / len(self.questions) * 100)
        print(f"Your score is {final_score}%")
        
