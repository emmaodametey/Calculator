from calculator import Calculator

def main():
    operations = ['+', '-', '*', '/']
    print('usage: a + b \n a - b \n a * b \n a / b')
    expression = input()

    hold = expression.split(' ')
    if(len(hold) != 3):
        raise Exception('Invalid computation')
    if(hold[0].isnumeric and hold[1] in operations and hold[2].isnumeric):
        calc = Calculator()
        match hold[1]:
            case '+' :
                print(calc.addition(float(hold[0]), float(hold[2])))
            case '-' :
                print(calc.subtraction(float(hold[0]), float(hold[2])))
            case '*' :
                print(calc.multiplication(float(hold[0]), float(hold[2])))
            case '/' :
                print(calc.division(float(hold[0]), float(hold[2])))
            case _:
                raise Exception('Something went wrong')
    
if (__name__ == "__main__") :
    main()