#import our file with our functions
import MyMathFunctions

def display_menu():
    print()
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Multiply two numbers")
    print("4. Divide two numbers")
    
def display_result(result):
    print("The answer to the choice you selected, is " + str(result));
    
def main():
    #prompt user to enter two numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    #initialize the result variable
    result = 0
    #display the menu
    display_menu()
    #get choice from user
    choice = int(input("What do you want to do with those numbers?"))
    #determine which function to call
    if(choice == 1):
        result = MyMathFunctions.add_numbers(num1, num2)
    elif(choice == 2):
        result = MyMathFunctions.subtract_numbers(num1, num2)
    elif(choice == 3):
        result = MyMathFunctions.multiply_numbers(num1, num2)
    elif(choice == 4):
        result = MyMathFunctions.divide_numbers(num1, num2)
    else:
        print("You entered an invalid choice.")
        
    #display answer to user
    if(choice > 0 and choice < 5):
        display_result(result)
        
if __name__ == "__main__":
    main()
