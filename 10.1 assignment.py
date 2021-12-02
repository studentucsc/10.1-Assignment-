# Jorge Hernandez Martinez
# 10.1 Assignment: Your Own Class

class Soda:
# class Soda reprsented the information display below
    def __init__(self, calories, sugars, oz, carbohydrates):
# init method hold the class variables
        self.calories = calories
# self.calories let recalled it for the later on to be used on
        self.sugars = sugars
# self.sugars let recalled it for the later on to be used on
        self.carbohydrates = carbohydrates
# self.carbohydrates let recalled it for the later on to be used on
        self.oz = oz
# self.oz let recalled it for the later on to be used on

    def get_sugars(self):
        return self.sugars
# get_sugars a function be recalled and return as self.sugars
    def get_calories(self):
        return self.calories
# get_calories a function be recalled and return as self.sugars

    def get_carbohydrates(self):
        return self.carbohydrates
# get_carbohydrates a function be recalled and return as self.carbohydrates
    def get_oz(self):
        return self.oz
# get_oz a function be recalled and recalled and return as self.oz

class profressors:
# class profressors hold the information
    __name = "Jorge"
# Data variables of the name
    __contacts = "9165850766"
# Data variables of the contacts z


def setname(self,name):
# allow us to return the information in __name
    self.__name=name
    return self.__name

def setcontacts(self,contacts):
# allow us to return the information in __contacts
        self.__contacts=contacts
        return self.__contacts


# the def main hold the results of the functions
def main():

    coke =Soda(300, 36, 12, 20)
    print('The amount of sugars in a soda is', coke.get_sugars())
# print out the results of the get_sugars

    sprite = Soda(320, 340, 360, 380)
    print('The amount of calories in a soda is', sprite.get_calories())
# print out the result of the get_calories

    drPepper = Soda(39.8, 40.7, 42.4, 44.8)
    print('The amount of Carbohydrates in a soda is', drPepper.get_carbohydrates())
# print out the results of the get_carbohydrates

    fanta = Soda(10, 8, 6, 4,)
    print('The amount of ounce in a soda is', fanta.get_oz())
# print out the results of the get_oz

    print('The name of profressor is', __name())
# print out the information of __name
    print('The contact of the profressor is:',__contacts())
# print out the information of __contacts 

if __name__ == '__main__':
    main()