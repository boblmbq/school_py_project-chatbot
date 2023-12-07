"""chat on classes"""
import random
import json
from program.MathClass import Math

data = json.load(open("intents.json"))

class Chat:
    """chat class"""
    def greet(self):
        """greeting""" 
        greet_input = input('Hello, do you need a help or just want to speak? \n')
        self.greet_answer(self, greet_input)

    def can_help(self, question = "Can i help you with something else?"):
        """can i help function"""
        can_help = self.confirm(self, question)
        if can_help:
            return self.greet_answer(self, question)
        else:
            return self.can_help(self, "Well then maybe you want to speak with me?")
        

    def confirm(self, custom_question):
        """confirming"""
        confirm_input  = input(f"{custom_question}\n").lower()
        if confirm_input in ["n", "no", "nicht", "nein"]:
            return False
        elif confirm_input in ['y', 'yes', 'ja', 'yep', 'genau', 'confirm', 'conf']:
            return True
        else:
            print("\n please answer only with simple statmants, for example : y, n, no, yes, nein, nicht, ja, yep")
            return self.confirm(self, custom_question)
    
    def greet_answer(self, answer: str):
        """answering on greet fnc"""
        for i in answer.split():
            if i in ['speak']:
                #function that will ask a question on a theme like wether or how the day gone
                user_wants =  input('well as you say, I want to ask you how do you felling\n')
                response =  self.get_response(user_wants)
                return input(response + " how do you think about the weather")
                
            
            if i in ['help']:
                print('Yes, for sure, these are the themes on which I can give full answer, please choose one\n')
                theme = Math.themes(Math)
                
                math_answer = Math.chooseOperation(Math, theme)

                if math_answer is False:
                    print("\nyou have wrote the theme not correct, plese do it again\n")
                    self.greet_answer("help")

                print(f"The answer is {math_answer}")
                return self.can_help(self)

    def get_response(self, user_input: str):
        """some responce from data"""
        #need to check with which tag is the user_input most similar and take the response of the tag
        for intent in data["intents"]:
            if any(pattern in user_input.lower() for pattern in intent["patterns"]):
                return random.choice(intent["responses"])
                
        return "Sorry, I didn't understand that."


    
