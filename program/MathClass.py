import operator
from functools import reduce

class Math:
    def themes(self):
        request_theme = str(input("add\nsubtruct -sub\ndivide -div\nmultiply -mult\nprobability -prob #not done\n"))
        return request_theme
    
    def list_of_ints(self):
        str_list_of_nums = str(input("Plese enter at least two numbers separeted throw space\n")).split(" ")
        correct_list_of_nums = []
        
        for i in str_list_of_nums:
            try:
                correct_list_of_nums.append(int(i))
            except:
                continue
        
        return correct_list_of_nums
   
    
    def chooseOperation(self, theme):
        lower_theme = theme.lower()

        if lower_theme in ["add"]:
            int_list = self.list_of_ints(self)
            answer = self.add(self, int_list)   
            return answer

        if lower_theme in ["subtruct", "-sub"]:
            int_list = self.list_of_ints(self)
            answer = self.subtruct(self, int_list)    
            return answer
        
        if lower_theme in ["divide", "-div"]:
            int_list = self.list_of_ints(self)
            answer = self.divide(self, int_list)  
            return answer
        
        if lower_theme in ["multiply", "-mult"]:
            int_list = self.list_of_ints(self)
            answer = self.multiply(self, int_list)   
            return answer
        
        if lower_theme in ["probability", "-prob"]:
            print("probability is chosen but it doesn't work yet, please try again\n")
            self.chooseOperation()
        
        return False
    
    def add(self, number_list: list):
        sum = reduce(operator.__add__, number_list)
        return sum

    def subtruct(self, number_list: list):
        sub = reduce(operator.__sub__, number_list)
        return sub
    
    def multiply(self, number_list: list):
        multiplied = reduce(operator.__mul__, number_list)
        return multiplied
    
    def divide(self, number_list: list):
        divided = reduce(operator.__truediv__, number_list)
        return divided

    def probability(self):
        #number of probability that we want to find from all posible ways
        #number of all posible ways
        return