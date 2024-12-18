class Question:
    """quiz classini yaradiriq ve lazm olan parametrleri veririk"""
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer

    def show_terminal(self):
        """suallari terminalda gostermek ucun func"""
        print("--------------------")
        print(self.text)
        for option in self.options:
            print(option)

    def check_answer(self, guess):
        """Cavablaru=i yoxlamq ucun func"""
        return guess.upper() == self.answer