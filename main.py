from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for entry in question_data:
    question_bank.append(Question(entry['question'], entry['correct_answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():

    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}")