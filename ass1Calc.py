#Comp thinking (a.Decompression, b.Pattern recog, c.Abstraction, d.Algo thinking)

#Instructions:

#Basic Calculator Program

#Create a simple Python program that
# 1.asks the user to input two numbers and 
# 2.a mathematical operation (addition, subtraction, multiplication, or division).
# 3.Perform the operation based on the user's input and print the result.
# 4.Validation measures to restrain user invalid inputs
#Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15

print("This is a basic calculator...you can currently use (+ , - , * , /)")

#Validation for 1st digit
while True:
    try:
        user_dig1 = int(input("Let's do arthimetics...give me your first digit:\n"))
        break #Exit loop if invalid
    except ValueError:
        print("Invalid input.Please enter a valid first digit")


#Validation for 2st digit
while True:
    try:
        user_dig2 = int(input("Give me your second digit:\n"))

        break #Exit loop if invalid
    except ValueError:
        print("Invalid input.Please enter a valid second digit")

#Allowed operators
operators = ['+', '-', '*', '/']

while True:
    userOperator = input("Kindly give me your sign to do the arithmetics from this available options (+ , - , * , /):")
    if userOperator in operators:
        break
    else:
        print(f"Invalid operator. Please use one of: {','.join(operators)}")

#Init where the answer will go
answ = None    

#Fn Prints the solution to user
def give_answer(userOperator):
    
    if userOperator == "+":
        answ = user_dig1 + user_dig2
    elif userOperator == "-":
        
        answ = user_dig1 - user_dig2
        
    elif userOperator == "*":
        
        answ = user_dig1 * user_dig2

    elif userOperator == "/":
        
        answ = float(user_dig1) / float(user_dig2)

    else:
        print("Input a valid math symbol")
        
    return print(f"{user_dig1} {userOperator} {user_dig2} = {answ}")

    
#Call the fn
give_answer(userOperator)    