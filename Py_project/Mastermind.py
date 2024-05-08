"""
This is a mini project created for fun. Basically it is a number guessing game, 
where you need to guess a number based on nu,ber of digits existing and number of digits at correct position to the answer,
The user will be given 10 chance to find the correct answer, and with each wrong answer get the corresponding clues.

Creator: Ruhan Saad Dave
"""

import random

class Mastermind:
    def __init__(self, digit):
        self.digit = digit
    def __generate_new(self):
        self.__real_answer = ""
        for _ in range(0,self.digit):
            n = random.randint(0,9)
            n = str(n)
            self.__real_answer += n
        #print(self.real_answer, len(self.real_answer))
    def play(self):
        self.__generate_new()
        for chance in range(1,11):
            print('_' * 20)
            print("Current trial:", chance)
            entered_ans = input("Enter your guess:")
            #print(entered_ans, len(entered_ans))
            if entered_ans == self.__real_answer:
                print("You win in ", chance , "tries!")
                break
            else:
                self.exist = 0
                self.position = 0
                for i in range(0, self.digit):
                    if entered_ans[i] == self.__real_answer[i]:
                        self.position += 1
                    if entered_ans[i] in self.__real_answer:
                        self.exist += 1
               
                #print("Guessed number:", entered_ans)
                print("Position = ", self.position)
                print("Exist = ", self.exist)
        else:
            print("You lost the game!!!")
            print("The real answer was:", self.__real_answer)

game = Mastermind(4)
game.play()
