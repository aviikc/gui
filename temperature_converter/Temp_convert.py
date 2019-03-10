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