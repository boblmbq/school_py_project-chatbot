"""chat on classes"""
import random
import json
from program.MathClass import Math
from difflib import SequenceMatcher

data = json.load(open("intents.json"))

class Chat:
    def greet(self):
        greet_input = input('Hello, do you need a help or just want to speak? \n')
        self.greet_answer(self, greet_input)

    def can_help(self, question = "Can i help you with something else?"):
        can_help = self.confirm(self, question)
        if can_help:
            return self.greet_answer(self, question)
        else:
            return self.can_help(self, "Well then maybe you want to speak with me?")
        

    def confirm(self, custom_question):
        confirm_input  = input(f"{custom_question}\n").lower()
        if confirm_input in ["n", "no", "nicht", "nein"]:
            return False
        elif confirm_input in ['y', 'yes', 'ja', 'yep', 'genau', 'confirm', 'conf']:
            return True
        else:
            print("\n please answer only with simple statmants, for example : y, n, no, yes, nein, nicht, ja, yep")
            return self.confirm(self, custom_question)
    
    def greet_answer(self, answer: str):
        for i in answer.split():
            if i in ['speak']:
                user_wants =  input('Then, I want to ask you how do you feel\n')
                user_response = self.update_intent(self, user_wants)
                response =  self.get_response(self, user_response)
                return self.greet_answer(self, input(response))
                
            
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
        for intent in data["intents"]:
            if any(pattern in user_input.lower() for pattern in intent["patterns"]):
                return f"{random.choice(intent["responses"])}\n"
                
        return "Sorry, I didn't understand that."
    
    def update_intent(self, user_input):
        intent_index = None
        intent_index_pattern = {}

        for intent in data["intents"]:
            for pattern in intent["patterns"]:
                similarity = SequenceMatcher(None, user_input.lower(), pattern.lower()).ratio()
                
                if similarity >= 0.7:
                    for index, next_intent in enumerate(data["intents"]):
                        if next_intent["tag"] == intent["tag"]:
                            intent_index = index
                            intent_index_pattern = data["intents"][index]
                            break

        if intent_index is None: 
            tag = str(input("how would you name the tag\n"))
            responses = str(input("which responses should be there\n"))
            new_intent = {'tag': tag, 'patterns': [user_input], 'responses': responses.split(" ")}
            data["intents"].append(new_intent)
            self.write_to_intents(self, data)

        if all(pattern != user_input for pattern in intent_index_pattern["patterns"]): 
            data["intents"][intent_index]["patterns"].append(user_input)
            self.write_to_intents(self, data)
        
        return user_input
            
    def write_to_intents(self, data):
        with open('intents.json', 'w', encoding='utf-8') as intents:
            json.dump(data, intents, ensure_ascii=False, indent=2)
            
            
            

        

                     
                     