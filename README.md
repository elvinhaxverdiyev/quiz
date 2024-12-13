Quiz Program - README

Overview

This Python script is a simple command-line quiz program that asks multiple-choice questions to the user, evaluates their answers, and provides a final score as a percentage.

Features

Multiple-choice questions with options (A, B, C, D).

Immediate feedback for each question, indicating whether the answer is correct or incorrect.

Display of the correct answer for incorrect guesses.

Final score calculation as a percentage.

How It Works

Questions and Options:

The questions tuple contains the quiz questions.

The options tuple contains the possible answers for each question.

The answers tuple contains the correct answers for each question.

User Input:

The program iterates through the questions, displaying each question with its corresponding options.

The user inputs their answer by typing A, B, C, or D (case-insensitive).

Feedback:

After each question, the program checks the user’s answer against the correct answer in the answers tuple.

If the answer is correct, the program displays "CORRECT!" and increments the score.

If the answer is incorrect, the program displays "WRONG!!!" along with the correct answer.

Final Score:

The program calculates the user’s score as a percentage of the total questions answered correctly and displays it at the end.
