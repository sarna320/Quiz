import question_model
import data
import quiz_brain
import data_trivia
question_bank = []
for question_and_answer in data.question_data:
    question_bank.append(
        question_model.Question(
            question_and_answer["text"], question_and_answer["answer"]
        )
    )
question_bank_2 = []
for question_and_answer in data_trivia.question_data:
    question_bank.append(
        question_model.Question(
            question_and_answer["question"], question_and_answer["correct_answer"]
        )
    )
# for i in range(len(q)):
#     print(q[i].text, q[i].answer)

quiz=quiz_brain.QuizBrain(question_bank_2)
quiz.next_question()
