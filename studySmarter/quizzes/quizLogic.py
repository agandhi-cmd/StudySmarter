class Question:
    def __init__(self, text):
        self.text = text

    def checkAnswer(self, answer):
        raise NotImplementedError
    
class MultipleChoice(Question):
    def __init__(self, text, possibleAnswers, correctAnswer):
        super().__init__(text)
        self.possibleAnswers = possibleAnswers
        self.correctAnswer = correctAnswer

    def checkAnswer(self, answer):
        return answer == self.correctAnswer
    
class TrueFalse(Question):
    def __init__(self, text, correctAnswer):
        super().__init__(text)
        self.correctAnswer = correctAnswer

    def checkAnswer(self, answer):
        return answer == self.correctAnswer
    
class shortAnswer(Question):
    def __init__(self, text, correctAnswer):
        super.__init__(text)
        self.correctAnswer = correctAnswer

    def checkAnswer(self, answer):
        return answer == self.correctAnswer

class Quiz:
    def __init__(self, title):
        self.title = title 
        self.questions = []

    def add_questions(self, question):
        self.questions.append(question)

    def run(self):
        score = 0 

        for q in self.questions:
            print(q.text)

            if hasattr(q, "options"):
                pass