class Converter:
    def __init__(self, temp = 0):
        self.temperature = temp


    def cel_to_far(self, temp):
        return ((temp*(9/5)) + 32)

    def far_to_cel(self, temp):
        return ((temp - 32)*(5/9))

    def far_to_kel(self, temp):
        return ((temp − 32) * (5/9) + 273.15)

    def cel_to_kel(self, temp):
        return (temp + 273.15)

    def kel_to_cel(self, temp):
        return (temp - 273.15)

    def kel_to_far(self, temp):
        return ((9/5)*(temp - 273.15) + 32)




'''
class Menu:
    def __init__(self):
        conv = Converter()
        self.choices = {
            "1":self.c2f()
            "2":self.c2k()
            "3":self.f2c()
            "4":self.f2k()
            "5":self.k2c()
            "6":self.k2f()
        }

    def run_menu(self, choice, temp_value):
        choices[choice]

    def c2f(self, temp):
        conv.cel_to_far(temp)

    def c2k(self, temp):
        conv.cel_to_kel(temp)

    def f2c(self, temp):
        conv.far_to_cel(temp)

    def f2k(self, temp):
        conv.far_to_kel(temp)
    
    def k2c(self, temp):
        conv.kel_to_cel(temp)

    def k2f(self, temp):
        conv.kel_to_far(temp)

'''

    