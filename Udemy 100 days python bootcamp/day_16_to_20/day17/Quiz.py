import Utility
class QuizBrain:
    def __init__(self):
        self.quesNum=0
        self.score=0
        self.wrong=[]
        self.questionList=[]
        for ques in Utility.questions:
            self.questionList.append(Utility.question(ques['text'],ques['answer']))

    def nextQuestion(self):
        question=self.questionList[self.quesNum] #an object of the class question, it has attributes of text and ans
        user_ans=input(f"{self.quesNum+1}.{question.text} (T/F): ").upper()
        if user_ans=='T': user_ans=True
        elif user_ans=='F': user_ans=False
        if user_ans==question.answer:
            self.score+=1
        elif user_ans!=question.answer:
            self.wrong.append(self.quesNum)
        self.quesNum+=1    

    def Results(self):
        print(f"\nFinal score:{self.score}/{len(self.questionList)}")
        if self.score!=len(self.questionList):
            print("\nQuestions that you answered incorrectly:")
            for Q_num in self.wrong:
                print(f"{Q_num+1}.{self.questionList[Q_num].text}--->{self.questionList[Q_num].answer}")
        else:
            print("Congrats! You got a perfect score!")    

quiz=QuizBrain()
print("The quiz contains 10 True or False questions on several computer science concepts and the languages SQL,Python,C and java.\nGood luck!\n")
while quiz.quesNum<len(quiz.questionList):
    quiz.nextQuestion()
quiz.Results()       
