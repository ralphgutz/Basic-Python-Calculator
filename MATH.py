# BASIC MATH OPERATIONS CALCULATOR v4 #
#       by Raphael Gutierrez          #          

# NOTE: Type the selected operation in capital letters ONLY.

print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%%        M A T H        %%\n%%  C A L C U L A T O R  %%\n%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")

def add(num1, num2):
        return "\n Answer: " + str(num1 + num2)

def sub(num1, num2):
        return "\n Answer: " + str(num1 - num2)

def mul(num1, num2):
        return "\n Answer: " + str(num1 * num2)

def div(num1, num2):
        return "\n Answer: " + str(num1 / num2)

def mod(num1, num2):
        return "\n Answer: " + str(num1 % num2)

def pow(num1, num2):
        return "\n Answer: " + str(num1 ** num2)

def operation():
        oper_list = "  ADD = Addition \n  SUB = Subtraction \n  MUL = Multiplication \n  DIV = Division \n  MOD = Modulus/Remainder \n  POW = Power/Exponent"
        print(oper_list)
        oper_input = input("\nWhat operation you want to use? ")
        if oper_input != "ADD" and oper_input != "SUB" and oper_input != "MUL" and oper_input != "DIV" and oper_input != "MOD" and oper_input != "POW":
                print("\nERROR! Please enter a valid operation.\n")
        else:
                input_var1 = int(input("\n Enter the first number: "))
                input_var2 = int(input(" Enter the second number: "))
                print("\nProcessing...")
                if oper_input == "ADD":
                        print(add(input_var1, input_var2))
                elif oper_input == "SUB":
                        print(sub(input_var1, input_var2))
                elif oper_input == "MUL":
                        print(mul(input_var1, input_var2))
                elif oper_input == "DIV":
                        print(div(input_var1, input_var2))
                elif oper_input == "MOD":
                        print(mod(input_var1, input_var2))
                else:
                        print(pow(input_var1, input_var2))

operation()
end_input = input("\nPress Enter to terminate.")

# Restart the program after using it to perform an another operation.
