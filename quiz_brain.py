class QuizBrain:
    def __init__(self, question_list, queststion_number=0) -> None:
        self.queststion_number=queststion_number
        self.question_list = question_list
        self.score=0

    def next_question(self):
        qurrent_question=self.question_list[self.queststion_number]
        answer = (input(f"Q.{self.queststion_number+1}: {qurrent_question.text} (True/False)?: "))
        
        if answer==qurrent_question.answer:
            self.score+=1
            print("Correct answer")

        else:
            print("Bad answer")
            print(f"The correct answer was {qurrent_question.answer}")
        print(f"Yor score {self.score}/{self.queststion_number+1}")
        if self.queststion_number< len(self.question_list)-1:
            self.queststion_number+=1
            self.next_question()
        