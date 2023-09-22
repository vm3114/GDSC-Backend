import random

class Questions():
    def __init__(self,data):
        self.question_data=data

    def shuffle(self):
        random.shuffle(self.question_data)

class Game():
    def __init__(self,data):
        self.question_data=data
        self.answer=None

    def show_ques(self):
        dictionary=self.question_data.pop()
        question=dictionary["text"]
        self.answer=dictionary["answer"]
        return question

    def remaining(self):
        if len(self.question_data==0):
            return False
        else:
            return True

    def check(self,answer):
        if self.answer==answer:
            print("Yep, that's correct!")
            return True
        else:
            print("Nope, that's incorrect!")
            return False



class Player():
    def __init__(self,name):
        self.name=name
        self.score=0

    def score_change(self,correct):
        if correct:
            self.score+=2
        else:
            self.score-=1



def main():
    question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
    ]

    question_bank=Questions(question_data)
    question_bank.shuffle()
    game=Game(question_bank.question_data)
    name=input("Enter your name: ")
    player=Player(name)

    for i in range(1,13):
        q = game.show_ques()
        print(f"Question {i}: {q}")
        ans = None
        temp_ans = ""

        while temp_ans == "":
            temp_ans = input("Enter t for True or f for False: ")
            if temp_ans not in "tf":
                print("Check your input!")
                temp_ans = ""

        if temp_ans in "t":
            ans="True"

        else:
            ans="False"

        correct=game.check(ans)
        print(f"{12-i} questions remain!")
        player.score_change(correct)

    print(f"Your final score is: {player.score}")

if __name__ == "__main__":
    main()
