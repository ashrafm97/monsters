class Monster():

    def __init__(self, name, tax_number, fur):
        self.__name = name.title()
        self.__tax_number = tax_number
        self.__fur = fur
    #encapsulated because we dont want the user to change these values


    def set_name(self, name):
        self.__name = name.title()

    def get_name(self):
        return self.__name
    ## setter sets the variable name as name with title and getter goes and grabs that


    def set_tax_no(self, tax_number):
        self.__tax_number = tax_number
    def get_tax_no(self):
        return self.__tax_number


    def set_fur_colour(self, fur):
        self.__fur = fur
    def get_fur_colour(self):
        return self.__fur