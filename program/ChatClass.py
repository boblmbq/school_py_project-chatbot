"""chat on classes"""
import random
import json
from program.MathClass import Math

data = json.load(open("intents.json"))

class Chat:
    """chat class"""
    def __init__(self):
        self.math = Math()


    def greet(self):
        """greeting""" 
        greet_input = input('Hello, do you need a help or just want to speak? \n')
        self.greet_answer(greet_input)

    def can_help(self, question = "Can i help you with something else?"):
        can_help = self.confirm(f"{question}\n")
        if can_help:
            return self.greet_answer(question)
        else:
            return self.can_help( "Well then maybe you want to speak with me?")
        

    def confirm(self, custom_question = "Yes? No?"):
        """"""
        confirm_input  = input(f"{custom_question} Yes? No?: ").lower()
        if confirm_input in ["n", "no", "nicht", "nein"]:
            return False
        elif confirm_input in ['y', 'yes', 'ja', 'yep', 'genau', 'confirm', 'conf']:
            return True
        else:
            print("\n please answer only with simple statmants, for example : y, n, no, yes, nein, nicht, ja, yep")
            return self.confirm()
    
    def greet_answer(self, answer: str):
        """answering on greet fnc"""
        for i in answer.split():
            if i in ['speak']:
                #function that will ask a question on a theme like wether or how the day gone
                user_wants =  input('well as you say, I want to ask you how do you felling\n')
                response =  self.get_response(user_wants)
                return input(response + " how do you think about the weather")
                
            
            if i in ['help']:
                print('ok, these are the themes on which I can give full answer, please choose one\n')
                theme = self.math.themes(Math)
                
                math_answer = Math.chooseOperation(Math, theme)

                if math_answer == False:
                    print("\nyou have wrote the theme not correct, plese do it again\n")
                    self.greet_answer("help")

                print(f"The answer is {math_answer}")
                return self.can_help()

    def get_response(self, user_input: str):
        #need to check with which tag is the user_input most similar and take the response of the tag
        for intent in data["intents"]:
            if any(pattern in user_input.lower() for pattern in intent["patterns"]):
                return random.choice(intent["responses"])
                
        return "Sorry, I didn't understand that."


    
