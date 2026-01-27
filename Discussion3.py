import math

class Rectangle():
    # Create the constructor "__init__" method
    def __init__(self, user_width, user_height):
        self.user_width = user_width
        self.user_height = user_height
    
    def __str__(self):
        return{f"A rectangle with width {self.user_width} and height {self.user_height}"}
    
    def area_calculator(self):
        return self.user_width * self.user_height
    
    def __eg__(self, other):
        if self.user_width == self.user_height:
            return True
        else:
            return False
        

    # YOUR CODE HERE



    # Create the "__str__" method

    # YOUR CODE HERE



    # Create the "area_calculator" method

    # YOUR CODE HERE



    # Create the "__eq__" method
    # 
    # Returns a boolean value

    # YOUR CODE HERE


    


def main():
    r1 = Rectangle(10, 10)
    # call the __str__ method
    print(r1.__str__())
    # call the area_calculator method
    print("Area:", r1.area_calculator())


    r2 = Rectangle(10, 15)
    print(r2.__str__())
    print("Area:", r2.area_calculator())
    # call the __eq__ method
    print(r1 == r2)
    print()

    # you can create additional rectangle objects to 
    # test your code or learn more about how the class behaves
    pass

if __name__ == "__main__":
    main()