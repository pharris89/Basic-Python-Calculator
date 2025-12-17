#define our function
def add_two_numbers(number1, number2):
    sum = number1 + number2
    return sum
    
def multiply_number(firstNum, secondNum):
    sum = firstNum * secondNum
    return sum

def divide_numbers(number1, number2):
    sum = number1 / number2
    return sum
    
def subtract_number(firstNum, secondNum):
    sum = firstNum - secondNum
    return sum

def main():
    #get numers from user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    #call the add function and display the result
    sum = add_two_numbers(num1, num2)
    print("Addition answer: " + str(sum))
    
    #call the multiply function and display the answer
    product = multiply_number(num1, num2)
    print("Multiplcation answer: " + str(product))
    
    #call the division function and display the result
    sum = divide_numbers(num1, num2)
    print("Division answer: " + str(sum))
    
    #call the subtraction function and display the answer
    product = subtract_number(num1, num2)
    print("Subtraction answer: " + str(product))
    
#call main function if this file is the one the program started from
if __name__ == "__main__":
    main()
    
