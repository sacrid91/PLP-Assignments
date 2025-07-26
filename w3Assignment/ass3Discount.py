#Mathematical thinking (Decompression, Pattern Recog, Abstraction, Algo thinking)

#Instructions 
#1.Create a function named calculate_discount(price, discount_percent) 
#2.that calculates the final price after applying a discount.
#3.The function should take the original price (price) and the discount percentage (discount_percent) as parameters.
#4.If the discount is 20% or higher, apply the discount; otherwise, return the original price.
#5.Using the calculate_discount function, prompt the user to enter the original price of an item
#and the discount percentage. 
#6.Print the final price after applying the discount, or if no discount was applied, print the original price.

#Example Instance
#Discount = OP(Original Price * Discount Percentage 20/100 ) i.e $100 & 20% discount...
# Discount amount = $100 * 0.20 
#                  = $20
# sale price =  Original Price - Discount Amount 

#Validation for Original price
while True:
    try:
        price = int(input("Let's see if you are eligible for some discount on your item...give me the original Price of the item:\n"))
        break #Exit loop if invalid
    except ValueError:
        print("Invalid input.Please enter a valid digits not in words!")
        

while True:
    try:
        discount_percent = float(input("Let's do some discount arthimetics...now give me the Percentage(%)Discount:\nJust the number without (%) sign:"))
        break #Exit loop if invalid
    except ValueError:
        print("Invalid input.Please enter a valid digits not in words!")
        


def calculate_discount(price, discount_percent):
    discount_rate = discount_percent / 100
    
    if discount_percent >= 20:
        #Discount = OP(Original Price * Discount Percentage) i.e $100 & 20% discount...
        discountAmount = price * discount_rate
        
        #The actual sale price after %D is applied
        final_price = price - discountAmount
        return f"This is the amount you have to pay KES{final_price:.2f}"
    else:
        return f"You are not eligible, so no Discount applied.You have to pay KES{price}"
    
#Calling the fn    
result = calculate_discount(price, discount_percent)        
   
print(result)