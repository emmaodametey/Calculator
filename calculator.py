class Calculator:
    def __init__(self) -> None:
        pass
        
    def addition(self, first, second):
        return first + second
    
    def subtraction(self, first, second):
        return first - second
    
    def multiplication(self, first, second):
        return first * second
    
    def division(self, first, second):
        try:
            return first / second
        except ZeroDivisionError:
            print('Division by zero not allowed')