# BASIC MATH OPERATIONS CALCULATOR v3 #
#       by Raphael Gutierrez          #          

# NOTE: Type the selected operation in capital letters.

print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%%        M A T H        %%\n%%  C A L C U L A T O R  %%\n%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")

def add(num1, num2):
        return "\nAnswer: " + str(num1 + num2)

def sub(num1, num2):
        return "\nAnswer: " + str(num1 - num2)

def mul(num1, num2):
        return "\nAnswer: " + str(num1 * num2)

def div(num1, num2):
        return "\nAnswer: " + str(num1 / num2)

def operation():
        ask = input("What operation do you want? (ADD, SUB, MUL, DIV): ")
        if ask != "ADD" and ask != "SUB" and ask != "MUL" and ask != "DIV":
                print("\nERROR! Please enter a valid operation.\n")
        else:
                input_var1 = int(input("\nEnter the first number: "))
                input_var2 = int(input("Enter the second number: "))
                print("\nProcessing...")
                if ask == "ADD":
                        print(add(input_var1, input_var2))
                elif ask == "SUB":
                        print(sub(input_var1, input_var2))
                elif ask == "MUL":
                        print(mul(input_var1, input_var2))
                else:
                        print(div(input_var1, input_var2))

operation()

# Restart the program after using it to make another operation.
